from providers.myssql_db import MySqlDB
from common.config import initialize_config

queries = ["select `id`, `creation_date`,`marks`, `name`, " \
           "`description`,`age`, `city`, `state`, " \
           "`school`, `responses` from students where name='{0}'",
           "select `id`, `creation_date`,`marks`, `name`, " \
           "`description`,`age`, `city`, `state`, " \
           "`school`, `responses` from students where lower(name)='{0}'"
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


def get_quizzes_by_names(name, ignore_case=False):
    global db
    query = queries[1] if ignore_case else queries[0]
    # print(query, name)
    sql = query.format(name if not ignore_case else name.lower())
    return connect_and_execute(sql)


def get_query_result(query):
    return connect_and_execute(query)


if __name__ == '__main__':
    initialize_config()
    print(get_quizzes_by_names('Nazli'))
    print(get_quizzes_by_names('Matin', True))

    #print(get_query_result(queries[1].format('Matin'.lower())))
