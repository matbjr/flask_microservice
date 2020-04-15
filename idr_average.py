from idr import calculate_idr
from config import get_service_config
from utils import update_input


def calculate_idr_average(param):
    service_key = get_service_config(11)
    inp = update_input(param)
    idr_list = list(list(calculate_idr(inp).values())[0].values())
    num_items = len(idr_list)
    idr_avg = sum(idr_list) / num_items
        
    return {service_key: round(idr_avg, 3)}
