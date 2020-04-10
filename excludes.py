from idr import calculate_idr
from config import get_service_config
from key_map import get_keyword_value


def get_exclude_recos(param):
    service_key = get_service_config(9)
    idr_dict = list(calculate_idr(param).values())[0]
    exclude_list = []
    for i in idr_dict:
        if idr_dict[i] <= get_keyword_value('exclude_threshold_1'):
            exclude_list.append(i)
    
    if len(exclude_list) >= len(idr_dict)*get_keyword_value('exclude_length_1'):
        exclude_list = []
        for i in idr_dict:
            if idr_dict[i] < get_keyword_value('exclude_threshold_2'):
                exclude_list.append(i)
    
    if len(exclude_list) >= len(idr_dict)*get_keyword_value('exclude_length_2'):
        return {service_key: get_keyword_value('bad_exam')}
        
    return {service_key: exclude_list}
