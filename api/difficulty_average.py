from api.difficulty import calculate_difficulty
from api.config import get_service_config
from api.utils import update_input


def calculate_difficulty_average(param):
    service_key = get_service_config(10)
    inp = update_input(param)
    diff_list = list(list(calculate_difficulty(inp).values())[0].values())
    num_items = len(diff_list)
    diff_avg = sum(diff_list) / num_items
        
    return {service_key: round(diff_avg, 3)}
