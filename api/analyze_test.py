from api.config import get_service_config
from api.utils import update_input
from api.kr20 import calculate_kr20
from api.idr import calculate_idr
from api.difficulty import calculate_difficulty
from api.scores import calculate_scores
from api.average import calculate_average
from api.weighted_scores import calculate_weighted_scores
from api.weighted_average import calculate_weighted_average
from api.excludes import get_exclude_recos
from api.difficulty_average import calculate_difficulty_average
from api.idr_average import calculate_idr_average
from api.num_correct import calculate_num_correct
from api.assumptions import get_assumptions
from api.analyze_grad_years import analyze_grad_years


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


if __name__ == '__main__':
    from api.sample import sample, sample_result, sample_result2
    import json

    analysis = analyze_test(sample)
    print(json.dumps(analysis))

    sample["exclude_items"] = [2, 6, 9, 12, 15, 16, 17, 18]

    analysis = analyze_test(sample)

    print(json.dumps(analysis))
    