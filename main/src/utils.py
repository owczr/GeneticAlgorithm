import random

import numpy as np


X_LIM = (0, 300)
Y_LIM = (0, 300)
POINTS_NO = 30
SEED = 42
POPULATION_SIZE = 1000


def set_seeds():
    random.seed(SEED)
    np.random.seed(SEED)
