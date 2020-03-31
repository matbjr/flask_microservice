# import numpy as np
from statistics import pstdev

from api_client import get_std
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes


def get_list(item, index):
    ir = item[index]['itemresponses']
    irList = [int(i) for i in ir.split(',')]
    return irList


def calculate_kr20(param):
    student_list = list(param['students'])
    numStudents = len(student_list)
    numQ = len(get_list(student_list, 0))
    pqList = []
    scoreList = []

    for k in range(0, numStudents):
        if numQ != len(get_list(student_list, k)):
            return {'KR20': 'All students\' item count must be the same'}

    for i in range(0, numQ):
        p = 0
        for k in range(0, numStudents):
            p += get_list(student_list, k)[i]
        p /= numStudents
        q = 1 - p
        pqList.append(p * q)
    pqSum = sum(pqList)

    for k in range(0, numStudents):
        score = sum(get_list(student_list, k))
        scoreList.append(score)

    # scoreSTD = get_std(scoreList)  # micro service call
    scoreSTD = pstdev(scoreList)

    if scoreSTD <=0:
        return {'KR20': 'Invalid data - No Std. Dev.'}

    # need validation here
    kr20_value = (numQ /(numQ - 1)) * (1 - (pqSum / (scoreSTD ** 2)))

    return {'KR20': round(kr20_value, 3)}
