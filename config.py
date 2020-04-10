# JSON object for literals and constants
# will be hosted in some cloud storage
# all keys are lower case, Use underscore for longer keys
config = {
    'cloud_host': 'xxx',
    'cloud_host_credentials':'yyyy',
    'application_id': 'rm_01',
    'application_version': '0.1.3',
    'application_name': 'Reliability Measures microservices',
    'application_short_name': 'rm_microservices',
    'service_url': 'http://api.reliabilitymeasures.com/',
    'test_url': 'http://localhost:5000/',
    'keywords': {
            'item_responses': 'item_responses',
            'student_list': 'student_list',
            'item_id': 'item_id',
            'response': 'response',

            'exclude_threshold_1': 0.09,
            'exclude_threshold_2': 0,
            'exclude_length_1': 0.5,
            'exclude_length_2': 0.8,
            'bad_exam': 'bad_exam',

            'bad_std': 'Invalid data - No Std. Dev.',
            'bad_mean': 'Invalid data - No mean'
    },  
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
            'short_name': 'idr',
            'description': 'Item discrimination, Point biserial correlation coefficient',
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
            'name': 'Weighted Scores',
            'short_name': 'weighted_scores',
            'description': 'Weighted test scores',
            'type': 'list of floats'
        },
        {
            'id': 8,
            'name': 'Weighted Average',
            'short_name': 'weighted_avg',
            'description': 'Weighted Average of Weighted test scores',
            'type': 'float'
        },
        {
            'id': 9,
            'name': 'exclude_items',
            'short_name': 'exclude',
            'description': 'Items to exclude based on idr',
            'type': 'list of item ids'
        },
        {
            'id': 10,
            'name': 'difficulty_average',
            'short_name': 'diff_avg',
            'description': 'The average difficulty',
            'type': 'float'
        },
        {
            'id': 11,
            'name': 'discrimination_average',
            'short_name': 'idr_avg',
            'description': 'The average item discrimination',
            'type': 'float'
        },
        {
            'id': 12,
            'name': 'number_of_correct_responses',
            'short_name': 'num_correct',
            'description': 'The absolute number of an item\'s correct responses',
            'type': 'list of ints'
        }
    ] 
}

# more to follow


def get_keyword_value(key):
    return config['keywords'][key]


def get_service_config(service_id):
    return config['services'][service_id]['short_name']


def get_config(config_key):
    return config.get(config_key)
