import numpy as np


X_LIM = (0, 300)
Y_LIM = (0, 300)
POINTS_NO = 30


def gen_points(x_lim, y_lim, count):
    x_list = np.random.randint(*x_lim, count)
    y_list = np.random.randint(*y_lim, count)

    return x_list, y_list


if __name__ == "__main__":
    print((gen_points(X_LIM, Y_LIM, POINTS_NO)[0]))
