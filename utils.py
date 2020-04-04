from statistics import pstdev
from api_client import get_std


def get_item_std(item, numStudents):
    scoreList = []
    for i in range(0, numStudents):
        score = sum(item[i])
        scoreList.append(score)
    # scoreSTD = get_std(scoreList)  # micro service call
    scoreSTD = pstdev(scoreList)

    return scoreSTD

def get_list(item, index):
    
    return list(item[index].values())[0]


def get_list(item, index):
    return list(item[index]['itemresponses'])


def get_id_list(param):
    student_list = list(param['studentList'])
    responseList = get_list(student_list, 0)
    numItems = len(responseList)
    idList = []

    for i in range(0, numItems): # Put all item IDs into a list
        idList.append(responseList[i]['itemid'])
    idList.sort()

    return idList


def get_sorted_responses(param):
    student_list = list(param['studentList'])
    responseList = get_list(student_list, 0)
    numStudents = len(student_list)
    numItems = len(responseList)
    responses = {}

    for i in range(0, numStudents): # Check if item count is consistent
        if numItems != len(get_list(student_list, i)):
            return {'Error': 'All students\' item count must be the same'}

    idList = get_id_list(param)

    for i in idList: # Create a dictionary with the item IDs as keys
        responses[i] = []
    
    for i in range(0, numStudents): # For each student i
        for k in range(0, numItems): # For each question k
            for j in responses: # For each item ID j
                if get_list(student_list, i)[k]['itemid'] == j: # If item IDs match, add response to dictionary
                    responses[j].append(get_list(student_list, i)[k]['response'])

    sortedResponses = []
    for i in range(0, numStudents): # For each student
        studentResponses = []
        for k in responses: # For every item ID
            studentResponses.append(responses[k][i]) # Create a list of the students responses sorted by item ID
        sortedResponses.append(studentResponses)

    return sortedResponses


# JSON object for literals and constants
# will be hosted in some cloud storage
# all keys are lower case, Use underscore for longer keys
config = {
    'cloud_host': 'xxx',
    'cloud_host_credentials':'yyyy',
    'application_id': 'rm_01',
    'application_version': '0.0.1',
    'application_name': 'Reliability Measures microservices',
    'application_short_name': 'rm_microservices',
}

# more to follow
