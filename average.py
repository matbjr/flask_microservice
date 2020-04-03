from scores import calculate_scores


def calculate_average(param, numStudents, numItems):
    scoreList = list(calculate_scores(param, numStudents, numItems).values())[0]
    average = sum(scoreList) / numStudents
        
    return {'average': average}
