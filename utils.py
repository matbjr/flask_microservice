from statistics import pstdev
from config import get_keyword_value


def get_item_std(item):
    scoreList = []
    for i in item:
        score = sum(i)
        scoreList.append(score)
    # scoreSTD = get_std(scoreList)  # micro service call
    scoreSTD = pstdev(scoreList)

    return scoreSTD


def get_id_list(param):
    student_list = get_student_list(param)
    exclude_list = list(param.get(get_keyword_value("exclude_items"), []))
    idList = []
    responseList = []
    
    for i in student_list:
        responseList.append(i[get_keyword_value("item_responses")])
        
    for i in responseList:
        for k in i:
            curr_id = int(k[get_keyword_value("item_id")])
            if curr_id not in idList and curr_id not in exclude_list:
                idList.append(curr_id)
    
    idList.sort()

    return idList


def get_sorted_responses(param):
    student_list = list(param[get_keyword_value("student_list")])
    numStudents = len(student_list)
    idList = get_id_list(param)
    responseList = []
    responses = {}
    
    for i in student_list:
        responseList.append(i[get_keyword_value("item_responses")])

    for i in idList:  # Create a dictionary with the item IDs as keys
        responses[i] = []
    
    for i in responseList: # For each student response list i
        checklist = idList.copy()
        for k in i: # For each question k
            for j in responses: # For each item ID j
                if k[get_keyword_value("item_id")] == j: # If item IDs match, add response to dictionary
                    responses[j].append(k[get_keyword_value("response")])
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


def get_grad_year_list(param):
    student_list = get_student_list(param)
    grad_year_list = []
        
    for i in student_list:
        curr_grad_year = i.get(get_keyword_value("grad_year"))
        if curr_grad_year != None:
            if curr_grad_year not in grad_year_list:
                grad_year_list.append(curr_grad_year)
    
    grad_year_list.sort()

    return grad_year_list


def sort_students_by_grad_year(param):
    student_list = list(param[get_keyword_value("student_list")])
    grad_year_list = get_grad_year_list(param)
    id_list = get_id_list(param)
    responses_by_grad_year = {}

    for i in grad_year_list:
        responses_by_grad_year[i] = {(get_keyword_value("student_list")): []}

    for i in grad_year_list:
        for k in range(0, len(student_list)): 
            curr_item_ids = []
            curr_responses = student_list[k][get_keyword_value("item_responses")]
            for j in curr_responses:
                curr_item_ids.append(j[get_keyword_value("item_id")])
            for j in id_list:
                if j not in curr_item_ids:
                    student_list[k][get_keyword_value("item_responses")].append({get_keyword_value("item_id"): j, get_keyword_value("response"): 0})
            if student_list[k][get_keyword_value("grad_year")] == i:
                responses_by_grad_year[i][get_keyword_value("student_list")].append(student_list[k])

    return responses_by_grad_year


def get_student_list(param):
    student_list = list(param[get_keyword_value("student_list")])
    exclude_students = list(param.get(get_keyword_value("exclude_students"), []))
    
    for i in student_list:
        if int(i[get_keyword_value("id")]) in exclude_students:
            student_list.remove(i)

    return student_list


def update_input(param):
    inp = param
    student_list = list(param[get_keyword_value("student_list")])

    for i in range(0, len(student_list)):
        curr_stud = student_list[i].get(get_keyword_value("id"))
        if curr_stud == None:
            student_list[i][(get_keyword_value("id"))] = i+1

    for i in range(0, len(student_list)):
        curr_responses = student_list[i][get_keyword_value("item_responses")]
        for k in range(0, len(curr_responses)):
            curr_item = curr_responses[k].get(get_keyword_value("item_id"))
            if curr_item == None:
                student_list[i][get_keyword_value("item_responses")][k][get_keyword_value("item_id")] = k+1

    inp[get_keyword_value("student_list")] = student_list
    return inp
