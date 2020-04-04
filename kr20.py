from utils import get_item_std
from utils import get_sorted_responses

def calculate_kr20(param):
    sortedResponses = get_sorted_responses(param)
    numStudents = len(sortedResponses)
    numItems = len (sortedResponses[0])
    pqList = []
    scoreSTD = get_item_std(sortedResponses, numStudents)

    if scoreSTD <=0:
        return {'Error': 'Invalid data - No Std. Dev.'}

    for i in range(0, numItems):
        p = 0
        for k in range(0, numStudents):
            p += sortedResponses[k][i]
        p /= numStudents
        q = 1 - p
        pqList.append(p * q)
    pqSum = sum(pqList)

    # need validation here
    kr20_value = (numItems /(numItems - 1)) * (1 - (pqSum / (scoreSTD ** 2)))

    return {'KR20': round(kr20_value, 3)}
