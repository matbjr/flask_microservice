from googleapiclient.discovery import build


from providers.google.get_credentials import GoogleCredentails

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses',
          'https://www.googleapis.com/auth/classroom.coursework.me',
          'https://www.googleapis.com/auth/classroom.coursework.students',
          'https://www.googleapis.com/auth/classroom.rosters',
          'https://www.googleapis.com/auth/classroom.profile.emails',
          'https://www.googleapis.com/auth/spreadsheets.readonly',
          'https://www.googleapis.com/auth/forms']

# https://www.googleapis.com/auth/classroom.topics
# https://www.googleapis.com/auth/classroom.push-notifications
# https://www.googleapis.com/auth/classroom.announcements

QUIZES = ['1wxJ2TAM75oPu_JM8g6OfHHmq-Zy2K4H0hj3RzEoWrko',
          '1YqKgwDOcaXV18ndcmFxUi74mtzbVDMC9EXOIRxenQ6M',
          '1bGPWCeTQDO2fvMrmm8qsVqc9HrtDUvgjz3uEHYosI5U'
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

    creds = GoogleCredentails().get_cred()

    # responses = get_sheet(creds)
    # print("Responses: ", len(responses))
    #
    # for d in responses:
    #     print(d)
    #
    # print("**********************************")
    close = 0
    index = 1
    for quiz in QUIZES:
        responses = get_sheet(creds, sheet_id=quiz,
                              col_range="Form Responses 1")
        print("Quiz ", index, quiz, len(responses))
        index += 1
        for g in responses:
            if not g:
                close += 1
            else:
                print(g)
            if close > 2:
                break
