import numpy as np
import numba
from src.data import Problem, Case, Matter
from src.common.trivial_reducer import trivial_reducer
from src.solver.common.color import only_color


@numba.jit('i8[:](i8[:, :], i8[:, :])', nopython=True)
def find_color_change_rule_one(x_arr, y_arr):

    # -2: not assigned, -1: failed
    res_vec = -2 * np.ones(10, dtype=np.int64)
    fail_vec = -1 * np.ones(10, dtype=np.int64)

    for i in range(x_arr.shape[0]):
        for j in range(x_arr.shape[1]):
            c_x = x_arr[i, j]
            c_y = y_arr[i, j]
            if res_vec[c_x] == -2:
                res_vec[c_x] = c_y
            elif res_vec[c_x] != c_y:
                return fail_vec

    return res_vec


@numba.jit('i8[:, :](i8[:, :], i8[:])', nopython=True)
def fit_color_change_rule_one(x_arr, rule):
    # -2: not assigned, -1: failed
    y_arr = np.zeros(x_arr.shape, dtype=np.int64)

    for i in range(x_arr.shape[0]):
        for j in range(x_arr.shape[1]):
            y_arr[i, j] = rule[x_arr[i, j]]

    return y_arr


def color_change(p: Problem) -> Problem:
    assert only_color(p)
    # print(p)
    case_x: Case
    case_y: Case
    case_x_new: Case

    change_vec = -2 * np.ones(10, dtype=np.int64)

    for case_x, case_y in zip(p.train_x_list, p.train_y_list):

        # need to be one matter
        assert len(case_y.matter_list) == 1
        if len(case_x.matter_list) == 1:
            x_values = case_x.repr_values()
        else:
            x_values = trivial_reducer(case_x)
        y_values = case_y.repr_values()

        # same shape
        assert x_values.shape == y_values.shape

        # value range
        assert x_values.min() >= 0
        assert x_values.max() <= 9
        assert y_values.min() >= 0
        assert y_values.max() <= 9

        # one rule
        res_arr = find_color_change_rule_one(x_values, y_values)
        # print(res_arr)

        for c in range(10):
            if res_arr[c] == -2:
                pass
            elif change_vec[c] == -2:
                change_vec[c] = res_arr[c]
            else:
                assert change_vec[c] == res_arr[c]

    # print(change_vec)
    # fill
    for c in range(10):
        if (change_vec == c).sum() >= 3:
            change_vec[change_vec == -2] = c

    q: Problem
    q = p.copy()
    q.train_x_list = []
    q.test_x_list = []

    # transform
    # test_x first so that find exception faster
    for case_x in p.test_x_list:
        if len(case_x.matter_list) == 1:
            x_values = case_x.repr_values()
        else:
            x_values = trivial_reducer(case_x)
        # print(x_values)
        # value range
        assert x_values.min() >= 0
        assert x_values.max() <= 9

        # change_vec
        new_values = fit_color_change_rule_one(x_values, change_vec)
        assert new_values.min() >= 0  # no more-2
        # print(new_values)
        case_x_new = case_x.copy()
        case_x_new.matter_list = [Matter(new_values, background_color=case_x_new.background_color, new=True)]
        q.test_x_list.append(case_x_new)
    # train_x
    for case_x in p.train_x_list:
        if len(case_x.matter_list) == 1:
            x_values = case_x.repr_values()
        else:
            x_values = trivial_reducer(case_x)
        # print(x_values)
        # value range
        assert x_values.min() >= 0
        assert x_values.max() <= 9

        # change_vec
        new_values = fit_color_change_rule_one(x_values, change_vec)
        # print(new_values)
        case_x_new = case_x.copy()
        case_x_new.matter_list = [Matter(new_values, background_color=case_x_new.background_color, new=True)]
        q.train_x_list.append(case_x_new)

    return q
