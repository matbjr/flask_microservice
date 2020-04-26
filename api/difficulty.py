from api.utils import get_sorted_responses, get_item_ids, get_student_list, update_input, get_error
from api.config import get_service_config, get_keyword_value


def calculate_difficulty(param):
    """
    A function to get the difficulty of 
    each item on the exam:
    It calculates how many students got an
    item correct, and then divides it by
    the total number of students.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a dictionary of floats: a dictionary
             with item ids as keys and the
             difficulty as values
    """
    service_key = get_service_config(3)
    catch_error = get_error(param)
    if catch_error[0]:
        return {service_key: catch_error[1]}
    inp = update_input(param)
    sorted_resp = get_sorted_responses(inp)
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

def calculate_difficulty_average(param):
    """
    A function to get the average difficulty
    of items on the exam:
    It gets the difficulty of every item and then 
    calculates the average of those difficulties.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a float: the difficulty average
    """
    service_key = get_service_config(10)
    catch_error = get_error(param)
    if catch_error[0]:
        return {service_key: catch_error[1]}
    inp = update_input(param)
    diff_list = list(list(calculate_difficulty(inp).values())[0].values())
    num_items = len(diff_list)
    diff_avg = sum(diff_list) / num_items
        
    return {service_key: round(diff_avg, 3)}
