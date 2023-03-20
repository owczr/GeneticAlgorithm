import math

import numpy as np


def generate(x_lim, y_lim, count):
    x_list = np.random.randint(*x_lim, count)
    y_list = np.random.randint(*y_lim, count)

    return tuple(zip(x_list, y_list))


def distance(point_1, point_2):
    x_1 = point_1[0]
    y_1 = point_1[1]
    x_2 = point_2[0]
    y_2 = point_2[1]

    return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)


def plot(ax, x_lim, y_lim, point_tuples):
    ax.set_xlim(*x_lim)
    ax.set_ylim(*y_lim)
    x, y = zip(*point_tuples)
    ax.scatter(x, y)

