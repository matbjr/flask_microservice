from utils import get_sorted_responses, get_id_list, get_student_list, update_input
from config import get_service_config, get_keyword_value


def calculate_difficulty(param):
    service_key = get_service_config(3)
    inp = update_input(param)
    student_list = {get_keyword_value("student_list"): get_student_list(inp)}
    sortedResponses = get_sorted_responses(student_list)
    numStudents = len(sortedResponses)
    numItems = len (sortedResponses[0])
    idList = get_id_list(inp)
    difficultyList = []
    difficultyDict = {}

    for i in range(0, numItems): # For each question i
        numRight = 0
        for k in range(0, numStudents): # For each student k
            studentAnswer = sortedResponses[k][i]
            numRight += studentAnswer
        difficulty = 1 - numRight / numStudents
        difficulty = round(difficulty, 3)
        difficultyList.append(difficulty)

    k = 0
    for i in idList:
        difficultyDict[i] = difficultyList[k]
        k += 1
        
    return {service_key: difficultyDict}
