import numpy as np

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
    best_distances = []

    set_seeds()
    points = generate(X_LIM, Y_LIM, POINTS_NO)

    # Generate initial population
    initial_population = Population.generate_first(10, POINTS_NO)

    # Create Population object
    population = Population(initial_population, POINTS_NO, points)

    while True:
        # Calculate distances
        population.calculate_distances()

        # Get the best element distance
        best_distance = population.best_distance()
        best_distances.append(best_distance)

        # Check for improvement
        if early_stopping(best_distances):
            break
        # Select best elements
        population.select_elite(limit=POPULATION_SIZE, method="roulette")

        # Create children elements
        children_permutations = population.crossover(keep_parents=POPULATION_SIZE)

        # Create new Population object
        children_elements = Population.generate_elements(children_permutations)
        population = Population(children_elements, POINTS_NO, points)

        # Mutate elements
        population.mutate()


def early_stopping(best_distances, patience=5):
    if len(best_distances) < patience:
        return False

    last_distances = best_distances[-patience:]

    if all(np.array(last_distances) == last_distances[0]):
        return True
    return False
