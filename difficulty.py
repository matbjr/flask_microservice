def get_list(item, index):
<<<<<<< Updated upstream

    return list(item[index].values())[0]
=======
    ir = item[index]['itemresponses']
    irList = [int(i) for i in ir.split(',')]
    return irList
>>>>>>> Stashed changes


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
