from googleapiclient.discovery import build

from providers.google.get_credentials import get_credential, \
    get_cred, get_credential_from_token


def get_sheet(creds=None, sheet=None, range=None):
    if not creds:
        creds = get_cred()

    SPREADSHEET_ID = sheet or "1W8m1I_eMccRQ9eGdOaucckmem0Jyf-5cmJzyA3wQB-k"
    RANGE_NAME = range or 'Student Submissions'
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    #print(values)
    return values


def list_courses(creds=None):
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    if not creds:
        creds = get_cred()

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])

    if not courses:
        print('No courses found.')
    else:
        print('Courses:')
        print(courses)
        for course in courses:
            print("\t", course['id'], course['name'], course['courseState'])

    return courses


def list_course_work(creds=None, course_id="78180851867"):
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    if not creds:
        creds = get_cred()

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    results = service.courses().courseWork().list(courseId=course_id).execute()
    # print(results)
    course_works = results.get('courseWork', [])

    if not course_works:
        print('No course work found.')
    else:
        print('Course Work:')
        for course in course_works:
            print("\t", course['id'], course['title'], course['state'], course['workType'])

    return course_works


def list_student_responses(creds=None, students={},
                           course_id="78180851867",
                           coursework_id="77680692780"):
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    if not creds:
        creds = get_cred()

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    results = service.courses().courseWork().studentSubmissions().list(
        courseId=course_id, courseWorkId=coursework_id).execute()
    #print(results)
    submissions = results.get('studentSubmissions', [])
    # print(len(submissions))
    if not submissions:
        print('No submissions found.')
    else:
        print('Submissions for ',  coursework_id)
        print("\t", "Student", "\t\t\t\t\t", "State", "\t", "Type",
              "\t", "Length",  "\t\t", "State",  "\t", "Grade")
        for submission in submissions:
            state_history = {}
            grade_history = {}
            history = submission.get('submissionHistory', [])
            if history:
                state_history = history[-1].get('stateHistory', {})
                grade_history = history[-1].get('gradeHistory', {})

            print("\t",
                  students.get(submission["userId"], {}).get("email"), "\t",
                  submission['state'], "\t", submission['courseWorkType'],"\t",
                  len(history), "\t", state_history.get('state'),
                  "\t", grade_history.get('pointsEarned'), "/", grade_history.get('maxPoints'))

    return submissions


def list_students_teachers(creds=None, teachers=False, course_id="78180851867"):
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    if not creds:
        creds = get_cred()

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    if teachers:
        results = service.courses().teachers().list(
            courseId=course_id).execute()
        # print(results)
        students = results.get('teachers', [])
    else:
        results = service.courses().students().list(
            courseId=course_id).execute()
        # print(results)
        students = results.get('students', [])
    #print(len(submissions))
    student_dict = {}
    if not students:
        print('No ', 'student' if not teachers else 'teacher',' found.')
    else:
        print('Teachers' if teachers else 'Students:')
        for student in students:
            student_dict[student['userId']] = {
                'name': student['profile'].get('name'),
                'email': student['profile'].get('emailAddress'),
                'user_id': student['userId']}

            print("\t", student['profile'].get('emailAddress'),
                  student['profile'].get('name'),
                  student['userId'])

    return student_dict


def add_course(creds=None):
    if not creds:
        creds = get_cred()

    service = build('classroom', 'v1', credentials=creds)
    course = {
        'name': 'Middle School Science',
        'section': 'Period 4',
        'descriptionHeading': 'Welcome to Mid School Science Class',
        'description': """We'll be learning about Mid level Science 
           from a combination of textbooks, guest lectures, and online material. 
           Expect to be excited!""",
        'room': '305',
        'ownerId': 'matin.baji@reliabilitymeasures.com',
        'courseState': 'PROVISIONED'
    }
    course = service.courses().create(body=course).execute()
    print('Course created: {0} ({1})'.format(course.get('name'),
                                             course.get('id')))


if __name__ == '__main__':

    # creds = get_cred()
    # add_course()

    #creds = get_credential('token2.pickle')

    token_id = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImY5ZDk3YjRjYWU5MGJjZDc2YWViMjAwMjZmNmI3NzBjYWMyMjE3ODMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiODA3Njg2NTA0MTk4LWs5b2I1czRnNGt1bnVma3J0YjZtYjlzNnNyM2RrYXR1LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiODA3Njg2NTA0MTk4LWs5b2I1czRnNGt1bnVma3J0YjZtYjlzNnNyM2RrYXR1LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTAyOTE5Njg2OTIwNjYxNzU2NTU1IiwiZW1haWwiOiJmYXJydWtoNTAzQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoidDJKZHpOS3pGaXdzeDk2WVpVbkVWUSIsIm5hbWUiOiJGYXJydWtoIFNoYWh6YWQiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FPaDE0R2dqeUlLMU13WGNRd1RvRm9lM3dkV0oxMDRRN1NLalF3X0tIcmR3N0E9czk2LWMiLCJnaXZlbl9uYW1lIjoiRmFycnVraCIsImZhbWlseV9uYW1lIjoiU2hhaHphZCIsImxvY2FsZSI6ImVuIiwiaWF0IjoxNTg3ODI5NzgyLCJleHAiOjE1ODc4MzMzODIsImp0aSI6IjVmZDMyMmE3YjUzYmFiMWI5ZjU4M2FhNmMzMzllZjY2YzQ2MDJiMmYifQ.OJLWVoN51i88F_Uc9sa5YN-r2r3Dzhw4JD4yWfjnZn2-2UCv0rRniH2IdgUHNf1YwuFgVz1ny7jXBdcgt5v-xNWniDYsTAs22-8NO_qfeJu66svtRyT-r0l91KUOtVbhcQg0ZfhkZdf61n7MH3ACMu_DWCkUeKfCuJvlzH7YYv0KXXqq6eOIAeV27B6-HTmJ38qSTCesAvte0ct9ktcUxnZTImgAInwyq1p4L4q2Kit9jUrbihXShLcq_lDS6DW_sD6NwVKQjY96sxibbuFqjxB8I7Y3Sxf1FZeNOiLSH-0WbhEJsasM77PK0CIv3gZyFyHdIp3WNDHt66XmaXxR0Q"
    access_token = "ya29.a0Ae4lvC1_O-Bsx_aCrA8PSWoLcxz5c1a0yep47KVyqRwatG-ha0ykCFbmO7h47rQRXal1uYnV-ufSac3ilUOpo3hMxnDayvAKANL3zcxAht7ICz3NbyLXwfHiMVYOETS2fsvKIR-JXetL7brFrTAfXpXRzNrNjWaUUxQ"
    creds = get_credential_from_token(token_id, access_token)
    print(creds.refresh_token, creds.client_id, creds.client_secret, creds.id_token)

    courses = list_courses(creds)
    print("**********************************")
    for course in courses:
        course_works = list_course_work(creds, course_id=course['id'])

        students = list_students_teachers(creds, course_id=course['id'])
        #print(students)
        teachers = list_students_teachers(creds, teachers=True, course_id=course['id'])
        #print(students)

        print("**********************************")

        for work in course_works:
            list_student_responses(creds, students=students,
                                   course_id=course['id'],
                                   coursework_id=work['id'])
            print("++++++++++++++++++++++++++++++++++")
