import math

import matplotlib.pyplot as plt

import utils
from points import points
from population.population import Population


if __name__ == "__main__":
    utils.set_seeds()
    points = points.generate(utils.X_LIM, utils.Y_LIM, utils.POINTS_NO)

    population = Population(10, utils.POINTS_NO, points)
    population.calculate_distances()

    population.select_elite()

    print(len(population.crossover(keep_parents=True)))

    # for prob, dist, pop in zip(probabilities, distance_list, population):
    #     print(prob, sum(dist), pop)

    #
    # fig, axs = plt.subplots(1, 1)
    #
    # points.plot(axs, utils.X_LIM, utils.Y_LIM, points_list)
    #
    # plt.show()

#%%
