import numpy as np

from src.data import Case, Problem


SHAPE_DIFF_FLAG = 10000
VAL_DIFF = 1


def eval_distance(problem: Problem) -> np.int:

    res = 0
    case_x: Case
    case_y: Case

    # color_map
    color_map_list = [[] for _ in range(10)]
    keep_flag = True

    for case_x, case_y in zip(problem.train_x_list, problem.train_y_list):

        x_values = case_x.repr_values()
        y_values = case_y.repr_values()

        # shape
        if x_values.shape != y_values.shape:
            res += SHAPE_DIFF_FLAG

        # values
        for i in range(min(x_values.shape[0], y_values.shape[0])):
            for j in range(min(x_values.shape[1], y_values.shape[1])):
                if x_values[i, j] != y_values[i, j]:
                    res += VAL_DIFF

    return res
