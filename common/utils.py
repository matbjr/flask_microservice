from statistics import pstdev
from common.config import get_keyword_value


def get_score_std(param):
    """
    A function to calculate the standard deviation of
    the students' scores for the exam:
    It iterates through a list of each student's
    responses, putting the sums in a list, and then
    taking the standard deviation of that list.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: float: the standard deviation
    """
    catch_error = get_error(param)
    if catch_error[0]:
        return catch_error[1]
    inp = update_input(param)
    sorted_resp = get_sorted_responses(inp)
    score_list = []
    for i in sorted_resp:
        score = sum(i)
        score_list.append(score)
    # score_std = get_std(score_list)  # micro service call
    score_std = pstdev(score_list)

    return score_std


def get_item_ids(param):
    """
    A function to get a list of all the item ids 
    used in the exam:
    It iterates through a list of all the items a
    student responded to, and then adds that item's
    id to the id list if it isn't already in it.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: list of strings: a list containing all item ids
    """
    catch_error = get_error(param)
    if catch_error[0]:
        return catch_error[1]
    inp = update_input(param)
    student_list = get_student_list(inp)
    id_list = []
    response_list = []
    
    for i in student_list:
        response_list.append(i[get_keyword_value("item_responses")])
        
    for i in response_list:
        for k in i:
            curr_id = k[get_keyword_value("item_id")]
            if curr_id not in id_list:
                id_list.append(curr_id)
    
    id_list.sort()

    return id_list


def get_sorted_responses(param):
    """
    A function to sort every student's response
    to an item based on its item id:
    It calls the get_item_ids function and then
    creates a dictionary with the item ids as keys.
    Then it iterates through every students' responses
    adding each item response to its corresponding key
    in the dictionary. It then creates a now sorted 
    list of each student's responses based on its 
    index in the dictionary.


    :param: a json in the Reliabilty Measures
            standard json format
    :return: list of lists of ints: a list containing 
             all students' responses in order of item id
    """
    catch_error = get_error(param)
    if catch_error[0]:
        return catch_error[1]
    inp = update_input(param)
    student_list = get_student_list(inp)
    num_students = len(student_list)
    id_list = get_item_ids(inp)
    response_list = []
    responses = {}
    
    for i in student_list:
        response_list.append(i[get_keyword_value("item_responses")])

    for i in id_list:  # Create a dictionary with the item IDs as keys
        responses[i] = []
    
    for i in response_list:  # For each student response list i
        checklist = id_list.copy()
        for k in i: # For each question k
            for j in responses: # For each item ID j
                # If item IDs match, add response to dictionary
                if k[get_keyword_value("item_id")] == j:
                    responses[j].append(k[get_keyword_value("response")])
                    checklist.remove(j)

        if len(checklist) != 0:
            for i in checklist:
                responses[i].append(0)

    sorted_resp = []
    for i in range(0, num_students):  # For each student
        student_responses = []
        for k in responses: # For every item ID
            # Create a list of the students responses sorted by item ID
            student_responses.append(responses[k][i])
        sorted_resp.append(student_responses)

    return sorted_resp


def get_group_list(param):
    """
    A function to get all the groups
    of students taking the exam:
    It iterates through every student's information
    adding their group to a list if it 
    exists and isnt already in the list.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: list of strings: a list containing 
             all listed groups
    """
    catch_error = get_error(param)
    if catch_error[0]:
        return catch_error[1]
    inp = update_input(param)
    student_list = get_student_list(inp)
    group_list = []
        
    for i in student_list:
        curr_group = i[get_keyword_value("group")]
        for k in curr_group:
            if k not in group_list:
                group_list.append(k)

    if len(group_list) == 1:
        return get_keyword_value("no_group")
    
    group_list.sort()

    return group_list


