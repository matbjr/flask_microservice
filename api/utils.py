from statistics import pstdev
from api.config import get_keyword_value


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
    inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return get_keyword_value("no_students")
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
    inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return get_keyword_value("no_students")
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
    inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return get_keyword_value("no_students")
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


def get_grad_year_list(param):
    """
    A function to get all the graduation years
    of students taking the exam:
    It iterates through every student's information
    adding their graduation year to a list if it 
    exists and isnt already in the list.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: list of strings: a list containing 
             all listed graduation years
    """
    inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return get_keyword_value("no_students")
    student_list = get_student_list(inp)
    grad_year_list = []
        
    for i in student_list:
        curr_grad_year = i[get_keyword_value("grad_year")]
        if curr_grad_year not in grad_year_list:
            grad_year_list.append(curr_grad_year)

    if len(grad_year_list) == 1:
        return get_keyword_value("no_grad_year")
    
    grad_year_list.sort()

    return grad_year_list


def sort_students_by_grad_year(param):
    """
    A function to sort students into a dictionary 
    with the graduation years as keys:
    It calls the get_grad_year_list function and
    then creates a dictionary with the years as keys.
    Then it iterates through every student and adds 
    their responses to the dictionary of their
    corresponding year.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: dictionary of responses: a dictionary
             with graduation years as keys and
             student responses as values in the
             Reliabilty Measures standard json format
    """
    inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return get_keyword_value("no_students")
    student_list = get_student_list(inp)
    grad_year_list = get_grad_year_list(inp)
    id_list = get_item_ids(inp)
    responses_by_grad_year = {}

    if grad_year_list == get_keyword_value("no_grad_year"):
        return get_keyword_value("no_grad_year")

    for i in grad_year_list:
        responses_by_grad_year[i] = {(get_keyword_value("student_list")): []}

    for i in grad_year_list:
        for k in range(0, len(student_list)): 
            curr_item_ids = []
            curr_responses = student_list[k][get_keyword_value("item_responses")]
            for j in curr_responses:
                curr_item_ids.append(j[get_keyword_value("item_id")])
            for j in id_list:
                if j not in curr_item_ids:
                    student_list[k][get_keyword_value("item_responses")].append({get_keyword_value("item_id"): j, get_keyword_value("response"): 0})
            if student_list[k][get_keyword_value("grad_year")] == i:
                responses_by_grad_year[i][get_keyword_value("student_list")].append(student_list[k])

    return responses_by_grad_year


def get_student_ids(param):
    """
    A function to get a list of all the student ids:
    It iterates through every student and adds their
    id to a list.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: list of strings: a list containing all student ids
    """
    inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return get_keyword_value("no_students")
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
             id, and grad year if given
    """
    inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return get_keyword_value("no_students")
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
    exclude_students = list(param.get(get_keyword_value("exclude_students"), []))
    exclude_items = list(param.get(get_keyword_value("exclude_items"), []))
    student_list = list(param.get(get_keyword_value("student_list"), []))

    # If no exam object is given or no exam name is given, name it "unknown"
    exam_info = param.get(get_keyword_value("exam"))
    if not exam_info:
        inp[get_keyword_value("exam")] = {get_keyword_value("name"): get_keyword_value("unknown")}
    else:
        exam_name = exam_info[get_keyword_value("name")]
        if not exam_name:
            inp[get_keyword_value("exam")][get_keyword_value("name")] = get_keyword_value("unknown")

    # If no student data was given, return with message
    if not student_list:
        return get_keyword_value("no_students")

    # If a student does not have responses, give him an empty response list
    for i in range(0, len(student_list)):
        curr_responses = student_list[i].get(get_keyword_value("item_responses"))
        if not curr_responses:
            student_list[i][get_keyword_value("item_responses")] = []
        
    # If a student does not have an id, assign their index+1 as their id
    for i in range(0, len(student_list)):
        curr_stud = student_list[i].get(get_keyword_value("id"))
        curr_grad_yr = student_list[i].get(get_keyword_value("grad_year"))
        if not curr_stud:
            student_list[i][(get_keyword_value("id"))] = str(i+1)
        if not curr_grad_yr:
            student_list[i][(get_keyword_value("grad_year"))] = get_keyword_value("unknown")

    # If an item in a student's response list does not have an id, assign its index+1 as its id
    # If an item in a student's response list does not have a response, assign it a value of 0
    for i in range(0, len(student_list)):
        curr_responses = student_list[i][get_keyword_value("item_responses")]
        for k in range(0, len(curr_responses)):
            curr_item_id = curr_responses[k].get(get_keyword_value("item_id"))
            curr_item = curr_responses[k].get(get_keyword_value("response"))
            if not curr_item_id:
                student_list[i][get_keyword_value("item_responses")][k][get_keyword_value("item_id")] = str(k+1)
            if not curr_item:
                student_list[i][get_keyword_value("item_responses")][k][get_keyword_value("response")] = 0

    # If a student's id is in the exclude list, exclude them from the data
    remove_students = []
    for i in student_list:
        if i[get_keyword_value("id")] in exclude_students:
            remove_students.append(i)
    for i in remove_students:
        student_list.remove(i)

    # If an item's id is in the exclude list, exclude it from the data
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
    inp = inp = update_input(param)
    if inp == get_keyword_value("no_students"):
        return get_keyword_value("no_students")
    topics = inp.get(get_keyword_value("item_topics"))
    
    if not topics:
        return get_keyword_value("no_topics")

    tree_dict = {}
    index = 0
    for i in topics:
        index += 1
        item = i.get(get_keyword_value("item_id"), index)
        tree_dict[item] = []
        tags = i.get(get_keyword_value("tags"))
        if tags:
            for k in tags:
                if k.get(get_keyword_value("scored"), "Y") != "Y":
                    continue
                curr_tree = k.get(get_keyword_value("topic_tree"), 
                            inp[get_keyword_value("exam")][get_keyword_value("name")])
                curr_levels = k.get(get_keyword_value("topic_branch_hierarchy"))
                curr_topic = k.get(get_keyword_value("topic_tagged"), get_keyword_value("unknown"))

                level_list = []
                if curr_levels:
                    for i in curr_levels:
                        level_list.append(int(i))
                    level_list.sort(reverse=True)

                hier_level = {}
                hier_level[0] = curr_tree
                if curr_levels:
                    for i in range(1, level_list[0]+2):
                        hier_level[i] = curr_levels.get(str(i-1), "Unkown")
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
