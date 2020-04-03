# import numpy as np
from statistics import mean
from statistics import pstdev
from math import sqrt
# from utils import get_list

# Having issues using imported get_list from utils.py
def get_list(item, index):
    return list(item[index]['itemresponses'])


def calculate_pbcc(param):
    student_list = list(param['studentList'])
    responseList = get_list(student_list,0)
    numStudents = len(student_list)
    numItems = len(responseList)
    idList = []
    responses = {}
    scoreList = []
    pbccList = []

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

    for i in range(0, numStudents): # Check if item count is consistent
        if numItems != len(sortedResponses[i]):
            return {'Error': 'All students\' item count must be the same'}

    for i in range(0, numStudents): # Get standard deviation of scores
        score = sum(sortedResponses[i])
        scoreList.append(score)
    scoreSTD = pstdev(scoreList)

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

        # rightMean = wrongMean = None <-- Causing errors
        if len(rightList) == 1:
            rightMean = rightList[0]
        elif len(rightList) > 1:
            rightMean = mean(rightList)
        if len(wrongList) == 1:
            wrongMean = wrongList[0]
        elif len(wrongList) > 1:
            wrongMean = mean(wrongList)
        if not rightMean or not wrongMean:
            return {'pbcc': 'Invalid Data - No mean'}

        pbcc = ((rightMean - wrongMean) * sqrt(numRight * numWrong)) / numStudents * scoreSTD
        pbcc = round(pbcc, 3)
        pbccList.append(pbcc)

    k = 0
    for i in idList:
        responses[i] = pbccList[k]
        k += 1
        
    return {'pbcc': responses}
