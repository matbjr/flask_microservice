from api.idr import calculate_idr
from api.config import get_service_config, get_keyword_value
from api.utils import update_input


def get_exclude_recos(param):
    service_key = get_service_config(9)
    inp = update_input(param)
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
