import json
from googleapiclient.discovery import build
from providers.google.get_credentials import GoogleCredentails
from providers.myssql_db import MySqlDB
from common.config import get_config, initialize_config


QUIZES = ['1wxJ2TAM75oPu_JM8g6OfHHmq-Zy2K4H0hj3RzEoWrko',
          '1YqKgwDOcaXV18ndcmFxUi74mtzbVDMC9EXOIRxenQ6M',
          '1bGPWCeTQDO2fvMrmm8qsVqc9HrtDUvgjz3uEHYosI5U',
          '1ap2RTfete16Q76KWefeM8TF59XjVugzF-unGTJOk85k'
          ]


def get_sheet(creds=None, sheet_id=None, col_range=None):
    if not creds:
        creds = GoogleCredentails().get_cred()

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id,
                                range=col_range).execute()
    values = result.get('values', [])
    #print(values)

    return values


if __name__ == '__main__':

    initialize_config()
    creds = GoogleCredentails().get_cred()
    db = MySqlDB()
    # print(db)
    db.connect()

    print(db.query("show tables"))

    close = 0
    index = 1
    sql_quiz = "INSERT INTO quizzes(`id`, `provider_id`, `tilte`, " \
               "`desciption`, `metadata`, `type`, `no_of_questions`, " \
               "`total_marks`, `questions`) " \
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_ques = "INSERT INTO `questions`(`id`, `text`, `subject`, " \
               "`subject_id`, `topic`, `topic_id`, `sub_topics`, " \
               "`sub_topics_id`, `type`, `metadata`, `choices`, " \
               "`answer`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    for quiz in QUIZES:
        responses = get_sheet(creds, sheet_id=quiz,
                              col_range="Form Responses 1")
        print("Quiz ", index, quiz, len(responses))
        head = responses[0]
        answers = responses[1]

        questions = []
        correct_answers = []
        metadata = []
        start = 5
        for h in head[:start]:
            metadata.append(h)

        for h in head[start:]:
            questions.append(h)

        for a in answers[start:]:
            correct_answers.append(a)

        ques_dict = {'questions': questions,
                     'correct_answers': correct_answers
                     }
        values = (index, quiz, 'Quiz ' + str(index), '', json.dumps(metadata),
                  1, len(head[:start]), 5, json.dumps(ques_dict))

        db.insert(sql_quiz, values)

        print(values)

        index += 1


        # for g in responses:
        #     if not g:
        #         close += 1
        #     else:
        #         print(g)
        #     if close > 2:
        #         break
