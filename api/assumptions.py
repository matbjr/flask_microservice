from api.config import get_keyword_value, get_service_config
from api.utils import get_item_ids, get_student_list, update_input


def get_assumptions(param):
    service_key = get_service_config(13)
    inp = update_input(param)
    student_list = get_student_list(inp)
    id_list = get_item_ids(inp)
    assumptions_dict = {}
    
    for i in student_list: # For each student i
        checklist = id_list.copy()
        for k in i[get_keyword_value("item_responses")]: # For each question k
            for j in id_list: # For each item ID j
                if k[get_keyword_value("item_id")] == j: # If item IDs match
                    checklist.remove(j)

        if len(checklist) != 0:
            assumptions_dict[i[get_keyword_value("id")]] = checklist.copy()

    if not assumptions_dict:
        return {service_key: get_keyword_value("no_assumptions")}

    return {service_key: assumptions_dict}
