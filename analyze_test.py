from kr20 import calculate_kr20
from pbcc import calculate_pbcc
from difficulty import calculate_difficulty
from scores import calculate_scores
from average import calculate_average
from utils import get_service_config
from weighted_scores import calculate_weighted_scores
from weighted_average import calculate_weighted_average
from excludes import get_excludes


def analyze_test_scores(param):
    service_key = get_service_config(6)
    # use microservice calls here when all are hosted
    valKR20 = calculate_kr20(param)
    valPBCC = calculate_pbcc(param)
    valDifficulty = calculate_difficulty(param)
    valScores = calculate_scores(param)
    valAverage = calculate_average(param)
    valWeightedS = calculate_weighted_scores(param)
    valWeightedAvg = calculate_weighted_average(param)
    valExcludes = get_excludes(param)

    # list of all results
    return {service_key: [valKR20, valPBCC, valDifficulty,
                          valScores, valAverage, valWeightedS,
                          valWeightedAvg, valExcludes]
           }
