from api.utils import get_sorted_responses, get_item_ids, get_student_list, update_input
from api.config import get_service_config, get_keyword_value


def calculate_num_correct(param):
    service_key = get_service_config(12)
    inp = update_input(param)
    student_list = {get_keyword_value("student_list"): get_student_list(inp)}
    sorted_resp = get_sorted_responses(student_list)
    num_students = len(sorted_resp)
    num_items = len(sorted_resp[0])
    id_list = get_item_ids(inp)
    num_correct_list = []
    num_correct_dict = {}

    for i in range(0, num_items):  # For each question i
        num_right = 0
        for k in range(0, num_students): # For each student k
            student_answer = sorted_resp[k][i]
            num_right += student_answer
        num_correct_list.append(num_right)

    k = 0
    for i in id_list:
        num_correct_dict[i] = num_correct_list[k]
        k += 1

    return {service_key: num_correct_dict}
