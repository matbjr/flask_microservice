import json
from providers.myssql_db import MySqlDB
from common.config import initialize_config

queries = ["select `id`, date_format(`creation_date`, '%Y-%c-%d %H:%i:%s') as created_at,"
           "`marks`, `name`, `description`,`age`, `city`, `state`, " \
           "`school`, `responses` from students where name='{0}'",

           "select `id`, `creation_date`,`marks`, `name`, " \
           "`description`,`age`, `city`, `state`, " \
           "`school`, `responses` from students where lower(name)='{0}'",

           "select s.`id`, date_format(`creation_date`, '%Y-%c-%d %H:%i:%s') as created_at, "
           "`marks`, s.`name`, `description`, "
           "`age`, `city`, `state`, `school`, s.`responses`, questions "
           "from students s inner join quizzes q on s.description=q.name "
           "where s.name='{0}'",
           ]

db = None


def connect_and_execute(sql):
    global db
    if not db:
        db = MySqlDB()
        db.connect()
    try:
        results = db.query(sql)
    except Exception as exc:
        print(exc)
        db.connect()
        results = db.query(sql)

    return results


def get_quizzes_by_names(name, ignore_case=False, get_questions=False):
    global db
    query = queries[1] if ignore_case else queries[0]
    if get_questions:
        query = queries[2]
    # print(query, name)
    sql = query.format(name if not ignore_case else name.lower())
    results = connect_and_execute(sql)
    for quiz in results:
        your_answers = json.loads(quiz['responses'])
        score = int(quiz['marks'].split('/')[0].strip())
        quiz['score'] = score
        if 'questions' in quiz:
            questions = json.loads(quiz['questions'])
            quiz.pop('questions')
            quiz['responses'] = []
            for q, c, a in zip(questions['questions'],
                               questions['correct_answers'],
                               your_answers):
                quiz['responses'].append({
                    'question': q,
                    'correct': c,
                    'your_answer': a,
                    'point': 1 if a == c else 0})

    return results


def get_query_result(query):
    return connect_and_execute(query)


if __name__ == '__main__':
    initialize_config()
    print(get_quizzes_by_names('Nazli'))
    print(json.dumps(get_quizzes_by_names('Matin', True, True), indent=4))

    #print(get_query_result(queries[1].format('Matin'.lower())))
