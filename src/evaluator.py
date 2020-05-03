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
                c_x = x_values[i, j]
                c_y = y_values[i, j]
                if c_x != c_y:
                    res += VAL_DIFF
                if keep_flag:
                    if len(color_map_list[c_x]) == 0:
                        color_map_list[c_x].append(c_y)
                    elif color_map_list[c_x][0] != c_y:
                        keep_flag = False

    # adjust
    color_map = dict()
    if 0 < res < SHAPE_DIFF_FLAG and keep_flag:
        for i in range(10):
            if len(color_map_list[i]) > 0:
                color_map[i] = color_map_list[i][0]
            else:
                color_map[i] = i
        res = 0
        for case in problem.train_x_list:
            case.color_map = color_map
        for case in problem.test_x_list:
            case.color_map = color_map

    return res
