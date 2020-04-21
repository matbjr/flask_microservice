from api.utils import get_student_list , update_input, get_item_topics
from api.config import get_service_config, get_keyword_value


def calculate_topic_rights(param):
    """
    A function to calculate the number of
    correct responses in every topic for each
    student:
    It gets a list of every topic with its
    corresponding item id. If a student gets
    that item correct, then the number of right
    responses for that topic increases.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a dictionary of dictionaries:
             a dictionary with student ids as keys
             and a list of topics and their number
             of right responses
    """
    service_key = get_service_config(15)
    inp = update_input(param)
    student_list = get_student_list(inp)
    check_topics = get_item_topics(inp)
    topic_rights = {}

    if check_topics == get_keyword_value("no_topics"):
        return {service_key: get_keyword_value("no_topics")}

    for i in student_list:
        topic_trees = get_item_topics(inp)
        stud_id = i[get_keyword_value("id")]
        responses = i[get_keyword_value("item_responses")]
        for k in responses:
            item_id = k[get_keyword_value("item_id")]
            item_resp = k[get_keyword_value("response")]
            for j in range(0, len(topic_trees)):
                topic_ids = topic_trees[j][get_keyword_value("topic_ids")]
                if item_resp == 1 and item_id in topic_ids:
                    topic_trees[j][get_keyword_value("topic_rights")] += 1

        for k in range(0, len(topic_trees)):
            del topic_trees[k][get_keyword_value("topic_ids")]

        topic_rights[stud_id] = topic_trees


    return {service_key: topic_rights}


def calculate_topic_averages(param):
    """
    A function to calculate the average number of
    correct responses in every topic:
    It gets the total number of right responses
    per topic and then divides them by the total
    number of students.

    :param: a json in the Reliabilty Measures
            standard json format
    :return: a list of dictionaries, a list of
             each topic and its average number
             of right responses
    """
    service_key = get_service_config(16)
    inp = update_input(param)
    topic_avgs = get_item_topics(inp)
    topic_responses = calculate_topic_rights(inp)[get_service_config(15)]
    num_topics = len(topic_avgs)
    num_students = len(topic_responses)
    check_topics = get_item_topics(inp)

    if check_topics == get_keyword_value("no_topics"):
        return {service_key: get_keyword_value("no_topics")}

    for i in range(0, num_topics):
        avg_rights = 0
        for k in topic_responses:
            rights = topic_responses[k][i][get_keyword_value("topic_rights")]
            avg_rights += rights
        avg_rights /= num_students
        avg_rights = round(avg_rights, 3)
        topic_avgs[i][get_keyword_value("topic_rights")] = avg_rights

    for i in range(0, num_topics):
            del topic_avgs[i][get_keyword_value("topic_ids")]

    return {service_key: topic_avgs}
    