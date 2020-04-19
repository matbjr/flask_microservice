from api.scores import calculate_scores
from api.config import get_service_config
from api.utils import update_input


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
    score_list = list(list(calculate_scores(inp).values())[0].values())
    num_students = len(score_list)
    average = sum(score_list) / num_students
        
    return {service_key: round(average, 1)}
