"""Class for single member of a population"""
import numpy as np


class Element:
    def __init__(self, permutations):
        self.chromosomes = permutations
        self.distance = None
        self.rank = None

    def __len__(self):
        return len(self.chromosomes)

    def mutate(self, mask):
        chromosomes_to_mutate = self.chromosomes[mask]
        chromosomes_mutated = np.random.permutation(chromosomes_to_mutate)
        self.chromosomes[mask] = chromosomes_mutated
