from statistics import mean
from math import sqrt

from utils import get_item_std, get_sorted_responses, get_id_list
from config import get_service_config, get_keyword_value


def calculate_idr(param):
    service_key = get_service_config(2)
    sortedResponses = get_sorted_responses(param)
    numStudents = len(sortedResponses)
    numItems = len (sortedResponses[0])
    idList = get_id_list(param)
    scoreSTD = get_item_std(sortedResponses)
    idrList = []
    idrDict = {}

    if scoreSTD <=0:
        return {service_key: get_keyword_value('bad_std')}

    for i in range(0, numItems): # For each question i
        rightList = [] # Scores of students who got question i right
        wrongList = [] # Scores of students who got question i wrong
        numRight = 0 # Total number of students who got question i right
        numWrong = 0 # Total number of students who got question i wrong
        for k in range(0, numStudents): # For each student k
            if sortedResponses[k][i] == 1: # If student k gets question i correct
                score = sum(sortedResponses[k]) / numItems
                rightList.append(score) # Then add their score to the "right" list
                numRight += 1
            elif sortedResponses[k][i] == 0: # If student k gets question i wrong 
                score = sum(sortedResponses[k]) / numItems
                wrongList.append(score) # Then add their score to the "wrong" list
                numWrong += 1

        if len(rightList) == 1:
            rightMean = rightList[0]
        elif len(rightList) > 1:
            rightMean = mean(rightList)
        if len(wrongList) == 1:
            wrongMean = wrongList[0]
        elif len(wrongList) > 1:
            wrongMean = mean(wrongList)
        if not rightMean or not wrongMean:
            return {service_key: get_keyword_value('bad_mean')}

        idr = ((rightMean - wrongMean) * sqrt(numRight * numWrong)) / numStudents * scoreSTD
        idr = round(idr, 3)
        idrList.append(idr)
    
    k = 0
    for i in idList:
        idrDict[i] = idrList[k]
        k += 1

    return {service_key: idrDict}
