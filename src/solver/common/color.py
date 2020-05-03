import numpy as np
from src.data import Problem, Case


def monotone_color(p: Problem) -> np.int:
    color_count = np.array([case.color_count for case in p.train_y_list]).sum(axis=0)
    # ignore background
    color_count[p.background_color] = 0
    # only color other than background
    if (color_count > 0).sum() == 1:
        color_add = color_count.argmax()
    else:
        color_add = -1
    return np.int(color_add)


def new_color(p: Problem) -> np.int:
    case_x: Case
    case_y: Case
    new_color_count = np.zeros(10, dtype=np.int)
    for case_x, case_y in zip(p.train_x_list, p.train_y_list):
        y_values = case_y.repr_values()
        x_values = case_x.repr_values()
        if x_values.shape != y_values.shape:
            return np.int(-1)
        # find not equal, add y color
        for i in range(y_values.shape[0]):
            for j in range(y_values.shape[1]):
                if y_values[i, j] != x_values[i, j]:
                    new_color_count[y_values[i, j]] += 1

    if (new_color_count > 0).sum() == 1:
        color_add = new_color_count.argmax()
    else:
        color_add = -1
    return np.int(color_add)