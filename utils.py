from statistics import pstdev


def get_item_std(item, numStudents):
    scoreList = []
    for i in range(0, numStudents):
        score = sum(item[i])
        scoreList.append(score)
    # scoreSTD = get_std(scoreList)  # micro service call
    scoreSTD = pstdev(scoreList)

    return scoreSTD


def get_list(item, index):
    return list(item[index]['item_responses'])


def get_id_list(param):
    student_list = list(param['student_list'])
    responseList = get_list(student_list, 0)
    numItems = len(responseList)
    idList = []

    for i in range(0, numItems): # Put all item IDs into a list
        idList.append(responseList[i]['item_id'])
    idList.sort()

    return idList


def get_sorted_responses(param):
    student_list = list(param['student_list'])
    responseList = get_list(student_list, 0)
    numStudents = len(student_list)
    numItems = len(responseList)
    responses = {}

    for i in range(0, numStudents): # Check if item count is consistent
        if numItems != len(get_list(student_list, i)):
            return {'error': 'All students\' item count must be the same'}

    idList = get_id_list(param)

    for i in idList: # Create a dictionary with the item IDs as keys
        responses[i] = []
    
    for i in range(0, numStudents): # For each student i
        for k in range(0, numItems): # For each question k
            for j in responses: # For each item ID j
                if get_list(student_list, i)[k]['item_id'] == j: # If item IDs match, add response to dictionary
                    responses[j].append(get_list(student_list, i)[k]['response'])

    sortedResponses = []
    for i in range(0, numStudents): # For each student
        studentResponses = []
        for k in responses: # For every item ID
            studentResponses.append(responses[k][i]) # Create a list of the students responses sorted by item ID
        sortedResponses.append(studentResponses)

    return sortedResponses


def get_service_config(service_id):
    return config['services'][service_id]['short_name']


def get_config(config_key):
    return config.get(config_key)


# JSON object for literals and constants
# will be hosted in some cloud storage
# all keys are lower case, Use underscore for longer keys
config = {
    'cloud_host': 'xxx',
    'cloud_host_credentials':'yyyy',
    'application_id': 'rm_01',
    'application_version': '0.0.1',
    'application_name': 'Reliability Measures microservices',
    'application_short_name': 'rm_microservices',
    'service_url': 'http://visonics.net/rm/',
    'services': [
        # use the shot_name key for service path and in response key.
        # Must follow Python/JS variable rules
        {'id': 0},  # left  empty on purpose
        {
            'id': 1,
            'name': 'kr20',
            'short_name': 'kr20',
            'description': 'KR20 value',
            'type': 'float'
        },
        {
            'id': 2,
            'name': 'Item discrimination',
            'short_name': 'pbcc',
            'description': 'Item discrimination',
            'type': 'list of floats'
        },
        {
            'id': 3,
            'name': 'Item difficulty',
            'short_name': 'difficulty',
            'description': 'Item difficulty',
            'type': 'list of floats'
        },
        {
            'id': 4,
            'name': 'scores',
            'short_name': 'scores',
            'description': 'Test scores',
            'type': 'list of floats'
        },
        {
            'id': 5,
            'name': 'average',
            'short_name': 'average',
            'description': 'Student Average',
            'type': 'list of floats'
        },
        {
            'id': 6,
            'name': 'Test Analysis',
            'short_name': 'analysis',
            'description': 'The whole test analysis with all results',
            'type': 'list of items'
        },
        {
            'id': 7,
            'name': 'weighted_scores',
            'short_name': 'weighted_s',
            'description': 'Weighted test scores',
            'type': 'list of floats'
        },
        {
            'id': 8,
            'name': 'weighted_average',
            'short_name': 'weighted_avg',
            'description': 'Weighted average',
            'type': 'float'
        },
        {
            'id': 9,
            'name': 'exclude_items',
            'short_name': 'exclude',
            'description': 'Items to exclude based on pbcc',
            'type': 'list of ints' # item id might not be only ints?
        }
    ]
}

# more to follow
