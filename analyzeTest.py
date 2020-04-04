from kr20 import calculate_kr20
from pbcc import calculate_pbcc
from difficulty import calculate_difficulty
from scores import calculate_scores
from average import calculate_average


def analyze_test(param):
    # use microservice calls here when all are hosted
    valKR20 = calculate_kr20(param)
    valPBCC = calculate_pbcc(param)
    valDifficulty = calculate_difficulty(param)
    valScores = calculate_scores(param)
    valAverage = calculate_average(param)

    return {'analysis': (valKR20, valPBCC, valDifficulty, valScores, valAverage)}