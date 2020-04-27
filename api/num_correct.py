from common.utils import get_sorted_responses, get_item_ids, update_input
from common.config import get_service_config


def calculate_num_correct(param):
    """
    A function to get the number of students who
    got an item correct:
    It iterates over each item, counting how many
    students got it correct.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a dictionary of ints: a dictionary with
             item ids as keys and number of correct
             responses as values
    """
    service_key = get_service_config(12)
    inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return {service_key: get_keyword_value("no_students")}
    sorted_resp = get_sorted_responses(inp)
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
