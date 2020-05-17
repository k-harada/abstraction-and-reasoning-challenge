import numpy as np
from src.data import Problem, Case
from .case import point_cross_cnt_case, point_cross_fit_case


def point_cross_cnt(p: Problem) -> np.array:

    res_problem = np.zeros((10, 5), dtype=int)
    c_x: Case
    c_y: Case
    for c_x, c_y in zip(p.train_x_list, p.train_y_list):
        assert c_x.shape == c_y.shape
        y_arr = c_y.repr_values()
        res_case = point_cross_cnt_case(c_x, y_arr)
        for x, c in res_case:
            res_problem[c, :] += x

    return res_problem


def point_cross(p: Problem) -> Problem:

    res_problem = point_cross_cnt(p)
    op_arr = np.zeros(10, dtype=int)
    for c in range(10):
        c_min = res_problem[c, :].min()
        # keep > delete > cross > row > col
        if res_problem[c, 1] == c_min:
            op_arr[c] = 1
        elif res_problem[c, 0] == c_min:
            op_arr[c] = 0
        elif res_problem[c, 4] == c_min:
            op_arr[c] = 4
        elif res_problem[c, 2] == c_min:
            op_arr[c] = 2
        else:  # res_problem[c, 3] == c_min:
            op_arr[c] = 3

    q: Problem = p.copy()
    q.train_x_list = [point_cross_fit_case(c, op_arr) for c in p.train_x_list]
    q.test_x_list = [point_cross_fit_case(c, op_arr) for c in p.test_x_list]

    return q
