import numpy as np

from .points import generate
from .utils import set_seeds, X_LIM, Y_LIM, POINTS_NO, POPULATION_SIZE
from .population import Population


def run():
    best_distances = []
    best_chromosomes = []
    minimal_mutation_probability = 0.01
    set_seeds()
    points = generate(X_LIM, Y_LIM, POINTS_NO)
    # Generate initial population
    initial_population = Population.generate_first(POPULATION_SIZE, POINTS_NO)

    # Create Population object
    population = Population(initial_population, POINTS_NO, points, minimal_mutation_probability)

    while True:
        # Drop elements with duplicates
        population.drop_duplicates()

        # Calculate distances
        population.calculate_distances()

        # Get the best element distance
        best_distance = population.best_distance()
        best_distances.append(best_distance)

        # Get the best chromosomes
        best_chromosome = population.best_chromosome()
        best_chromosomes.append(best_chromosome)
        print(best_distance)

        # Check for improvement
        # If none increase mutation
        mutation_probability = increase_mutation(population, best_distances, minimal_mutation_probability)

        if early_stopping(best_distances):
            break
        # Select best elements
        population.select_elite(limit=POPULATION_SIZE, method="roulette")

        # Create children elements
        children_permutations = population.crossover(keep_parents=POPULATION_SIZE)

        # Create new Population object
        children_elements = Population.generate_elements(children_permutations)
        population = Population(children_elements, POINTS_NO, points, mutation_probability)

        # Mutate elements
        population.mutate()

    return best_distances, best_chromosomes, population.points


def increase_mutation(population, best_distances, minimal_mutation_probability, strength=1, patience=7):
    mutation_probability = population.mutation_probability
    if len(best_distances) < patience:
        return mutation_probability

    last_distances = best_distances[-patience:]

    if all(np.array(last_distances) == last_distances[0]):
        mutation_probability += 0.01 * strength
        print(f"Increasing {mutation_probability}")
    else:
        decreased_mutation_probability = mutation_probability - 0.01 * strength

        if decreased_mutation_probability > minimal_mutation_probability:
            mutation_probability = decreased_mutation_probability
        else:
            mutation_probability = minimal_mutation_probability

        print(f"Decreasing {mutation_probability}")

    return mutation_probability


def early_stopping(best_distances, patience=15):
    if len(best_distances) < patience:
        return False

    last_distances = best_distances[-patience:]

    if all(np.array(last_distances) == last_distances[0]):
        return True
    return False
