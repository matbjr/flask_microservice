from api.difficulty import calculate_difficulty
from api.config import get_service_config
from api.utils import update_input


def calculate_difficulty_average(param):
    """
    A function to get the average difficulty
    of items on the exam:
    It gets the difficulty of every item and then 
    calculates the average of those difficulties.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a float: the difficulty average
    """
    service_key = get_service_config(10)
    inp = update_input(param)
    diff_list = list(list(calculate_difficulty(inp).values())[0].values())
    num_items = len(diff_list)
    diff_avg = sum(diff_list) / num_items
        
    return {service_key: round(diff_avg, 3)}
