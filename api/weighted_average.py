from api.weighted_scores import calculate_weighted_scores
from api.config import get_service_config
from api.utils import update_input


def calculate_weighted_average(param):
    service_key = get_service_config(8)
    inp = update_input(param)
    weighted_scores = list(list(calculate_weighted_scores(inp).values())[0].values())
    numStudents = len(weighted_scores)
    weighted_average = sum(weighted_scores) / numStudents
        
    return {service_key: round(weighted_average, 1)}
