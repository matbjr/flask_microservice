from difficulty import calculate_difficulty
from config import get_service_config


def calculate_difficulty_average(param):
    service_key = get_service_config(10)
    diff_list = list(list(calculate_difficulty(param).values())[0].values())
    num_items = len(diff_list)
    diff_avg = sum(diff_list) / num_items
        
    return {service_key: round(diff_avg, 3)}
