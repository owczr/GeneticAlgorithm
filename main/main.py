import numpy as np

import utils


def gen_points(x_lim, y_lim, count):
    x_list = np.random.randint(*x_lim, count)
    y_list = np.random.randint(*y_lim, count)

    return x_list, y_list


if __name__ == "__main__":
    utils.set_seeds()
    print((gen_points(utils.X_LIM, utils.Y_LIM, utils.POINTS_NO)[0]))
