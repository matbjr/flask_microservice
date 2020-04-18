from api.scores import calculate_scores
from api.config import get_service_config
from api.utils import update_input


def calculate_average(param):
    service_key = get_service_config(5)
    inp = update_input(param)
    score_list = list(list(calculate_scores(inp).values())[0].values())
    num_students = len(score_list)
    average = sum(score_list) / num_students
        
    return {service_key: round(average, 1)}
