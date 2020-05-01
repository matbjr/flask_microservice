from common.utils import get_sorted_responses, update_input, get_student_ids, get_error, get_scoring_method
from common.config import get_service_config, get_keyword_value


def calculate_scores(param):
    """
    A function to get the score of each student:
    For each student, it gets the number of correct
    responses and divides it by the number of questions.

    :param: a json in the Reliability Measures
            standard json format
    :return: a dictionary of floats: a dictionary with
             student ids as keys and their score as values
    """
    service_key = get_service_config(4)
    catch_error = get_error(param)
    if catch_error[0]:
        return {service_key: catch_error[1]}
    inp = update_input(param)
    sorted_resp = get_sorted_responses(inp)
    student_ids = get_student_ids(inp) 
    scoring_method = get_scoring_method(inp)
    num_items = len (sorted_resp[0])
    score_dict = {}

    for curr_id in student_ids:
        score_dict[curr_id] = None

    k = 0
    for i in score_dict:
        num_right = sum(sorted_resp[k])
        score = num_right / num_items
        if scoring_method[0] == get_keyword_value("percentage"):
            score = round(score * 100, 3)
        elif scoring_method[0] == get_keyword_value("absolute"):
            score = round(score * num_items, 3)
        elif scoring_method[0] == get_keyword_value("scaled"):
            score = round(score * scoring_method[1], 3)
        else:
            score = round(score, 3)
        score_dict[i] = score
        k += 1

    return {service_key: score_dict}

def calculate_average(param):
    """
    A function to get the average score of
    the students:
    It gets every students score and then
    calculates the average of those scores.

    :param: a json in the Reliability Measures
            standard json format
    :return: a float: the score average
    """
    service_key = get_service_config(5)
    catch_error = get_error(param)
    if catch_error[0]:
        return {service_key: catch_error[1]}
    inp = update_input(param)
    score_list = list(list(calculate_scores(inp).values())[0].values())
    num_students = len(score_list)

    average = sum(score_list) / num_students
    average = round(average, 3)
        
    return {service_key: average}
