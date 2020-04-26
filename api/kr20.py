from api.utils import get_score_std, get_sorted_responses, get_student_list, update_input, get_error
from api.config import get_service_config, get_keyword_value


def calculate_kr20(param):
    """
    A function to get the kr20 value of an exam:
    First it get the number of items divided by the
    number of items - 1. Then it multiplies that by 
    1 - the summation of the product of the 
    proportion of those who got an item right by the
    proportion of those who got it wrong divided by the
    variance of the students' scores.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a float: the kr20
    """
    service_key = get_service_config(1)
    catch_error = get_error(param)
    if catch_error[0]:
        return {service_key: catch_error[1]}
    inp = update_input(param)
    sorted_resp = get_sorted_responses(inp)
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
