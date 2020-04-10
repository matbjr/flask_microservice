from providers.cloud_handler import get_config_file


# JSON object for literals and constants
# will be hosted in some cloud storage
# all keys are lower case, Use underscore for longer keys

# need to read from env
cloud_provider = {
    'cloud_host': 'dropbox',
    'cloud_config_file': 'config.json',
    'cloud_access_key': 'vDuiM-56ZzsAAAAAAAAHJGw5MRrhkkeJZ0AJhft11_SCePhuuP2XCVGY3pMGvLBn',
}

# default
config = {
    'application_id': 'rm_01',
    'application_version': '0.1.1',
    'application_name': 'Reliability Measures microservices',
    'application_short_name': 'rm_microservices',
    'service_url': 'http://api.reliabilitymeasures.com/',
    'test_url': 'http://localhost:5000/',
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
        }
    ]
}

# more to follow


def get_service_config(service_id):
    return config['services'][service_id]['short_name']


def get_config(config_key):
    return config.get(config_key)


def get_config_from_cloud(cloud_provider):
    try:
        config = get_config_file(cloud_provider)
    except Exception as exc:
        print("Config Exception!")

