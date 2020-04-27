from statistics import mean
from math import sqrt

from api.utils import get_score_std, get_sorted_responses, get_item_ids, get_student_list, update_input, get_error
from api.config import get_service_config, get_keyword_value


def calculate_idr(param):
    """
    A function to get the idr of each item:
    For every item, it calculates the mean score
    of students who got the answer right and subtracts
    it by the mean score of those who got it wrong.
    Then it multiplies that by the square root of 
    the number of students who got the item right
    multiplied by the total of those who got it wrong.
    Then it divides that by the number of students
    multiplied by the std of the students' scores.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a dictionary of floats: a dictionary with
             item ids as keys and idr as values
    """
    service_key = get_service_config(2)
    catch_error = get_error(param)
    if catch_error[0]:
        return {service_key: catch_error[1]}
    inp = update_input(param)
    sorted_resp = get_sorted_responses(inp)
    num_students = len(sorted_resp)
    num_items = len (sorted_resp[0])
    id_list = get_item_ids(inp)
    score_std = get_score_std(inp)
    idr_list = []
    idr_dict = {}

    if score_std < 0:
        return {service_key: get_keyword_value("bad_std")}

    for i in range(0, num_items): # For each question i
        right_list = []
        wrong_list = []
        num_right = 0
        num_wrong = 0
        for k in range(0, num_students): # For each student k
            if sorted_resp[k][i] == 1: # If student k gets question i correct
                score = sum(sorted_resp[k]) / num_items
                right_list.append(score) # Then add their score to the "right" list
                num_right += 1
            elif sorted_resp[k][i] == 0: # If student k gets question i wrong 
                score = sum(sorted_resp[k]) / num_items
                wrong_list.append(score) # Then add their score to the "wrong" list
                num_wrong += 1

        if num_right == num_students or num_wrong == num_students:
            idr_list.append(0)
            continue
        if len(right_list) == 1:
            right_mean = right_list[0]
        elif len(right_list) > 1:
            right_mean = mean(right_list)
        if len(wrong_list) == 1:
            wrong_mean = wrong_list[0]
        elif len(wrong_list) > 1:
            wrong_mean = mean(wrong_list)
        if not right_mean or not wrong_mean:
            return {service_key: get_keyword_value("bad_mean")}

        idr = ((right_mean - wrong_mean) * sqrt(num_right * num_wrong)) / num_students * score_std
        idr = round(idr, 3)
        idr_list.append(idr)

    k = 0
    for i in id_list:
        idr_dict[i] = idr_list[k]
        k += 1

    return {service_key: idr_dict}

def calculate_idr_average(param):
    """
    A function to get the average idr of
    the items:
    It gets a list of each item's idr, and
    then calculates the average.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a float: the average idr
    """
    service_key = get_service_config(11)
    catch_error = get_error(param)
    if catch_error[0]:
        return {service_key: catch_error[1]}
    inp = update_input(param)
    idr_dict = list(calculate_idr(inp).values())[0]
    if idr_dict == get_keyword_value("bad_mean"):
        return {service_key: get_keyword_value("bad_mean")}
    idr_list = list(list(idr_dict.values()))
    num_items = len(idr_list)
    idr_avg = sum(idr_list) / num_items
        
    return {service_key: round(idr_avg, 3)}
