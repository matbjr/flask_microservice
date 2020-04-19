from api.weighted_scores import calculate_weighted_scores
from api.config import get_service_config
from api.utils import update_input


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
