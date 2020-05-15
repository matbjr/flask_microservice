import json
import decimal
from providers.myssql_db import MySqlDB
from common.config import initialize_config
from quiz.subjects import subjects as subjects_json
from quiz.type_map import get_type_id

queries = [
    "select `id`, date_format(`creation_date`, '%Y-%c-%d %H:%i:%s') as created_at,"
    "`marks`, `name`, `description`,`age`, `city`, `state`, " \
    "`school`, `responses` from students where name='{0}'",

    "select `id`, date_format(`creation_date`, '%Y-%c-%d %H:%i:%s') "
    "as created_at,`marks`, `name`, " \
    "`description`,`age`, `city`, `state`, " \
    "`school`, `responses` from students where lower(name)='{0}'",

    "select s.`id`, date_format(`creation_date`, '%Y-%c-%d %H:%i:%s') "
    "as created_at, `marks`, s.`name`, `description`, "
    "`age`, `city`, `state`, `school`, s.`responses`, questions "
    "from students s inner join quizzes q on s.description=q.name "
    "where s.name='{0}'",

    "select s.`id`, date_format(`creation_date`, '%Y-%c-%d %H:%i:%s') "
    "as created_at, `marks`, s.`name`, `description`, "
    "`age`, `city`, `state`, `school`, s.`responses`, questions "
    "from students s inner join quizzes q on s.description=q.name "
    "where s.name like '{0}%' and age={1}",

    "SELECT count(*) as count, COUNT(DISTINCT(name)) as names, "
    "COUNT(DISTINCT(school)) as schools, "
    "COUNT(DISTINCT(state)) as states, "
    "COUNT(DISTINCT(description)) as quizzes,"
    "COUNT(DISTINCT(city)) as cities, min(age) as min_age, "
    "max(age) as max_age, round(avg(age), 2) as avg_age "
    "FROM `students` where age>4 and age<100",

    """SELECT  count(*) as count, description as quiz,
sum(case when marks='5 / 5' then 1 else 0 end) as all_correct,
sum(case when marks='5 / 5' then 1 else 0 end) * 100.0/count(*) as all_correct_perc,
sum(case when marks='4 / 5' then 1 else 0 end) as four_correct,
sum(case when marks='4 / 5' then 1 else 0 end) * 100.0/count(*) as four_correct_perc,
sum(case when marks='3 / 5' then 1 else 0 end) as three_correct,
sum(case when marks='3 / 5' then 1 else 0 end) * 100.0/count(*) as three_correct_perc,
sum(case when marks='2 / 5' then 1 else 0 end) as two_correct,
sum(case when marks='2 / 5' then 1 else 0 end) * 100.0/count(*) as two_correct_perc,
sum(case when marks='1 / 5' then 1 else 0 end) as one_correct,
sum(case when marks='1 / 5' then 1 else 0 end) * 100.0/count(*) as one_correct_perc,
sum(case when marks='0 / 5' then 1 else 0 end) as zero_correct,
sum(case when marks='0 / 5' then 1 else 0 end) * 100.0/count(*) as zero_correct_perc 
FROM `students` group by description order by cast(substring(description, 5) as unsigned)""",
    "select name, external_link, cast(substring(name, 5) as unsigned) as number from quizzes order by cast(substring(name, 5) as unsigned)"
    ]


db = None


def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError


def connect_and_execute(sql, is_dict=True):
    global db
    if not db:
        db = MySqlDB()
        db.connect()
    try:
        results = db.query(sql, is_dict)
    except Exception as exc:
        # print(exc)
        db.connect()
        results = db.query(sql, is_dict)

    return results


def get_quizzes_by_names(name, ignore_case=False,
                         get_questions=False, age=None):
    global db
    query = queries[1] if ignore_case else queries[0]
    if get_questions:
        query = queries[2]
        if age:
            query = queries[3]
    # print(query, name)
    if age:
        sql = query.format(name, age)
    else:
        sql = query.format(name if not ignore_case else name.lower())
    results = connect_and_execute(sql)
    total = 0
    no_quizzes = len(results)
    topic_scores = {'Aqeedah': 0, 'Qur`an': 0, 'Fiqh': 0,
                    'Seerah': 0, 'History': 0}
    topic_max_scores = {'Aqeedah': 0, 'Qur`an': 0, 'Fiqh': 0,
                        'Seerah': 0, 'History': 0}
    for quiz in results:
        your_answers = json.loads(quiz['responses'])
        score = int(quiz['marks'].split('/')[0].strip())
        quiz['score'] = score
        total += score
        if 'questions' in quiz:
            questions = json.loads(quiz['questions'])
            quiz.pop('questions')
            quiz['responses'] = []
            for q, c, a, t in zip(questions['questions'],
                                  questions['correct_answers'],
                                  your_answers, questions['topics']):
                point = 1 if a in c.split(";") else 0
                quiz['responses'].append({
                    'question': q,
                    'correct': c,
                    'your_answer': a,
                    'topic': t,
                    'point': point})
                topic_scores[t] += point
                topic_max_scores[t] += 1

    total_scores = {'No. of Quizzes': no_quizzes,
                    'Combined score': total,
                    'Combined score Percentage':
                        round(total * 100.0 / (5 * no_quizzes), 2),
                    'Topic Scores': topic_scores,
                    'Topic Max Scores': topic_max_scores
                    }
    return {"quizzes": results, "total_scores": total_scores}


