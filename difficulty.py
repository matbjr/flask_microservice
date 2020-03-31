from utils import get_list


def calculate_difficulty(param):
    student_list = list(param['students'])
    numStudents = len(student_list)
    numQ = len(get_list(student_list, 0))
    difficultyList = []

    for i in range(0, numQ): # For each question i
        numRight = 0
        for k in range(0, numStudents): # For each student k
            studentAnswer = get_list(student_list, k)[i]
            numRight += studentAnswer
        difficulty = numRight / numStudents
        difficulty = round(difficulty, 3)
        difficultyList.append(difficulty)
        
    return {'difficulty': difficultyList}
