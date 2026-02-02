from math import log, sqrt

def calculate_log_return(start_price, end_price):
    return log(end_price / start_price)

def calculate_variance(dataset):
    mean = sum(dataset) / len(dataset)
    numerator = 0

    for x in dataset:
        numerator += (x - mean) ** 2

    return numerator / len(dataset)

def calculate_stddev(dataset):
    return sqrt(calculate_variance(dataset))

def calculate_correlation(set_x, set_y):
    sum_x = sum(set_x)
    sum_y = sum(set_y)

    sum_x2 = sum(x ** 2 for x in set_x)
    sum_y2 = sum(y ** 2 for y in set_y)
    sum_xy = sum(x * y for x, y in zip(set_x, set_y))

    n = len(set_x)

    numerator = n * sum_xy - sum_x * sum_y
    denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

    return numerator / denominator
