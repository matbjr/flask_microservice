from utils import get_sorted_responses, get_id_list, get_student_list
from config import get_service_config, get_keyword_value


def calculate_num_correct(param):
    service_key = get_service_config(12)
    student_list = {get_keyword_value("student_list"): get_student_list(param)}
    sortedResponses = get_sorted_responses(student_list)
    numStudents = len(sortedResponses)
    numItems = len (sortedResponses[0])
    idList = get_id_list(param)
    num_correct_list = []
    num_correct_dict = {}

    for i in range(0, numItems): # For each question i
        numRight = 0
        for k in range(0, numStudents): # For each student k
            studentAnswer = sortedResponses[k][i]
            numRight += studentAnswer
        num_correct_list.append(numRight)

    k = 0
    for i in idList:
        num_correct_dict[i] = num_correct_list[k]
        k += 1
        
    return {service_key: num_correct_dict}