def get_query_result(query=None, id=None):
    id = int(id)
    if id >= len(queries):
        return {'error': 'No queries'}

    if id:
        return json.loads(json.dumps(connect_and_execute(queries[id]),
                                     default=decimal_default))
    elif query:
        return connect_and_execute(query)
    else:
        return {}


# function to process the question from UI
def insert_item(item_data):
    sql = "INSERT INTO `questions` (`id`, `text`, `subject`, `subject_id`, " \
          "`topic`, `topic_id`, `sub_topics`, `sub_topics_id`, `type`, " \
          "`metadata`, `choices`, `answer`) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    tags = item_data.get('tags')

    # Getting choices and answer
    item_choices = item_data.get('item_choices', [])
    choice_list = []
    answer_list = []
    for i in item_choices:
        choice_list.append(i.get('choice', ''))
        if i.get('correct') == 1:
            answer_list.append(i.get('choice'))
    choices = ', '.join(choice_list)
    answers = ', '.join(answer_list)

    # Getting metadata
    metadata = json.dumps(item_data)

    # Getting type info
    item_type = get_type_id(tags.get('item_type'))

    # Getting subject, topic, and hierarchy info
    subject_list = subjects_json.get('subject_list')
    paths = tags.get('paths')
    subject = tags.get('subject')
    subject_id = None
    topic = None
    topic_id = None
    sub_topics = None
    sub_ids = None
    if paths is not None:
        topic = {}
        topic_id = {}
        sub_topics = {}
        sub_ids = {}
        for sub in subject_list:
            if sub.get('label') == subject:
                subject_id = sub.get('subject_id')
                break

        index = 0
        for path in paths:
            curr_topic = None
            curr_topic_id = None
            curr_sub_topics = None
            curr_sub_ids = None
            path = path.replace('children.', '')
            split_path = path.split('.')
            del split_path[0]
            if split_path:
                curr_topic_id = int(split_path[len(split_path)-1])
                del split_path[len(split_path)-1]
            if split_path:
                curr_sub_ids = list(map(int, split_path))

            for i in subject_list:
                if i.get('subject_id') == subject_id:
                    if curr_sub_ids:
                        curr_sub_topics = []
                        children = i.get('children')
                        for j in curr_sub_ids:
                            for k in children:
                                if j == children.index(k):
                                    child = children[j]
                                    curr_sub_topics.append(child.get('label'))
                                    children = child.get('children')
                                    break
                        for j in children:
                            if curr_topic_id == children.index(j):
                                curr_topic = j.get('label')
                    elif curr_topic_id:
                        children = i.get('children')
                        for j in children:
                            if curr_topic_id == children.index(j):
                                curr_topic = j.get('label')
                                break
                    break

            topic[index] = curr_topic
            topic_id[index] = curr_topic_id
            sub_topics[index] = curr_sub_topics
            sub_ids[index] = curr_sub_ids
            index += 1

        topic = json.dumps(topic)
        topic_id = json.dumps(topic_id)
        sub_topics = json.dumps(sub_topics)
        sub_ids = json.dumps(sub_ids)

    values = (tags.get('id', ''), tags.get('item_text', ''), subject, subject_id, topic,
              topic_id, sub_topics, sub_ids, item_type, metadata, choices, answers)

    db = MySqlDB()
    db.connect()
    return {'response': db.insert(sql, values)}


if __name__ == '__main__':
    initialize_config()
    # print(get_quizzes_by_names('Nazli'))
    # print(json.dumps(get_quizzes_by_names('FS admin', True, True), indent=4))

    # print(get_query_result(queries[1].format('Matin'.lower())))

    item = {
      "tags": {
        "item_text": "123123123",
        "subject": "Biology",
        "item_type": "Multiple Choice",
        "grade_min": "1",
        "grade_max": "12",
        "privacy": 1,
        "paths": [
          "1.children.1"
        ]
      },
      "item_choices": [
        {
          "correct": 0,
          "choice": "123"
        },
        {
          "correct": 1,
          "choice": "123"
        },
        {
          "correct": 0,
          "choice": "123123"
        },
        {
          "correct": 0,
          "choice": "234234"
        }
      ]
    }

    insert_item(item)
    sql = "SELECT * FROM `questions`"
    db = MySqlDB()
    db.connect()
    # db.query("TRUNCATE TABLE `questions`", False)
    print(db.query(sql, True))
