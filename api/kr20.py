from api.utils import get_score_std, get_sorted_responses, get_student_list, update_input
from api.config import get_service_config, get_keyword_value


def calculate_kr20(param):
    service_key = get_service_config(1)
    inp = update_input(param)
    student_list = {get_keyword_value("student_list"): get_student_list(inp)}
    sorted_resp = get_sorted_responses(student_list)
    num_students = len(sorted_resp)
    num_items = len (sorted_resp[0])
    pq_list = []
    score_std = get_score_std(inp)

    if score_std <= 0:
        return {service_key: get_keyword_value("bad_std")}

    for i in range(0, num_items):
        p = 0
        for k in range(0, num_students):
            p += sorted_resp[k][i]
        p /= num_students
        q = 1 - p
        pq_list.append(p * q)
    pq_sum = sum(pq_list)

    kr20_value = (num_items /(num_items - 1)) * (1 - (pq_sum / (score_std ** 2)))

    return {service_key: round(kr20_value, 3)}
