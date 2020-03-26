import numpy as np


def calculate_proportion(param):
    user_list = list(param['twoElements'])
    propo_value = np.divide(user_list[0], user_list[1])
    return {'Proportion': round(propo_value, 3)}
