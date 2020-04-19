from api.utils import get_sorted_responses, update_input, get_student_ids
from api.config import get_service_config, get_keyword_value


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
