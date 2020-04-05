from utils import get_sorted_responses,  get_service_config


def calculate_scores(param):
    service_key = get_service_config(4)
    sortedResponses = get_sorted_responses(param)
    numStudents = len(sortedResponses)
    numItems = len (sortedResponses[0])
    scoreList = []

    for i in range(0, numStudents):
        numRight = sum(sortedResponses[i])
        score = numRight / numItems
        score = round(score, 3)
        scoreList.append(score)
        
    return {service_key: scoreList}
