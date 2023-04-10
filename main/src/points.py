import numpy as np


def generate(x_lim, y_lim, count):
    x_list = np.random.randint(*x_lim, count)
    y_list = np.random.randint(*y_lim, count)

    return np.array(tuple(zip(x_list, y_list)))
