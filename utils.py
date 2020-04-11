from statistics import pstdev
from config import get_keyword_value


def get_item_std(item, numStudents):
    scoreList = []
    for i in range(0, numStudents):
        score = sum(item[i])
        scoreList.append(score)
    # scoreSTD = get_std(scoreList)  # micro service call
    scoreSTD = pstdev(scoreList)

    return scoreSTD


def get_id_list(param):
    student_list = list(param[get_keyword_value('student_list')])
    exclude_list = list(param[get_keyword_value('exclude_items')])
    idList = []
    responseList = []
    
    for i in student_list:
        responseList.append(i[get_keyword_value('item_responses')])
        
    for i in responseList:
        for k in i:
            curr_id = k[get_keyword_value('item_id')]
            if curr_id not in idList and curr_id not in exclude_list:
                idList.append(curr_id)
    
    idList.sort()

    return idList


def get_sorted_responses(param):
    student_list = list(param[get_keyword_value('student_list')])
    numStudents = len(student_list)
    idList = get_id_list(param)
    responseList = []
    responses = {}
    
    for i in student_list:
        responseList.append(i[get_keyword_value('item_responses')])

    for i in idList:  # Create a dictionary with the item IDs as keys
        responses[i] = []
    
    for i in responseList: # For each student response list i
        checklist = idList.copy()
        for k in i: # For each question k
            for j in responses: # For each item ID j
                if k[get_keyword_value('item_id')] == j: # If item IDs match, add response to dictionary
                    responses[j].append(k[get_keyword_value('response')])
                    checklist.remove(j)

        if len(checklist) != 0:
            for i in checklist:
                responses[i].append(0)

    sortedResponses = []
    for i in range(0, numStudents): # For each student
        studentResponses = []
        for k in responses: # For every item ID
            studentResponses.append(responses[k][i]) # Create a list of the students responses sorted by item ID
        sortedResponses.append(studentResponses)

    return sortedResponses



