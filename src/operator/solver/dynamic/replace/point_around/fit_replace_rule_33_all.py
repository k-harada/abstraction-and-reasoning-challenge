from typing import List
import numpy as np
from src.data import Problem, Case, Matter


def find_replace_rule_33_one_all(x_arr, y_arr, background):

    assert min(x_arr.shape) >= 3
    assert x_arr.shape == y_arr.shape

    res_arr = (-2) * np.ones((3, 3), dtype=int)

    # left up
    query_arr = (x_arr[1:, 1:] != background) * (x_arr[:-1, :-1] == background)
    res = np.unique(y_arr[:-1, :-1][query_arr])
    if res.shape[0] == 1 and res[0] != background:
        res_arr[0, 0] = res[0]

    # left
    query_arr = (x_arr[:, 1:] != background) * (x_arr[:, :-1] == background)
    res = np.unique(y_arr[:, :-1][query_arr])
    if res.shape[0] == 1 and res[0] != background:
        res_arr[1, 0] = res[0]

    # left down
    query_arr = (x_arr[:-1, 1:] != background) * (x_arr[1:, :-1] == background)
    res = np.unique(y_arr[1:, :-1][query_arr])
    if res.shape[0] == 1 and res[0] != background:
        res_arr[2, 0] = res[0]

    # up
    query_arr = (x_arr[1:, :] != background) * (x_arr[:-1, :] == background)
    res = np.unique(y_arr[:-1, :][query_arr])
    if res.shape[0] == 1 and res[0] != background:
        res_arr[0, 1] = res[0]

    # self
    query_arr = (x_arr != background)
    if query_arr.sum() > 0:
        if (x_arr[query_arr] == y_arr[query_arr]).min():
            res_arr[1, 1] = -1
        else:
            res = np.unique(y_arr[query_arr])
            if res.shape[0] == 1:
                res_arr[1, 1] = res[0]

    # down
    query_arr = (x_arr[:-1, :] != background) * (x_arr[1:, :] == background)
    res = np.unique(y_arr[1:, :][query_arr])
    if res.shape[0] == 1 and res[0] != background:
        res_arr[2, 1] = res[0]

    # right up
    query_arr = (x_arr[1:, :-1] != background) * (x_arr[:-1, 1:] == background)
    res = np.unique(y_arr[:-1, 1:][query_arr])
    if res.shape[0] == 1 and res[0] != background:
        res_arr[0, 2] = res[0]

    # right
    query_arr = (x_arr[:, :-1] != background) * (x_arr[:, 1:] == background)
    res = np.unique(y_arr[:, 1:][query_arr])
    if res.shape[0] == 1 and res[0] != background:
        res_arr[1, 2] = res[0]

    # right down
    query_arr = (x_arr[:-1, :-1] != background) * (x_arr[1:, 1:] == background)
    res = np.unique(y_arr[1:, 1:][query_arr])
    if res.shape[0] == 1 and res[0] != background:
        res_arr[2, 2] = res[0]

    return res_arr


def find_replace_rule_33_all(x_arr_list: List[np.array], y_arr_list: List[np.array], background: int = 0) -> np.array:

    res_arr = -2 * np.ones((3, 3), dtype=np.int)
    n = len(x_arr_list)
    assert n == len(y_arr_list)

    # pick 3x3
    for k in range(n):
        x_arr = x_arr_list[k]
        y_arr = y_arr_list[k]
        assert x_arr.shape == y_arr.shape
        res_arr_one = find_replace_rule_33_one_all(x_arr, y_arr, background)

        for i in range(3):
            for j in range(3):
                if res_arr_one[i, j] == -2:
                    pass
                elif res_arr[i, j] == -2:
                    res_arr[i, j] = res_arr_one[i, j]
                else:
                    assert res_arr[i, j] == res_arr_one[i, j]

    return res_arr