def sort_students_by_group(param):
    """
    A function to sort students into a dictionary 
    with the groups as keys:
    It calls the get_group_list function and
    then creates a dictionary with the years as keys.
    Then it iterates through every student and adds 
    their responses to the dictionary of their
    corresponding year.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: dictionary of responses: a dictionary
             with groups as keys and
             student responses as values in the
             Reliabilty Measures standard json format
    """
    catch_error = get_error(param)
    if catch_error[0]:
        return catch_error[1]
    inp = update_input(param)
    student_list = get_student_list(inp)
    group_list = get_group_list(inp)
    id_list = get_item_ids(inp)
    responses_by_group = {}

    if group_list == get_keyword_value("no_group"):
        return get_keyword_value("no_group")

    for i in group_list:
        responses_by_group[i] = {(get_keyword_value("student_list")): [], 
                                get_keyword_value("item_topics"): inp.get(get_keyword_value("item_topics"))}

    for i in group_list:
        for k in range(0, len(student_list)): 
            curr_item_ids = []
            curr_responses = student_list[k][get_keyword_value("item_responses")]
            curr_group = student_list[k][get_keyword_value("group")]
            for j in curr_responses:
                curr_item_ids.append(j[get_keyword_value("item_id")])
            for j in id_list:
                if j not in curr_item_ids:
                    student_list[k][get_keyword_value("item_responses")].append(
                        {get_keyword_value("item_id"): j, get_keyword_value("response"): 0})
            for j in curr_group:
                if j == i:
                    responses_by_group[i][get_keyword_value("student_list")].append(student_list[k])

    return responses_by_group


def get_student_ids(param):
    """
    A function to get a list of all the student ids:
    It iterates through every student and adds their
    id to a list.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: list of strings: a list containing all student ids
    """
    catch_error = get_error(param)
    if catch_error[0]:
        return catch_error[1]
    inp = update_input(param)
    student_list = get_student_list(inp)
    student_ids = []

    for i in student_list:
        curr_id = i[get_keyword_value('id')]
        student_ids.append(curr_id)
    
    return student_ids


def get_student_list(param):
    """
    A function to get the list of students from
    the Reliabilty Measures standard json format.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: list of student information: a list
             containing every student's item responses,
             id, and group if given
    """
    catch_error = get_error(param)
    if catch_error[0]:
        return catch_error[1]
    inp = update_input(param)
    student_list = list(inp[get_keyword_value("student_list")])

    return student_list


