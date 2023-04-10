"""Class for single member of a population"""
import numpy as np


class Element:
    def __init__(self, permutations):
        self.__chromosomes = permutations
        self.__distance = None
        self.__rank = None

    def __len__(self):
        return len(self.chromosomes)

    @property
    def chromosomes(self):
        return self.__chromosomes

    @chromosomes.setter
    def chromosomes(self, permutations):
        self.__chromosomes = permutations

    @chromosomes.getter
    def chromosomes(self):
        return self.__chromosomes

    @chromosomes.deleter
    def chromosomes(self):
        del self.__chromosomes

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance):
        self.__distance = distance

    @distance.getter
    def distance(self):
        return self.__distance

    @distance.deleter
    def distance(self):
        del self.__distance

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank):
        self.__rank = rank

    @rank.getter
    def rank(self):
        return self.__rank

    @rank.deleter
    def rank(self):
        del self.__rank

    def mutate(self, mask):
        chromosomes_to_mutate = self.chromosomes[mask]
        chromosomes_mutated = np.random.permutation(chromosomes_to_mutate)
        self.chromosomes[mask] = chromosomes_mutated
