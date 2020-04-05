from statistics import pstdev


def calculate_std(param):
    user_list = list(param['elements'])
    std_value = float(pstdev(user_list))
    return {'std': round(std_value, 3)}
