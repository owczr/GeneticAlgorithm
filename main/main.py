import math

import matplotlib.pyplot as plt

import utils
from points import points
from population import population


if __name__ == "__main__":
    utils.set_seeds()
    points_list = points.generate(utils.X_LIM, utils.Y_LIM, utils.POINTS_NO)

    population_list = population.generate_first(10, utils.POINTS_NO)
    distance_list = population.calculate_distance(population_list, points_list)
    population.select_elite(distance_list, population_list)

    #
    # fig, axs = plt.subplots(1, 1)
    #
    # points.plot(axs, utils.X_LIM, utils.Y_LIM, points_list)
    #
    # plt.show()
