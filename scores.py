from utils import get_sorted_responses
from config import get_service_config


def calculate_scores(param):
    service_key = get_service_config(4)
    sortedResponses = get_sorted_responses(param)
    numItems = len (sortedResponses[0])
    scoreList = []

    for i in sortedResponses:
        numRight = sum(i)
        score = numRight / numItems
        score = round(score * 100, 1)
        scoreList.append(score)
        
    return {service_key: scoreList}
