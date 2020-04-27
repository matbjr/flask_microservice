from common.config import get_keyword_value, get_service_config
from common.utils import get_item_ids, get_student_list, update_input


def get_assumptions(param):
    """
    A function to get the items for which a
    student was assumed to have a response
    of 0:
    It gets a list of all item ids listed from
    every student's responses, then iterates
    through every student. If a student doesn't
    have a response for an item in the id list,
    then that item is assumed to have a response
    of 0 for that student.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a dictionary of dictionaries:
             a dictionary with student ids as keys
             and a list of item ids as values
    """
    service_key = get_service_config(13)
    inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return {service_key: get_keyword_value("no_students")}
    student_list = get_student_list(inp)
    id_list = get_item_ids(inp)
    assumptions_dict = {}
    
    for i in student_list: # For each student i
        checklist = id_list.copy()
        dupes = []
        for k in i[get_keyword_value("item_responses")]: # For each question k
            for j in id_list: # For each item ID j
                if k[get_keyword_value("item_id")] == j: # If item IDs match
                    if j in checklist:
                        checklist.remove(j)
                    else:
                        dupes.append(j)
        if dupes:
            assumptions_dict[i[get_keyword_value("id")]] = {}
            assumptions_dict[i[get_keyword_value("id")]][get_keyword_value("dupes")] = dupes
            
        if len(checklist) != 0:
            assumptions_dict[i[get_keyword_value("id")]] = {}
            assumptions_dict[i[get_keyword_value("id")]][get_keyword_value("assumed")] = checklist.copy()

    if not assumptions_dict:
        return {service_key: get_keyword_value("no_assumptions")}

    return {service_key: assumptions_dict}
