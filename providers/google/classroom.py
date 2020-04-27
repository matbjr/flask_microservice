from __future__ import print_function
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses',
          'https://www.googleapis.com/auth/classroom.coursework.me',
          'https://www.googleapis.com/auth/classroom.coursework.students',
          'https://www.googleapis.com/auth/classroom.rosters',
          'https://www.googleapis.com/auth/classroom.profile.emails',
          'https://www.googleapis.com/auth/spreadsheets.readonly']

# https://www.googleapis.com/auth/classroom.topics
# https://www.googleapis.com/auth/classroom.push-notifications
# https://www.googleapis.com/auth/classroom.announcements


def get_cred():
    """allow access
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    #print(creds.valid, creds.expired)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        #os.environ['OAUTHLIB_STRICT_TOKEN_TYPE'] = "1"
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def get_sheet(creds=None):
    if not creds:
        creds = get_cred()

    SPREADSHEET_ID = "10tKvzNdqESywFUzwIQPYXJ_KM6x93HArBxE2ZJwlPYI"
    RANGE_NAME = 'Form Responses 2'
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    print(values)
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
        for course in courses:
            print(course['id'], course['name'], course['courseState'])

    return courses


def list_course_work(creds=None, course_id="77672504254"):
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    if not creds:
        creds = get_cred()

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    results = service.courses().courseWork().list(courseId=course_id).execute()
    #print(results)
    course_works = results.get('courseWork', [])

    if not course_works:
        print('No course work found.')
    else:
        print('Course Work:')
        for course in course_works:
            print(course['id'], course['title'], course['state'], course['workType'])

    return course_works


def list_student_responses(creds=None, course_id="77672504254",
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
    print(results)
    submissions = results.get('studentSubmissions', [])
    #print(len(submissions))
    if not submissions:
        print('No submissions found.')
    else:
        print('submissions:')
        for submission in submissions:
            print(submission['id'], submission['userId'],
                  submission['state'], submission['courseWorkType'],
                  len(submission['submissionHistory']))

    return submissions


def list_students(creds=None, course_id="77672504254"):
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    if not creds:
        creds = get_cred()

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    results = service.courses().students().list(
        courseId=course_id).execute()
    # print(results)
    submissions = results.get('students', [])
    #print(len(submissions))
    if not submissions:
        print('No student found.')
    else:
        print('students:')
        for submission in submissions:
            print(submission['profile'].get('emailAddress'),
                  submission['profile'].get('name'),
                  submission['userId'])

    return submissions


def add_course():
    creds = get_cred()

    service = build('classroom', 'v1', credentials=creds)
    course = {
        'name': 'High School Algebra',
        'section': 'Period 5',
        'descriptionHeading': 'Welcome to High School Algebra Class',
        'description': """We'll be learning about Mid level algebra 
           from a combination of textbooks, guest lectures, and online material. 
           Expect to be excited!""",
        'room': '301',
        'ownerId': 'me',
        'courseState': 'PROVISIONED'
    }
    course = service.courses().create(body=course).execute()
    print('Course created: {0} ({1})'.format(course.get('name'),
                                             course.get('id')))


if __name__ == '__main__':

    creds = get_cred()

    #list_courses(creds)
    # add_course()
    list_course_work(creds)
    #list_students(creds)

    list_student_responses(creds, coursework_id="71445760543")

    #service = build('classroom', 'v1', credentials=creds)
    #results = service.courses().delete(id='77675617282').execute()

    get_sheet(creds)