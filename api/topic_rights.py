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

    if not check_topics:
        return {service_key: get_keyword_value("no_topics")}

    for i in student_list:
        topic_trees = get_item_topics(inp)
        stud_id = i[get_keyword_value("id")]
        topic_rights[stud_id] = []
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

        topic_rights[stud_id].append(topic_trees)


    return {service_key: topic_rights}
    