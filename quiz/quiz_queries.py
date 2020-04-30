import json
import decimal
from providers.myssql_db import MySqlDB
from common.config import initialize_config

queries = ["select `id`, date_format(`creation_date`, '%Y-%c-%d %H:%i:%s') as created_at,"
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
FROM `students` group by description"""
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
        print(exc)
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
                point = 1 if a == c else 0
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
                        round(total * 100.0/(5 * no_quizzes), 2),
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



if __name__ == '__main__':
    initialize_config()
    #print(get_quizzes_by_names('Nazli'))
    #print(json.dumps(get_quizzes_by_names('FS admin', True, True), indent=4))

    #print(get_query_result(queries[1].format('Matin'.lower())))

    print(get_query_result(id=5))
