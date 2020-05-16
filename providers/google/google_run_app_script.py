"""
Shows basic usage of the Apps Script API.

"""
import json
from googleapiclient import errors
from googleapiclient.discovery import build

from providers.google.get_credentials import GoogleCredentials
from common.config import initialize_config
from providers.myssql_db import MySqlDB


SCRIPT_ID = '1FJi_cMqS8i1g5tvDMZa7qC60NW0vWSDf4pIOeggLSt5eIwbuPuyjJrB2'


def run_app_script(credentials=None, script_id=SCRIPT_ID,
                   function_name="myFunction",
                   params=None):
    """Calls the Apps Script API.
    """
    # store = oauth_file.Storage('token2.json')
    # creds = store.get()
    # if not creds or creds.invalid:
    #     flow = client.flow_from_clientsecrets('client.json', SCOPES)
    #     creds = tools.run_flow(flow, store)

    if not credentials:
       credentials = GoogleCredentials().get_credential_local()
    service = build('script', 'v1', credentials=credentials)

    # Call the Apps Script API
    result = []
    try:
        # Create an execution request object.
        request = {"function": function_name, "parameters": params}
        response = service.scripts().run(body=request,
                scriptId=script_id).execute()

        # print("..................")

        if 'error' in response:
            # The API executed, but the script returned an error.

            # Extract the first (and only) set of error details. The values of
            # this object are the script's 'errorMessage' and 'errorType', and
            # an list of stack trace elements.
            error = response['error']['details'][0]
            print("Script error message: {0}".format(error['errorMessage']))

            if 'scriptStackTraceElements' in error:
                # There may not be a stacktrace if the script didn't start
                # executing.
                print("Script error stacktrace:")
                for trace in error['scriptStackTraceElements']:
                    print("\t{0}: {1}".format(trace['function'],
                                              trace['lineNumber']))
        else:
            # The structure of the result depends upon what the Apps Script
            # function returns.
            result = response['response'].get('result', {})
            if not result:
                print('No result returned!')
            else:
                print("Result: ", result)

    except errors.HttpError as e:
        # The API encountered a problem before the script started executing.
        print("ERROR", e.content)
        result = {'error': e.content}

    return result


if __name__ == '__main__':
    initialize_config()
    creds = GoogleCredentials().get_credential_local()
    db = MySqlDB()
    db.connect()

    #print(db.query_commit("delete from quizzes"))
    #print(db.query_commit("delete from quiz_questions"))
    #print(db.query_commit("ALTER TABLE quiz_questions AUTO_INCREMENT=1"))

    quiz_links = [
        "https://docs.google.com/forms/d/1psEEWT9X0VfmKjE97OrYza3vnYsHyZWMkqhGkMB5N-I/edit",
        "https://docs.google.com/forms/d/e/1FAIpQLSePfn6rVDPSnlzPwZ-J4iT-I8Etdnma0zr2sJGNbvk9W9itXQ/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSdpSo8mekRI7jScqNtfuX_nUBOpOGnuuARkR1b8wSvDB26nsw/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSel8jWSvqc0jinJwsCQ2mJNDQ5zPsV1a4esQRA5GkXz-iKFdw/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSesHSSk1u_4zhiKXo3-lUgfjlTn6ikA9wmVDT7YcQp1ezZlgQ/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSe7xCDXY--JZD8dssvW1lK1fSlOYh9GULE7uxYF6d4EUZ7P1Q/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSfgniIGN07J7Mb3pYqS0BGNMJ2SOpWrTA8_gVCimcb25NC1FA/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSerQjGhaU1oAtZXNNvwgOAaogGpRzLErF8lAKntKCqHoZePbg/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSfhW7pZ2oHsPZngvSOydJ0VpfVVgEbtedW01JaQVtNHnbLgGw/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSfnLwbUmRt2_l-b0uVH8BVnYDHPl9cDIN_sf6QwzCC9KvIEHg/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSdstQSpDJgDtHUqLH7g2T7HYq1-yivr24u_U0-FyVZ3QfY9KA/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSf0StazPDOJsUP94S0TiFG-zaIwLtQk_cM3oHFGohY8qus-yA/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSfkUt8oABZNsp5NhWYwSm8ZdxSqzTahvNcw8Gd7HJUdDfMr-Q/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSerk_I5wnlbccm0DF3V4Aki3FxG07YvJXNriFiOnng3ElEK6g/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSfREh-kwG56ARUeIYqqYQk3i6NPZT_Cf4lyFpr5MinhM-U7uA/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSekPY3BgHr2Qbp-Snv8pC1Ge-79xaf15K3SL1rAAfCp6xLbJA/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSfrE1mlxJ3ABLddoKU87ica8YbwMHap9JPSDsxtItAsDoyiPA/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSeTBjhMU9J4KskMHFS-kHEzHZYNRoU7jiruUwf_NRYbKC8rMA/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSfStls1KxaIDrjWGNMLrA_tbd-OA2IlIXw6v2EfXkl_Ys2aDw/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSc5KPE7yb8hu5-_MpZ8i87UC84SLAUJKIocGS6AMUpuQUrIgQ/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLSf27hpXbxiem626bCMVQzKN0T_1EfxQVUp3_8d3itM3tdqsFg/viewform?usp=sf_link",
        "https://docs.google.com/forms/d/e/1FAIpQLScBou4QKNcBr7yXbwEhxcNGIk6J0QowKTEPx_uJ5ja8NtiOJw/viewform?usp=sf_link"
    ]
    sql_quiz = "INSERT INTO quizzes(`id`, `provider_id`, `name`, " \
               "`desciption`, `metadata`, `type`, `no_of_questions`, " \
               "`total_marks`, `questions`, `timestamp`, `responses`, " \
               "`external_link`) " \
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_ques = "INSERT INTO `quiz_questions`(`id`, `text`, `subject`, `subject_id` " \
               "`topic`, `type`, `metadata`, `choices`, `answer`) " \
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    index = 1
    for quiz in quiz_links[0:1]:
        params = [quiz, False]
        results = run_app_script(creds, function_name='getQuizDetails',
                             params=params)
        print(json.dumps(results, indent=4))
        updated = results.get('updated')
        metadata_quiz = \
        {
             'updated_timestamp': updated,
             'created_timestamp': results.get('created'),
             'quiz': results.get('title'),
             'description': results.get('description'),
             'weight': 1,
             'id': results.get('id'),
             'external_link': quiz
        }
        for item in results.get('items'):
            metadata = {
                'description': item.get('description'),
                'points': item.get('points'),
                'feedback_correct': item.get('feedback_correct'),
                'feedback_incorrect': item.get('feedback_incorrect')
            }
            values = ('', item.get('title'), 'Islam', 5,
                      item.get('description'),
                      item.get('type'), json.dumps(metadata, indent=4),
                      json.dumps(item.get('choices'), indent=4),
                      json.dumps(item.get('answer'), indent=4)
                      )
            print(values)
            #print(db.insert(sql_ques, values))

        values = (index, results.get('id'), 'Quiz ' + str(index),
                  results.get('description'),
                  json.dumps(metadata_quiz),
                  1, results.get('count_items'),
                  results.get('total_points'),
                  json.dumps(results.get('items'), indent=4),
                  updated, results.get('responses'),
                  quiz)
        print(values)
        #print(db.insert(sql_quiz, values))