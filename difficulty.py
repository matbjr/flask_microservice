def calculate_difficulty(param, numStudents, numItems):
    sortedResponses = param
    difficultyList = []

    for i in range(0, numItems): # For each question i
        numRight = 0
        for k in range(0, numStudents): # For each student k
            studentAnswer = sortedResponses[k][i]
            numRight += studentAnswer
        difficulty = numRight / numStudents
        difficulty = round(difficulty, 3)
        difficultyList.append(difficulty)
        
    return {'difficulty': difficultyList}