maps = {
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
        }
}


def get_keyword_value(key):
    return maps['keywords'][key]
