type_map = {
    'type_list': [
        {
            'type': 'Multiple Choice',
            'id': 0
        },
    ]
}


def get_type_id(item_type):
    type_id = -1
    for i in type_map['type_list']:
        if i['type'] == item_type:
            type_id = i['id']
    return type_id
