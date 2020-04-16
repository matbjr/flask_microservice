def calculate_summation(param):
    user_list = list(param["elements"])
    sum_value = sum(user_list)
    return {"sum": round(sum_value, 3)}