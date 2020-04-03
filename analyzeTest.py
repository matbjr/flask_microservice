from kr20 import calculate_kr20
from pbcc import calculate_pbcc
from difficulty import calculate_difficulty
from scores import calculate_scores
from average import calculate_average


def get_list(item, index):
    return list(item[index]['itemresponses'])


def analyze_test(param):
    student_list = list(param['studentList'])
    responseList = get_list(student_list, 0)
    numStudents = len(student_list)
    numItems = len(responseList)
    idList = []
    responses = {}

    for i in range(0, numStudents): # Check if item count is consistent
        if numItems != len(get_list(student_list, i)):
            return {'Error': 'All students\' item count must be the same'}

    for i in range(0, numItems): # Put all item IDs into a list
        idList.append(responseList[i]['itemid'])
    idList.sort()

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

    # Call microservices:
    valKR20 = calculate_kr20(sortedResponses, numStudents, numItems)
    valPBCC = calculate_pbcc(sortedResponses, numStudents, numItems)
    valDifficulty = calculate_difficulty(sortedResponses, numStudents, numItems)
    valScores = calculate_scores(sortedResponses, numStudents, numItems)
    valAvg = calculate_average(sortedResponses, numStudents, numItems)

    analysis = (valKR20, valPBCC, valDifficulty, valScores, valAvg)

    return {'analysis': analysis}
    # TO DO: store pbcc and difficulty by item id (pass id list as parameter?)