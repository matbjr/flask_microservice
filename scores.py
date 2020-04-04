from utils import get_item_std
from utils import get_sorted_responses

def calculate_scores(param):
    sortedResponses = get_sorted_responses(param)
    numStudents = len(sortedResponses)
    numItems = len (sortedResponses[0])
    scoreList = []

    for i in range(0, numStudents):
        numRight = sum(sortedResponses[i])
        score = numRight / numItems
        score = round(score, 3)
        scoreList.append(score)
        
    return {'scores': scoreList}