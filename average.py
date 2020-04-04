from scores import calculate_scores


def calculate_average(param):
    scoreList = list(calculate_scores(param).values())[0]
    numStudents = len(scoreList)
    average = sum(scoreList) / numStudents
        
    return {'average': average}