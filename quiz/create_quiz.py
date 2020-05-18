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
        metadata = result['metadata']
        choices = result['choices']
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
            'type': get_type_from_id(result.get('type'), 'google_form')
        }
        #print(item)
        questions.append(item)
        index += 1
    return questions


# create quiz from user provided data
def create_quiz_form_db(json_data):
    title = json_data.get('title')
    desc = json_data.get('description')
    ids = json_data.get('ids')
    user_data = json_data.get('user_data')

    # get items from list of ids
    sql = queries[11].format(ids)
    results = connect_and_execute(sql)
    items = process_items(results)

    creds = GoogleCredentials().get_credential()
    params = [title, desc, items]
    results = run_app_script(creds, function_name='createQuiz', params=params)
    # TODO: save in DB

    return {"quiz": results}


# sample quiz
def create_quiz(subject='Islam', topic=None):
    q = queries[7]
    print(q)
    sql = q.format(subject)
    if topic:
        sql = queries[8].format(subject, topic)

    results = connect_and_execute(sql)
    for result in results:
        result['choices'] = json.loads(result['choices'])
        result['metadata'] = json.loads(result['metadata'])
        result['user_profile'] = json.loads(result['user_profile'])
        result['answer'] = json.loads(result['answer'])

    print(json.dumps(results, indent=4))
    items = process_items(results)

    creds = GoogleCredentials().get_credential()
    params = ['Ramadan 2020 Quiz Review 1',
              "All " + topic + " Questions (" + str(len(results)) + "). "
              "See all quizzes here: http://muslimscholars.info/quiz/",
              None,  items]
    return run_app_script(creds, function_name='createQuiz', params=params)


if __name__ == '__main__':
    initialize_config()
    print(json.dumps(create_quiz(topic='Aqeedah'), indent=4))
