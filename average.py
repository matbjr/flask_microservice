from scores import calculate_scores
from config import get_service_config
from utils import update_input


def calculate_average(param):
    service_key = get_service_config(5)
    inp = update_input(param)
    scoreList = list(list(calculate_scores(inp).values())[0].values())
    numStudents = len(scoreList)
    average = sum(scoreList) / numStudents
        
    return {service_key: round(average, 1)}
