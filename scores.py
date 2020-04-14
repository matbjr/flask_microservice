from utils import get_sorted_responses, get_student_list
from config import get_service_config, get_keyword_value


def calculate_scores(param):
    service_key = get_service_config(4)
    student_list = get_student_list(param)
    sortedResponses = get_sorted_responses(param)
    numItems = len (sortedResponses[0])
    score_dict = {}

    for i in student_list:
        stud_id = i[get_keyword_value('id')]
        score_dict[stud_id] = None

    k = 0
    for i in score_dict:
        numRight = sum(sortedResponses[k])
        score = numRight / numItems
        score = round(score * 100, 1)
        score_dict[i] = score
        k += 1

    return {service_key: score_dict}
