from idr import calculate_idr
from utils import get_service_config


def calculate_idr_average(param):
    service_key = get_service_config(11)
    idr_list = list(list(calculate_idr(param).values())[0].values())
    num_items = len(idr_list)
    idr_avg = sum(idr_list) / num_items
        
    return {service_key: round(idr_avg, 3)}
