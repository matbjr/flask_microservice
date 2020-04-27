from api.idr import calculate_idr
from common.config import get_service_config, get_keyword_value
from common.utils import update_input


def get_exclude_recos(param):
    """
    A function to get a recommendation of
    items to exclude from the exam based on
    their idr values:
    It get every item's idr, and if it's less than
    0.09, it adds it to the exclude recommendations.
    If the number of recommendations is greater
    than half the number of items, only recommend
    items with idr values less than 0.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a list of strings: a list of item ids
    """
    service_key = get_service_config(9)
    inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return {service_key: get_keyword_value("no_students")}
    idr_dict = list(calculate_idr(inp).values())[0]
    if idr_dict == get_keyword_value("bad_mean"):
        return {service_key: get_keyword_value("bad_mean")}
    exclude_list = []
    for i in idr_dict:
        if idr_dict[i] <= get_keyword_value("exclude_threshold_1"):
            exclude_list.append(i)
    
    if len(exclude_list) >= len(idr_dict)*get_keyword_value("exclude_length_1"):
        exclude_list = []
        for i in idr_dict:
            if idr_dict[i] < get_keyword_value("exclude_threshold_2"):
                exclude_list.append(i)
    
    # if len(exclude_list) >= len(idr_dict)*get_keyword_value("exclude_length_2"):
    #     return {service_key: get_keyword_value("bad_exam")}
        
    return {service_key: exclude_list}
