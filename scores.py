from utils import get_list


def calculate_scores(param):
    student_list = list(param['students'])
    numStudents = len(student_list)
    numQ = len(get_list(student_list, 0))
    scoreList = []

    for i in range(0, numStudents): # For each student i
        numRight = 0
        for k in range(0, numQ): # For each question k
            studentAnswer = get_list(student_list, i)[k]
            numRight += studentAnswer
        score = numRight / numQ
        score = round(score, 3)
        scoreList.append(score)
        
    return {'scores': scoreList}
