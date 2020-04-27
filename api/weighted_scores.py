from common.config import get_service_config
from common.utils import get_sorted_responses, update_input, get_student_ids
from api.difficulty import calculate_difficulty


def calculate_weighted_scores(param):
    """
    A function to get the weighted score of each student:
    For each student, it gets the weight of every item
    they got correct by getting its difficulty and dividing
    it by the sum of all items' difficulties.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a dictionary of floats: a dictionary with
             student ids as keys and their weighted score 
             as values
    """
    service_key = get_service_config(7)
    inp = update_input(param)
    student_ids = get_student_ids(inp)
    sorted_resp = get_sorted_responses(inp)
    num_items = len(sorted_resp[0])
    difficulty_list = list(list(calculate_difficulty(inp).values())[0].values())
    difficulty_sum = sum(difficulty_list)
    weighted_scores_dict = {}

    for curr_id in student_ids:
        weighted_scores_dict[curr_id] = None

    j = 0
    for i in weighted_scores_dict:
        weighted = 0
        for k in range(0, num_items):
            if sorted_resp[j][k] == 1:
                weighted += difficulty_list[k]
        weighted /= difficulty_sum
        weighted = round(weighted * 100, 1)
        weighted_scores_dict[i] = weighted
        j += 1
        
    return {service_key: weighted_scores_dict}

def calculate_weighted_average(param):
    """
    A function to get the weighted average 
    score of the students:
    It gets every students weighted score and 
    then calculates the average of those scores.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a float: the weighted score average
    """
    service_key = get_service_config(8)
    inp = update_input(param)
    weighted_scores = list(list(calculate_weighted_scores(inp).values())[0].values())
    num_students = len(weighted_scores)
    weighted_average = sum(weighted_scores) / num_students
        
    return {service_key: round(weighted_average, 1)}
