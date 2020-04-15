from config import get_service_config
from utils import update_input
from kr20 import calculate_kr20
from idr import calculate_idr
from difficulty import calculate_difficulty
from scores import calculate_scores
from average import calculate_average
from weighted_scores import calculate_weighted_scores
from weighted_average import calculate_weighted_average
from excludes import get_exclude_recos
from difficulty_average import calculate_difficulty_average
from idr_average import calculate_idr_average
from num_correct import calculate_num_correct
from assumptions import get_assumptions
from analyze_grad_years import analyze_grad_years


def analyze_test(param):
    service_key = get_service_config(6)
    inp = update_input(param)
    # use microservice calls here when all are hosted
    val_kr20 = calculate_kr20(inp)
    val_idr = calculate_idr(inp)
    val_difficulty = calculate_difficulty(inp)
    val_scores = calculate_scores(inp)
    val_average = calculate_average(inp)
    val_weighted_s = calculate_weighted_scores(inp)
    val_weighted_avg = calculate_weighted_average(inp)
    val_excludes = get_exclude_recos(inp)
    val_diff_avg = calculate_difficulty_average(inp)
    val_idr_avg = calculate_idr_average(inp)
    val_num_correct = calculate_num_correct(inp)
    val_assumptions = get_assumptions(inp)
    val_grad_year_analysis = analyze_grad_years(inp)

    # join all results
    result = dict()
    items = [val_kr20, val_idr, val_difficulty,
             val_scores, val_average, val_weighted_s,
             val_weighted_avg, val_excludes, val_diff_avg,
             val_idr_avg, val_num_correct, val_assumptions,
             val_grad_year_analysis]
    for item in items:
        result.update(item)

    return {service_key: result}
