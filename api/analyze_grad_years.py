from common.config import get_service_config, get_keyword_value
from common.utils import sort_students_by_grad_year, get_student_list, get_grad_year_list, update_input, get_error
from api.kr20 import calculate_kr20
from api.idr import calculate_idr, calculate_idr_average
from api.difficulty import calculate_difficulty, calculate_difficulty_average
from api.scores import calculate_scores, calculate_average
from api.weighted_scores import calculate_weighted_scores, calculate_weighted_average
from api.excludes import get_exclude_recos
from api.num_correct import calculate_num_correct
from api.assumptions import get_assumptions
from api.topic_rights import calculate_topic_rights, calculate_topic_averages


def analyze_grad_years(param):
    """
    A function to get an exam's analysis by 
    students' graduation year:
    It groups all students by graduation year and 
    then iterates over the graduation years, calling
    every service used to analyze an exam. 

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a dictionary of nested dictionaries:
             a dictionary with graduation years as
             keys and the exam analysis as values
    """
    service_key = get_service_config(14)
    catch_error = get_error(param)
    if catch_error[0]:
        return {service_key: catch_error[1]}
    inp = update_input(param)
    assumptions_key = get_service_config(13)
    assumptions = get_assumptions(inp)[assumptions_key]
    students_dict = sort_students_by_grad_year(inp)
    grad_year_list = get_grad_year_list(inp)
    grad_analysis = {}

    if grad_year_list == get_keyword_value("no_grad_year"):
        return {service_key: get_keyword_value("no_grad_year")}

    for i in students_dict:
        curr_students = students_dict[i]
        catch_error = get_error(curr_students)
        if catch_error[0]:
            grad_analysis[i] = catch_error[1]
            continue
        student_list = get_student_list(curr_students)

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
        val_topic_rights = calculate_topic_rights(inp)
        val_topic_avgs = calculate_topic_averages(inp)

        curr_assumptions = {}
        for k in assumptions:
            for j in student_list:
                if k == j[get_keyword_value("id")]:
                    curr_assumptions[k] = assumptions[k]
        val_assumptions = {assumptions_key: curr_assumptions}

        result = {}
        items = [val_kr20, val_idr, val_difficulty,
                 val_scores, val_average, val_weighted_s,
                 val_weighted_avg, val_excludes, val_diff_avg,
                 val_idr_avg, val_num_correct, val_assumptions,
                 val_topic_rights, val_topic_avgs]
        for item in items:
            result.update(item)

        grad_analysis[i] = result

    return {service_key: grad_analysis}
