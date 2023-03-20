import math

import matplotlib.pyplot as plt

import utils
from points import points


if __name__ == "__main__":
    utils.set_seeds()
    points_list = points.generate(utils.X_LIM, utils.Y_LIM, utils.POINTS_NO)

    fig, axs = plt.subplots(1, 1)

    points.plot(axs, utils.X_LIM, utils.Y_LIM, points_list)

    plt.show()
