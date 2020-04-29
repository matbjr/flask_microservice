import json
from datetime import datetime

from googleapiclient.discovery import build
from providers.google.get_credentials import GoogleCredentials
from providers.myssql_db import MySqlDB
from common.config import initialize_config


QUIZES = ['1wxJ2TAM75oPu_JM8g6OfHHmq-Zy2K4H0hj3RzEoWrko',
          '1YqKgwDOcaXV18ndcmFxUi74mtzbVDMC9EXOIRxenQ6M',
          '1bGPWCeTQDO2fvMrmm8qsVqc9HrtDUvgjz3uEHYosI5U',
          '1ap2RTfete16Q76KWefeM8TF59XjVugzF-unGTJOk85k',
          '1BR88xMigzYiA_eN3h5S-8sUI1QIDwAs02gfuuanJ13o',
          '1Z75Hg9k3TTMF4ZPSMOMn_2Ccs5wHsbkxBU_MHMWOEo8'
          ]


def datetime_format(datestr, fr="%m/%d/%Y %H:%M:%S", to="%Y-%m-%d %H:%M:%S"):
    dt = datetime.strptime(datestr, fr)
    return datetime.strftime(dt, to)


def get_sheet(creds=None, sheet_id=None, col_range=None):
    if not creds:
        creds = GoogleCredentials().get_cred()

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id,
                                range=col_range).execute()
    values = result.get('values', [])

    #gs = sheet.get(spreadsheetId=sheet_id)
    #print(gs)

    return values


if __name__ == '__main__':

    initialize_config()
    creds = GoogleCredentials().get_cred()
    db = MySqlDB()
    # print(db)
    db.connect()

    print(db.query("show tables"))

    close = 0
    index = 1
    sql_quiz = "INSERT INTO quizzes(`id`, `provider_id`, `name`, " \
               "`desciption`, `metadata`, `type`, `no_of_questions`, " \
               "`total_marks`, `questions`, `timestamp`, `responses`) " \
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_ques = "INSERT INTO `questions`(`id`, `text`, `subject`, " \
               "`subject_id`, `topic`, `topic_id`, `sub_topics`, " \
               "`sub_topics_id`, `type`, `metadata`, `choices`, " \
               "`answer`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_responses = "INSERT INTO `students`(`id`, `creation_date`,`marks`, `name`, " \
                  "`description`,`age`, `city`, `state`, " \
                  "`school`, `responses`) VALUES " \
                  "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    for quiz in QUIZES:
        rows = get_sheet(creds, sheet_id=quiz,
                              col_range="Form Responses 1")
        print("Quiz ", index, quiz, len(rows))
        head = rows[0]
        answers = rows[1]
        choices = []

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
            choices.append(set())

        # get all responses
        all_responses = []
        for row in rows[1:]:
            i = 0
            loc = row[4].strip()
            location = loc.replace(',', '/').replace(' ', '/').split('/')
            values = ('', datetime_format(row[0]), row[1], row[2].strip(),
                      'Quiz ' + str(index), row[3],
                      location[0].strip(), )
            if len(location) > 1:
                values += (location[1].strip(),)
            else:
                values += (location[0].strip(),)
            if len(location) > 2:
                values += (location[2].strip(),)
            else:
                values += (location[0].strip(),)

            responses = []
            for a in row[start:]:
                choices[i].add(a)
                responses.append(a)
                i += 1
            values += (json.dumps(responses), )
            print(values)
            all_responses.append(values)

        print(db.insert(sql_responses, all_responses))

        # change and sort all set() to list for json
        options = []
        for ch in choices:
            op = list(sorted(ch))
            print(len(op), op)
            options.append(op)

        ques_dict = {'questions': questions,
                     'correct_answers': correct_answers,
                     'choices': options
                     }
        values = (index, quiz, 'Quiz ' + str(index), '', json.dumps(metadata),
                  1, len(head[:start]), 5, json.dumps(ques_dict),
                  datetime_format(answers[0]), len(rows)-1)

        #print(sql_quiz + str(values))

        #print(db.insert(sql_quiz, values))

        index += 1


        # for g in responses:
        #     if not g:
        #         close += 1
        #     else:
        #         print(g)
        #     if close > 2:
        #         break
