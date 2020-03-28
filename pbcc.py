# import numpy as np
from statistics import mean
from statistics import pstdev
from statistics import sqrt


def get_list(item, index):
    return list(item[index].values())[0]


def calculate_pbcc(param):
    student_list = list(param['students'])
    numStudents = len(student_list)
    numQ = len(get_list(student_list, 0))
    scoreList = []
    pbccList = []

    for i in range(0, numStudents): # Check if item count is consistent
        if numQ != len(get_list(student_list, i)):
            return {'Error': 'All students\' item count must be the same'}

    for i in range(0, numStudents): # Get standard deviation of scores
        score = sum(get_list(student_list, i))
        scoreList.append(score)
    scoreSTD = pstdev(scoreList)

    for i in range(0, numQ): # For each question i
        rightList = [] # Scores of students who got question i right
        wrongList = [] # Scores of students who got question i wrong
        numRight = 0 # Total number of students who got question i right
        numWrong = 0 # Total number of students who got question i wrong
        for k in range(0, numStudents): # For each student k
            if get_list(student_list, k)[i] == 1: # If student k gets question i correct
                score = sum(get_list(student_list, k))
                rightList.append(score) # Then add their score to the "right" list
                numRight += 1
            elif get_list(student_list, k)[i] == 0: # If student k gets question i wrong 
                score = sum(get_list(student_list, k))
                wrongList.append(score) # Then add their score to the "wrong" list
                numWrong += 1 
        rightMean = mean(rightList)
        wrongMean = mean(wrongList)
        pbcc = ((rightMean - wrongMean) * sqrt(numRight * numWrong)) / numStudents * scoreSTD
        pbcc = round(pbcc, 3)
        pbccList.append(pbcc)
        
    return {'pbcc': pbccList}
