"""Class for single member of a population"""


class Element:
    def __init__(self, permutations):
        self.__permutations = permutations
        self.__distance = None
        self.__rank = None

    @property
    def permutations(self):
        return self.__permutations

    @permutations.setter
    def permutations(self, permutations):
        self.__permutations = permutations

    @permutations.getter
    def permutations(self):
        return self.__permutations

    @permutations.deleter
    def permutations(self):
        del self.__permutations

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