def update_input(param):
    """
    A function to update the information of
    a json in the Reliabilty Measures standard 
    json format:
    If the json does not contain student ids, a
    default of 1-n is used. If no item ids are given.
    a default of 1-n is used. If a student or item is
    included in an exclude list, they are removed from
    the json.
    :param: a json in the Reliabilty Measures
            standard json format
    :return: a json in the Reliabilty Measures
            standard json format
    """
    inp = param
    exclude_students = list(
        param.get(get_keyword_value("exclude_students"), []))
    exclude_items = list(param.get(get_keyword_value("exclude_items"), []))
    student_list = list(param.get(get_keyword_value("student_list"), []))

    # If no student data was given, return with message
    if not student_list or len(student_list) <= 1:
        return get_keyword_value("bad_data")

    # If a student does not have responses, give him an empty response list
    for i in range(0, len(student_list)):
        curr_responses = student_list[i].get(
            get_keyword_value("item_responses"))
        if not curr_responses:
            student_list[i][get_keyword_value("item_responses")] = []

    # If all response lists are empty or only has one item, return with message
    valid_items = False
    for i in student_list:
        curr_responses = i[get_keyword_value("item_responses")]
        if len(curr_responses) > 1:
            valid_items = True
    if not valid_items:
        return get_keyword_value("bad_num_items")

    # If no exam object is given or it does not contain any info, update it with "unknown"
    exam_info = param.get(get_keyword_value("exam"))
    if not exam_info:
        inp[get_keyword_value("exam")] = {
            get_keyword_value("name"): get_keyword_value("unknown"), 
            get_keyword_value("scoring_method"): get_keyword_value("unknown")}
    else:
        exam_name = exam_info.get(get_keyword_value("name"))
        scoring_method = exam_info.get(get_keyword_value("scoring_method"))
        factor = exam_info.get(get_keyword_value("scaled_factor"))
        if not exam_name:
            inp[get_keyword_value("exam")][
                get_keyword_value("name")] = get_keyword_value("unknown")
        if not scoring_method:
            inp[get_keyword_value("exam")][
                get_keyword_value("scoring_method")] = get_keyword_value("unknown")
        if not factor:
            inp[get_keyword_value("exam")][
                get_keyword_value("scaled_factor")] = 1

    # If a student does not have an id, assign it a new id
    # If the student is given a group, assign it the group "unknown"
    student_ids = []
    for i in student_list:
        curr_stud = i.get(get_keyword_value("group"))
        if curr_stud:
            if curr_stud not in student_ids:
                student_ids.append(curr_stud)
    for i in range(0, len(student_list)):
        curr_stud = student_list[i].get(get_keyword_value("id"))
        curr_group = student_list[i].get(get_keyword_value("group"))
        new_id = 1
        if not curr_stud:
            while str(new_id) in student_ids:
                new_id += 1
            student_list[i][(get_keyword_value("id"))] = str(new_id)
            student_ids.append(str(new_id))
        if not curr_group:
            student_list[i][
                (get_keyword_value("group"))] = [get_keyword_value(
                "unknown")]

    # If an item in a student's response list does not have an id, assign it a new id
    # If an item in a student's response list does not have a response, assign it a value of 0
    item_ids = []
    for i in range(0, len(student_list)):
        curr_responses = student_list[i][get_keyword_value("item_responses")]
        for k in range(0, len(curr_responses)):
            curr_item_id = curr_responses[k].get(get_keyword_value("item_id"))
            if curr_item_id:
                if curr_item_id not in item_ids:
                    item_ids.append(curr_item_id)
    for i in range(0, len(student_list)):
        curr_responses = student_list[i][get_keyword_value("item_responses")]
        new_id = 1
        curr_new_ids = []
        for k in range(0, len(curr_responses)):
            curr_item_id = curr_responses[k].get(get_keyword_value("item_id"))
            curr_item = curr_responses[k].get(get_keyword_value("response"))
            if not curr_item_id:
                while str(new_id) in item_ids or str(new_id) in curr_new_ids:
                    new_id += 1
                student_list[i][get_keyword_value("item_responses")][k][
                    get_keyword_value("item_id")] = str(new_id)
                curr_new_ids.append(str(new_id))
            if not curr_item:
                student_list[i][get_keyword_value("item_responses")][k][
                    get_keyword_value("response")] = 0

    # If a student's id is in the exclude list, exclude them from the data
    remove_students = []
    for i in student_list:
        if i[get_keyword_value("id")] in exclude_students:
            remove_students.append(i)
    for i in remove_students:
        student_list.remove(i)

    # If an item's id is in the exclue list, exclude it from the data
    for i in range(0, len(student_list)):
        remove_items = []
        curr_responses = student_list[i][get_keyword_value("item_responses")]
        for k in curr_responses:
            curr_item = k[get_keyword_value("item_id")]
            if curr_item in exclude_items:
                remove_items.append(k)
        for k in remove_items:
            curr_responses.remove(k)
        student_list[i][get_keyword_value("item_responses")] = curr_responses

    inp[get_keyword_value("student_list")] = student_list

    # Re-check data
    student_list = list(inp.get(get_keyword_value("student_list"), []))
    if not student_list or len(student_list) <= 1:
        return get_keyword_value("bad_data")

    valid_items = False
    for i in student_list:
        curr_responses = i[get_keyword_value("item_responses")]
        if len(curr_responses) > 1:
            valid_items = True
    if not valid_items:
        return get_keyword_value("bad_num_items")

    return inp


