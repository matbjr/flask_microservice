from config import get_service_config, get_keyword_value
from utils import get_sorted_responses, get_student_list, update_input
from difficulty import calculate_difficulty


def calculate_weighted_scores(param):
    service_key = get_service_config(7)
    inp = update_input(param)
    student_list = get_student_list(inp)
    sortedResponses = get_sorted_responses(inp)
    numItems = len (sortedResponses[0])
    difficulty_list = list(list(calculate_difficulty(inp).values())[0].values())
    difficulty_sum = sum(difficulty_list)
    weighted_scores_dict = {}

    for i in student_list:
        stud_id = i[get_keyword_value('id')]
        weighted_scores_dict[stud_id] = None

    j = 0
    for i in weighted_scores_dict:
        weighted = 0
        for k in range(0, numItems):
            if sortedResponses[j][k] == 1:
                weighted += difficulty_list[k]
        weighted /= difficulty_sum
        weighted = round(weighted * 100, 1)
        weighted_scores_dict[i] = weighted
        j += 1
        
    return {service_key: weighted_scores_dict}
