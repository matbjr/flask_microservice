def get_list(item, index):

    return list(item[index].values())[0]


def calculate_difficulty(param):
    student_list = list(param['students'])
    numStudents = len(student_list)
    numQ = len(get_list(student_list, 0))
    difficultyList = []

    for i in range(0, numQ): # For each question i
        numRight = 0
        for k in range(0, numStudents): # For each student k
            if get_list(student_list, k)[i] == 1: # If student k gets question i correct
                numRight += 1
        difficulty = numRight / numStudents
        difficulty = round(difficulty, 3)
        difficultyList.append(difficulty)
        
    return {'difficulty': difficultyList}
