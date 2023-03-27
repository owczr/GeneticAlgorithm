import math

import numpy as np

# TODO: Generate new population
# TODO: Calculate distances
# TODO: Retain elite, select parents
# TODO:     Selection method: rank, roulette
# TODO: Create new population
# TODO: Early stopping
# TODO:     When no improvement increase mutation
# TOD0: At least 1000 times
# TODO: Visualization


def generate_first(population_size, points_count):
    perm_list = [np.random.permutation(points_count) for _ in range(population_size)]
    return perm_list


def distance(point_1, point_2):
    x_1 = point_1[0]
    y_1 = point_1[1]
    x_2 = point_2[0]
    y_2 = point_2[1]

    return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)


def calculate_distance(population_list, points_list):
    for population in population_list:
        points_new = points_list[population]
        distance_list = [distance(p1, p2) for p1, p2 in zip(points_new[:-1], points_new[1:])]
        distance_list = distance_list + [distance(points_new[-1], points_new[0])]

        return distance_list
