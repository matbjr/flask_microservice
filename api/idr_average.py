from api.idr import calculate_idr
from api.config import get_service_config, get_keyword_value
from api.utils import update_input


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
    inp = update_input(param)
    idr_dict = list(calculate_idr(inp).values())[0]
    if idr_dict == get_keyword_value("bad_mean"):
        return {service_key: get_keyword_value("bad_mean")}
    idr_list = list(list(idr_dict.values()))
    num_items = len(idr_list)
    idr_avg = sum(idr_list) / num_items
        
    return {service_key: round(idr_avg, 3)}
