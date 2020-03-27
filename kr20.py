import numpy as np 


def get_list(item, index):

    return list(item[index].values())[0]


def calculate_kr20(param):
    student_list = list(param['students'])
    numStudents = len(student_list)
    numQ = len(get_list(student_list, 0))
    pqList = []
    scoreList = []

    for k in range(0, numStudents):
        if numQ != len(get_list(student_list, k)):
            return {'Error': 'All student\'s item count must be the same'}

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

    scoreSTD = np.std(scoreList)
    kr20_value = (numQ /(numQ - 1)) * (1 - (pqSum / (scoreSTD ** 2)))

    return {'KR20': round(kr20_value, 3)}
