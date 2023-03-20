import math

import numpy as np

import utils
from points import points

if __name__ == "__main__":
    utils.set_seeds()
    points_list = points.generate(utils.X_LIM, utils.Y_LIM, utils.POINTS_NO)
    print(points.distance(points_list[0], points_list[1]))
    print(points.distance((1, 1), (0, 0)))
