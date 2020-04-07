from utils import get_sorted_responses,  get_service_config
from difficulty import calculate_difficulty


def calculate_weighted_scores(param):
    service_key = get_service_config(7)
    sortedResponses = get_sorted_responses(param)
    numStudents = len(sortedResponses)
    numItems = len (sortedResponses[0])
    difficulty_list = list(list(calculate_difficulty(param).values())[0].values())
    difficulty_sum = sum(difficulty_list)
    weighted_scores = []

    for i in range(0, numStudents):
        weighted = 0
        for k in range(0, numItems):
            if sortedResponses[i][k] == 1:
                weighted += difficulty_list[k]
        weighted /= difficulty_sum
        weighted = round(weighted * 100, 1)
        weighted_scores.append(weighted)
        
    return {service_key: weighted_scores}
