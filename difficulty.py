from utils import get_sorted_responses, get_id_list, get_service_config


def calculate_difficulty(param):
    service_key = get_service_config(3)
    sortedResponses = get_sorted_responses(param)
    numStudents = len(sortedResponses)
    numItems = len (sortedResponses[0])
    idList = get_id_list(param)
    difficultyList = []
    difficultyDict = {}

    for i in range(0, numItems): # For each question i
        numRight = 0
        for k in range(0, numStudents): # For each student k
            studentAnswer = sortedResponses[k][i]
            numRight += studentAnswer
        difficulty = numRight / numStudents
        difficulty = round(difficulty, 3)
        difficultyList.append(difficulty)

    k = 0
    for i in idList:
        difficultyDict[i] = difficultyList[k]
        k += 1
        
    return {service_key: difficultyDict}