def fit_replace_rule_33_one_all(x_arr, rule, background):
    n_row, n_col = x_arr.shape
    y_arr = background * np.ones((n_row, n_col), dtype=np.int64)

    # left up
    query_arr = (x_arr[1:, 1:] != background) * (x_arr[:-1, :-1] == background)
    if rule[0, 0] != -2:
        y_arr[:-1, :-1][query_arr] = rule[0, 0]

    # left
    query_arr = (x_arr[:, 1:] != background) * (x_arr[:, :-1] == background)
    if rule[1, 0] != -2:
        y_arr[:, :-1][query_arr] = rule[1, 0]

    # left down
    query_arr = (x_arr[:-1, 1:] != background) * (x_arr[1:, :-1] == background)
    if rule[2, 0] != -2:
        y_arr[1:, :-1][query_arr] = rule[2, 0]

    # up
    query_arr = (x_arr[1:, :] != background) * (x_arr[:-1, :] == background)
    if rule[0, 1] != -2:
        y_arr[:-1, :][query_arr] = rule[0, 1]

    # self
    query_arr = (x_arr != background)
    if rule[1, 1] >= 0:
        y_arr[query_arr] = rule[1, 1]
    elif rule[1, 1] == -1:
        y_arr[query_arr] = x_arr[query_arr]

    # down
    query_arr = (x_arr[:-1, :] != background) * (x_arr[1:, :] == background)
    if rule[2, 1] != -2:
        y_arr[1:, :][query_arr] = rule[2, 1]

    # right up
    query_arr = (x_arr[1:, :-1] != background) * (x_arr[:-1, 1:] == background)
    if rule[0, 2] != -2:
        y_arr[:-1, 1:][query_arr] = rule[0, 2]

    # right
    query_arr = (x_arr[:, :-1] != background) * (x_arr[:, 1:] == background)
    if rule[1, 2] != -2:
        y_arr[:, 1:][query_arr] = rule[1, 2]

    # right down
    query_arr = (x_arr[:-1, :-1] != background) * (x_arr[1:, 1:] == background)
    if rule[2, 2] != -2:
        y_arr[1:, 1:][query_arr] = rule[2, 2]

    return y_arr


class FitRuleOne33All:

    def __init__(self):
        pass

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        c_x: Case
        c_y: Case

        # find rule
        x_arr_list = []
        y_arr_list = []
        for c_x, c_y in zip(p.train_x_list, p.train_y_list):
            assert c_x.background_color == p.background_color
            x_arr_list.append(c_x.repr_values())
            y_arr_list.append(c_y.repr_values())

        rule_33 = find_replace_rule_33_all(x_arr_list, y_arr_list, p.background_color)

        # fit rule
        q: Problem = p.copy()
        q.train_x_list = []
        q.test_x_list = []
        c_x: Case
        c_x_new: Case
        for c_x in p.train_x_list:
            c_x_new = c_x.copy()
            new_values = fit_replace_rule_33_one_all(c_x.repr_values(), rule_33, p.background_color)
            c_x_new.matter_list = [Matter(new_values, background_color=p.background_color, new=True)]
            q.train_x_list.append(c_x_new)

        for c_x in p.test_x_list:
            c_x_new = c_x.copy()
            new_values = fit_replace_rule_33_one_all(c_x.repr_values(), rule_33, p.background_color)
            c_x_new.matter_list = [Matter(new_values, background_color=p.background_color, new=True)]
            q.test_x_list.append(c_x_new)

        return q


if __name__ == "__main__":
    x_list = [
        np.array([[0, 0, 0], [0, 1, 0], [0, 2, 0]], dtype=np.int),
        np.array([[1, 0, 0], [0, 1, 0], [0, 2, 0]], dtype=np.int)
    ]
    y_list = [
        np.array([[5, 5, 5], [5, 1, 5], [5, 2, 5]], dtype=np.int),
        np.array([[1, 5, 5], [5, 1, 5], [5, 2, 5]], dtype=np.int)
    ]
    import time
    t0 = time.time()
    print(find_replace_rule_33_one_all(x_list[0], y_list[0], 0))
    print(time.time() - t0)
    t0 = time.time()
    rule_easy = find_replace_rule_33_all(x_list, y_list)
    print(time.time() - t0)
    print(rule_easy)
    print(fit_replace_rule_33_one_all(x_list[0], rule_easy, 0))
    print(fit_replace_rule_33_one_all(x_list[1], rule_easy, 0))

    pp = Problem.load(94)
    qq = FitRuleOne33All.problem(pp)
    print(qq)

    pp = Problem.load(265)
    qq = FitRuleOne33All.problem(pp)
    print(qq)

    pp = Problem.load(330)
    qq = FitRuleOne33All.problem(pp)
    print(qq)
