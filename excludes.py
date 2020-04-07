from pbcc import calculate_pbcc
from utils import get_service_config


def get_excludes(param):
    service_key = get_service_config(9)
    pbcc_dict = list(calculate_pbcc(param).values())[0]
    exclude_list = []
    for i in pbcc_dict:
        if pbcc_dict[i] < 0: # <-- some threshhold
            exclude_list.append(i)
        
    return {service_key: exclude_list}
