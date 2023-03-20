import math

import numpy as np

import utils


def gen_points(x_lim, y_lim, count):
    x_list = np.random.randint(*x_lim, count)
    y_list = np.random.randint(*y_lim, count)

    return tuple(zip(x_list, y_list))


def points_distance(point_1, point_2):
    x_1 = point_1[0]
    y_1 = point_1[1]
    x_2 = point_2[0]
    y_2 = point_2[1]

    return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)


if __name__ == "__main__":
    utils.set_seeds()
    points = gen_points(utils.X_LIM, utils.Y_LIM, utils.POINTS_NO)
    # print(points_distance(points[0], points[1]))
    print(points_distance((1, 1), (0, 0)))
