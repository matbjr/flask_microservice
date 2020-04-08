from kr20 import calculate_kr20
from idr import calculate_idr
from difficulty import calculate_difficulty
from scores import calculate_scores
from average import calculate_average
from utils import get_service_config
from weighted_scores import calculate_weighted_scores
from weighted_average import calculate_weighted_average
from excludes import get_exclude_recos
from difficulty_average import calculate_difficulty_average
from idr_average import calculate_idr_average


def analyze_test(param):
    service_key = get_service_config(6)
    # use microservice calls here when all are hosted
    val_kr20 = calculate_kr20(param)
    val_idr = calculate_idr(param)
    val_difficulty = calculate_difficulty(param)
    val_scores = calculate_scores(param)
    val_average = calculate_average(param)
    val_weighted_s = calculate_weighted_scores(param)
    val_weighted_avg = calculate_weighted_average(param)
    val_excludes = get_exclude_recos(param)
    val_diff_avg = calculate_difficulty_average(param)
    val_idr_avg = calculate_idr_average(param)

    # join all results
    result = dict()
    items = [val_kr20, val_idr, val_difficulty,
             val_scores, val_average, val_weighted_s,
             val_weighted_avg, val_excludes, val_diff_avg,
             val_idr_avg]
    for item in items:
        result.update(item)

    return {service_key: result}

