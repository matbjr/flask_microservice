import numpy as np


def calculate_std(param):
    user_list = list(param['elements'])
    std_value = float(np.std(user_list))
    return {'Std': round(std_value, 3)}
