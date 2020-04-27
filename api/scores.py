from common.utils import get_sorted_responses, update_input, get_student_ids
from common.config import get_service_config, get_keyword_value


def calculate_scores(param):
    """
    A function to get the score of each student:
    For each student, it gets the number of correct
    responses and divides it by the number of questions.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a dictionary of floats: a dictionary with
             student ids as keys and their score as values
    """
    service_key = get_service_config(4)
    inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return {service_key: get_keyword_value("no_students")}
    sorted_resp = get_sorted_responses(inp)
    student_ids = get_student_ids(inp) 
    num_items = len (sorted_resp[0])
    score_dict = {}

    for curr_id in student_ids:
        score_dict[curr_id] = None

    k = 0
    for i in score_dict:
        num_right = sum(sorted_resp[k])
        score = num_right / num_items
        score = round(score * 100, 1)
        score_dict[i] = score
        k += 1

    return {service_key: score_dict}

def calculate_average(param):
    """
    A function to get the average score of
    the students:
    It gets every students score and then
    calculates the average of those scores.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a float: the score average
    """
    service_key = get_service_config(5)
    inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return {service_key: get_keyword_value("no_students")}
    score_list = list(list(calculate_scores(inp).values())[0].values())
    num_students = len(score_list)
    average = sum(score_list) / num_students
        
    return {service_key: round(average, 1)}
