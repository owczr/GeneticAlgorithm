from src import points, utils
from src.population import Population


def main():
    utils.set_seeds()
    points_list = points.generate(utils.X_LIM, utils.Y_LIM, utils.POINTS_NO)

    # Generate initial population
    initial_population = Population.generate_first(10, utils.POINTS_NO)

    # Create Population object
    population = Population(initial_population, utils.POINTS_NO, points_list)

    # Calculate distances
    population.calculate_distances()

    # Select best elements
    population.select_elite()

    # Create children elements
    children = population.crossover(keep_parents=True)

    # Create new Population object
    population = Population(children, utils.POINTS_NO, points_list)

    print(population.elements)
    # for prob, dist, pop in zip(probabilities, distance_list, population):
    #     print(prob, sum(dist), pop)

    #
    # fig, axs = plt.subplots(1, 1)
    #
    # points.plot(axs, utils.X_LIM, utils.Y_LIM, points_list)
    #
    # plt.show()


if __name__ == "__main__":
    main()
