def calculate_scores(param, numStudents, numItems):
    sortedResponses = param
    scoreList = []

    for i in range(0, numStudents):
        numRight = sum(sortedResponses[i])
        score = numRight / numItems
        score = round(score, 3)
        scoreList.append(score)
        
    return {'scores': scoreList}