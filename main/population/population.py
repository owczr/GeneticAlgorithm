import math

import numpy as np
from scipy.stats import rankdata
from sklearn.preprocessing import MinMaxScaler

from .element import Element


# TODO: Generate new population
# TODO: Calculate distances
# TODO: Retain elite, select parents
# TODO:     Selection method: rank, roulette
# TODO: Create new population
# TODO: Early stopping
# TODO:     When no improvement increase mutation
# TOD0: At least 1000 times
# TODO: Visualization


def _distance(point_1, point_2):
    x_1 = point_1[0]
    y_1 = point_1[1]
    x_2 = point_2[0]
    y_2 = point_2[1]

    return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)


class Population:
    def __init__(self, population_size, points_count, points):
        self.__elements = self.__generate_first(population_size, points_count)
        self.__size = population_size
        self.__points = points
        self.__points_count = points_count

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, elements):
        self.__elements = elements

    @elements.getter
    def elements(self):
        return self.__elements

    @elements.deleter
    def elements(self):
        del self.__elements

    @classmethod
    def __generate_first(cls, population_size: int, points_count: int) -> list:
        elements = [Element(np.random.permutation(points_count)) for _ in range(population_size)]
        return elements

    @classmethod
    def generate_population(cls, probabilities, population_list):
        pass

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        self.__points = points

    @points.getter
    def points(self):
        return self.__points

    @points.deleter
    def points(self):
        del self.__points

    def calculate_distances(self):
        for element in self.elements:
            points_new = self.points[element.permutations]
            distances = [_distance(p1, p2) for p1, p2 in zip(points_new[:-1], points_new[1:])]
            distances = distances + [_distance(points_new[-1], points_new[0])]
            element.distance = sum(distances)

    def select_elite(self, method="rank"):
        self.__set_ranks()
        if method == "rank":
            self.__select_by_rank()
        elif method == "roulette":
            self.__select_by_roulette()
        else:
            raise NameError(f"Method {method} not supported")

    def __select_by_rank(self):
        index = 0
        for probability in np.random.random(self.__size):
            if probability > self.elements[index].rank:
                del self.elements[index]
                index = index - 1
            index = index + 1

    def __select_by_roulette(self):
        pass

    def __set_ranks(self):
        distances = [element.distance for element in self.elements]
        ranks = len(distances) - rankdata(distances)

        scaler = MinMaxScaler(feature_range=(0, 1))
        ranks_std = scaler.fit_transform(np.array(ranks).reshape(-1, 1))

        for element, rank in zip(self.elements, ranks_std):
            element.rank = rank

    @staticmethod
    def __one_point_crossover(first_parent, second_parent, point):
        first_child = np.concatenate((first_parent[:point], second_parent[point:]))
        second_child = np.concatenate((second_parent[:point], first_parent[point:]))

        return first_child, second_child

    @staticmethod
    def __two_point_crossover(first_parent, second_parent, points):
        p1, p2 = points

        first_child = np.concatenate((first_parent[:p1], second_parent[p1:p2], first_parent[p2:]))
        second_child = np.concatenate((second_parent[:p1], first_parent[p1:p2], second_parent[p2:]))

        return first_child, second_child

    def crossover(self, keep_parents=True, two_point=False):
        element_lenght = len(self.elements[0])

        if two_point:
            crossover_point = sorted(np.random.randint(1, element_lenght, 2))
            crossover_function = self.__two_point_crossover
        else:
            crossover_point = np.random.randint(1, element_lenght)
            crossover_function = self.__one_point_crossover

        first_parent_indexes = np.random.randint(0, len(self.elements), element_lenght)
        second_parent_indexes = np.random.randint(0, len(self.elements), element_lenght)

        children = []
        for first, second in zip(first_parent_indexes, second_parent_indexes):
            children.append(crossover_function(self.elements[first].permutations,
                                               self.elements[second].permutations,
                                               crossover_point))

        return children
