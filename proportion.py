def calculate_proportion(param):
    user_list = list(param['twoElements'])
    propo_value = user_list[0]/user_list[1]
    return {'proportion': round(propo_value, 3)}
