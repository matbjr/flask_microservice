import json

from common.config import initialize_config
from quiz.quiz_queries import queries, connect_and_execute
from providers.google.google_run_app_script import run_app_script, \
    GoogleCredentials
from quiz.type_map import get_type_from_id


# returns items from DB for specific filters
def get_items_db(json_data):
    subject = json_data.get('subject')
    topic = json_data.get('topic')
    limit = json_data.get('limit', 100)
    sql = queries[9].format(subject, limit)
    if topic:
        sql = queries[10].format(subject, topic, limit)
    results = connect_and_execute(sql)
    for result in results:
        result['choices'] = json.loads(result['choices'])
        result['answer'] = json.loads(result['answer'])
    return {'items': results, 'total_items': len(results)}


# extract and process items for quiz
def process_items(results):
    questions = []
    index = 1
    for result in results:
        metadata = json.loads(result['metadata'])
        choices = json.loads(result['choices'])
        # answer = json.loads(result['answer'])
        # correct = []
        # for ch in choices:
        #     point = 1 if ch in answer[0].split(";") else 0
        #     correct.append(point)
        item = {
            'question': str(index) + ". " +
                        result['text'].split(".", 1)[1],
            'desc': metadata['quiz'] + "-" + result['topic'],
            'options': choices,
            'points': metadata['points'],
            'type': get_type_from_id(result.get('type'), 'google_form'),
            'feedback_correct': metadata['feedback_correct'],
            'feedback_incorrect': metadata['feedback_incorrect'],
        }
        print(item)
        questions.append(item)
        index += 1
    return questions


# create quiz from user provided data
def create_quiz_form_db(json_data):
    title = json_data.get('quiz_name')
    desc = json_data.get('quiz_description')
    ids = json_data.get('item_ids')
    user_data = json_data.get('user_data')

    # get items from list of ids
    sql = queries[11].format(','.join(map(str, ids)))
    results = connect_and_execute(sql)
    items = process_items(results)

    creds = GoogleCredentials().get_credential()
    params = [title, desc, user_data, items, 0]
    results = run_app_script(creds, function_name='createQuiz', params=params)
    # TODO: save in DB

    return {"quiz": results}


# sample quiz
def create_quiz(subject='Islam', topic=None):
    q = queries[7]
    sql = q.format(subject)
    if topic:
        sql = queries[8].format(subject, topic)

    results = connect_and_execute(sql)
    # print(json.dumps(results, indent=4))
    items = process_items(results)
    user = json.loads(results[0]['user_profile'])
    pt = "We are compiling the results for 25 Quizzes. " \
         "Please complete any missed ones before the 29th of Ramadan.\n\n" \
         "We are very grateful for your overwhelming response, " \
         "support and feedback to our daily Ramadan quizzes. " \
         "Ramadan will shortly be over but our striving to gain knowledge " \
         "should continue. We will soon be introducing a feature to allow " \
         "you to contribute your own questions and create your own quizzes. " \
         "Please look out for more updates on this soon."

    creds = GoogleCredentials().get_credential()
    params = ['Ramadan 2020 Quiz Review 4',
              "All " + topic + " Questions (" + str(len(results)) + "). "
              "See all quizzes here: http://muslimscholars.info/quiz/\n\n" + pt,
              user, items, 0]
    return run_app_script(creds, function_name='createQuiz', params=params)


if __name__ == '__main__':
    initialize_config()
    print(json.dumps(create_quiz(topic='Seerah'), indent=4))

    ids = [1, 3, 6, 9, 25]
    json_data = {'quiz_description': 'Test', 'quiz_name': 'Form 2',
                 'item_ids': ids}

    #print(json.dumps(create_quiz_form_db(json_data), indent=4))

    # sql = queries[11].format(','.join(map(str, ids)))
    # print(sql)
    # res = connect_and_execute(sql)
    # print(json.dumps(res, indent=4))
