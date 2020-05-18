type_map = {
    'type_list': [
        {
            'type': 'Multiple Choice',
            'google_form': 'MULTIPLE_CHOICE',
            'description': 'A question item that allows the respondent to '
                           'select one choice from a list of radio buttons '
                           'or an optional "other" field.',
            'id': 0
        },
        {
            'type': 'Multiple Checkbox',
            'google_form': 'CHECKBOX',
            'description': 'A question item that allows the respondent to '
                           'select one or more checkboxes, as well as an '
                           'optional "other" field.',
            'id': 1
        },
        {
            'type': 'Text',
            'google_form': 'TEXT',
            'description': 'A question item that allows the respondent to '
                           'enter a single line of text.',
            'id': 2
        },
        {
            'type': 'Text Box',
            'google_form': 'PARAGRAPH_TEXT',
            'description': 'A question item that allows the respondent to '
                           'enter a block of text.',
            'id': 3
        },
    ]
}


def get_type_id(item_type):
    type_id = -1
    for i in type_map['type_list']:
        if item_type in [i['type'], i['google_form']]:
            return i['id']
    return type_id


def get_type_from_id(item_id, type='type'):
    for i in type_map['type_list']:
        if item_id == i['id']:
            return i[type]
    return None
