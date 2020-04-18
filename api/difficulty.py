from api.utils import get_sorted_responses, get_item_ids, get_student_list, update_input
from api.config import get_service_config, get_keyword_value


def calculate_difficulty(param):
    service_key = get_service_config(3)
    inp = update_input(param)
    student_list = {get_keyword_value("student_list"): get_student_list(inp)}
    sorted_resp = get_sorted_responses(student_list)
    num_students = len(sorted_resp)
    num_items = len (sorted_resp[0])
    id_list = get_item_ids(inp)
    difficulty_list = []
    difficulty_dict = {}

    for i in range(0, num_items): # For each question i
        numRight = 0
        for k in range(0, num_students): # For each student k
            studentAnswer = sorted_resp[k][i]
            numRight += studentAnswer
        difficulty = 1 - numRight / num_students
        difficulty = round(difficulty, 3)
        difficulty_list.append(difficulty)

    k = 0
    for i in id_list:
        difficulty_dict[i] = difficulty_list[k]
        k += 1
        
    return {service_key: difficulty_dict}
