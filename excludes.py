from idr import calculate_idr
from utils import get_service_config


def get_exclude_recos(param):
    service_key = get_service_config(9)
    idr_dict = list(calculate_idr(param).values())[0]
    exclude_list = []
    for i in idr_dict:
        if idr_dict[i] <= 0.09: # Hard coded
            exclude_list.append(i)
    
    if len(exclude_list) >= len(idr_dict)*0.5: # Hard coded
        exclude_list = []
        for i in idr_dict:
            if idr_dict[i] < 0: # Hard coded
                exclude_list.append(i)
    
    # if len(exclude_list) >= len(idr_dict)*0.8:
    #     then suggest that this may be a poor exam with very low exam reliability.
        
    return {service_key: exclude_list}
