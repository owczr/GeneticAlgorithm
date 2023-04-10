from .points import generate
from .utils import set_seeds, X_LIM, Y_LIM, POINTS_NO, POPULATION_SIZE
from .population import Population


# TODO: Generate new population
# TODO: Calculate distances
# TODO: Retain elite, select parents
# TODO:     Selection method: rank, roulette
# TODO: Create new population
# TODO: Early stopping
# TODO:     When no improvement increase mutation
# TOD0: At least 1000 times
# TODO: Visualization


def run():
    set_seeds()
    points = generate(X_LIM, Y_LIM, POINTS_NO)

    # Generate initial population
    initial_population = Population.generate_first(10, POINTS_NO)

    # Create Population object
    population = Population(initial_population, POINTS_NO, points)

    for i in range(100):
        # Calculate distances
        population.calculate_distances()

        # Get the best element distance
        best_distance = population.best_distance()
        print(best_distance)

        # Select best elements
        population.select_elite(limit=POPULATION_SIZE, method="roulette")

        # Create children elements
        children_permutations = population.crossover(keep_parents=True)

        # Create new Population object
        children_elements = Population.generate_elements(children_permutations)
        population = Population(children_elements, POINTS_NO, points)

        # Mutate elements
        population.mutate()

        print(len(population.elements))