def get_item_topics(param):
    """
    A function to get the hierarchy of all topics
    per item:
    It iterates through every items topic info and
    creates a hierarchy for each item's topics.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a list of dictionaries:
             a list of dictionaries containing a
             topic hierarchy, its corresponding item id,
             and a placeholder number of rights.
    """
    catch_error = get_error(param)
    if catch_error[0]:
        return catch_error[1]
    inp = inp = update_input(param)
    topics = inp.get(get_keyword_value("item_topics"))
    
    if not topics:
        return get_keyword_value("no_topics")

    item_ids = []
    for i in topics:
        item = i.get(get_keyword_value("item_id"))
        if item:
            if item not in item_ids:
                item_ids.append(item)

    tree_dict = {}
    index = 1
    for i in topics:
        item = i.get(get_keyword_value("item_id"))
        if not item:
            while str(index) in item_ids:
                index += 1
            item = str(index)
            item_ids.append(str(index))
        tree_dict[item] = []
        tags = i.get(get_keyword_value("tags"))
        if tags:
            for k in tags:
                if k.get(get_keyword_value("scored"), "Y") != "Y":
                    continue
                curr_tree = k.get(get_keyword_value("topic_tree"), 
                            inp[get_keyword_value("exam")][get_keyword_value("name")])
                curr_levels = k.get(get_keyword_value("topic_branch_hierarchy"))
                curr_topic = k.get(get_keyword_value("topic_tagged"), 
                             get_keyword_value("unknown"))

                level_list = []
                if curr_levels:
                    for i in curr_levels:
                        level_list.append(int(i))
                    level_list.sort(reverse=True)

                hier_level = {}
                hier_level[0] = curr_tree
                if curr_levels:
                    for i in range(1, level_list[0]+2):
                        hier_level[i] = curr_levels.get(
                            str(i-1), get_keyword_value("unknown"))
                    hier_level[level_list[0]+2] = curr_topic
                else:
                    hier_level[1] = curr_topic

                tree_dict[item].append(hier_level)
    
    tree_list = []
    for i in tree_dict:
        for k in tree_dict[i]:
            if k not in tree_list:
                tree_list.append(k)

    tree_tuple = {}
    for i in tree_list:
        tree = tuple(sorted(i.items()))
        tree_tuple[tree] = []
        for k in tree_dict:
            for j in tree_dict[k]:
                if j == i:
                    tree_tuple[tree].append(k)
    tree_tuple = tuple(tree_tuple.items())

    final_trees = []
    for i in tree_tuple:
        tree_object = {}
        ids = i[1]
        tree = i[0]
        tree_object[get_keyword_value("topic_ids")] = ids
        tree_object[get_keyword_value("topic_hierarchy")] = tree
        tree_object[get_keyword_value("topic_rights")] = 0
        final_trees.append(tree_object)

    return final_trees


def get_error(param):
    """
    A function to get the errors from an input:
    It checks whether the param is already an error
    message (from a previous update_input() call).
    If not, then it calls update_input() and checks again.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a tuple with the first value a bool
             of whether or not there was an error, and the
             second value the error message.
    """
    if param == get_keyword_value("bad_data") or param == get_keyword_value("bad_num_items"):
        return (True, param)
    inp = update_input(param)
    if inp == get_keyword_value("bad_data") or inp == get_keyword_value("bad_num_items"):
        return (True, inp)
    
    return (False, inp)


def get_scoring_method(param):
    """
    A function to get the scoring method
    of an exam:
    Returns the "scoring_method" object from the json
    and its factor for scaled scoring.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a string: containing the scoring method. 
    """
    catch_error = get_error(param)
    if catch_error[0]:
        return catch_error[1]
    inp = update_input(param)
    scoring_method = inp[get_keyword_value("exam")][
        get_keyword_value("scoring_method")]
    factor = inp[get_keyword_value("exam")][
        get_keyword_value("scaled_factor")]

    return (scoring_method, factor)