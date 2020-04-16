from api.config import get_keyword_value, get_service_config
from api.utils import get_id_list, get_student_list, update_input


def get_assumptions(param):
    service_key = get_service_config(13)
    inp = update_input(param)
    student_list = get_student_list(inp)
    idList = get_id_list(inp)
    assumptions_dict = {}
    
    for i in student_list: # For each student i
        checklist = idList.copy()
        for k in i[get_keyword_value("item_responses")]: # For each question k
            for j in idList: # For each item ID j
                if k[get_keyword_value("item_id")] == j: # If item IDs match
                    checklist.remove(j)

        if len(checklist) != 0:
            assumptions_dict[i[get_keyword_value("id")]] = checklist.copy()

    if not assumptions_dict:
        return {service_key: get_keyword_value("no_assumptions")}

    return {service_key: assumptions_dict}
