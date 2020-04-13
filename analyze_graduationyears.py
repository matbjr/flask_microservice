from config import get_service_config, get_keyword_value
from utils import sort_students_by_grad_year
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

def analyze_gradyears(param):
    service_key = get_service_config(14)
    assumptions_key = get_service_config(13)
    assumptions = get_assumptions(param)[assumptions_key]
    students_dict = sort_students_by_grad_year(param)
    grad_analysis = {}

    for i in students_dict:
        curr_students = students_dict[i]
        student_list = curr_students[get_keyword_value('student_list')]
        if len(student_list) <= 1:
            grad_analysis[i] = get_keyword_value('bad_data')
            continue

        val_kr20 = calculate_kr20(curr_students)
        val_idr = calculate_idr(curr_students)
        val_difficulty = calculate_difficulty(curr_students)
        val_scores = calculate_scores(curr_students)
        val_average = calculate_average(curr_students)
        val_weighted_s = calculate_weighted_scores(curr_students)
        val_weighted_avg = calculate_weighted_average(curr_students)
        val_excludes = get_exclude_recos(curr_students)
        val_diff_avg = calculate_difficulty_average(curr_students)
        val_idr_avg = calculate_idr_average(curr_students)
        val_num_correct = calculate_num_correct(curr_students)

        curr_assumptions = dict()
        for k in assumptions:
            for j in student_list:
                if k == j[get_keyword_value('id')]:
                    curr_assumptions[k] = assumptions[k]
        val_assumptions = {assumptions_key: curr_assumptions}

        result = dict()
        items = [val_kr20, val_idr, val_difficulty,
                 val_scores, val_average, val_weighted_s,
                 val_weighted_avg, val_excludes, val_diff_avg,
                 val_idr_avg, val_num_correct, val_assumptions]
        for item in items:
            result.update(item)

        grad_analysis[i] = result

    return {service_key: grad_analysis}
