import numpy as np
from src.data import Problem, Case


def fill_pattern(p: Problem) -> Problem:
    assert p.is_pattern

    # assert
    case_x: Case
    case_y: Case
    for case_x, case_y in zip(p.train_x_list, p.train_y_list):
        # equal or background
        x_values = case_x.repr_values()
        y_values = case_y.repr_values()
        assert x_values.shape == y_values.shape

        for i in range(x_values.shape[0]):
            for j in range(x_values.shape[1]):
                assert x_values[i, j] == case_x.background_color or x_values[i, j] == y_values[i, j]

        # all color appear
        x_cnt = case_x.color_count
        y_cnt = case_y.color_count
        for c in range(10):
            if y_cnt[c] > 0:
                assert x_cnt[c] > 0

    q: Problem
    q = p.copy()
    q.train_x_list = []
    c_x: Case
    c_y: Case
    for c_y in q.train_y_list:
        c_x = Case()
        c_x.initialize(c_y.repr_values())
        q.train_x_list.append(c_x)

    q.test_x_list = []
    base_values = p.train_y_list[0].repr_values()
    for c_x in p.test_x_list:
        old_values = c_x.repr_values()
        new_values = np.ones(c_x.shape, dtype=np.int8) * c_x.background_color
        assert old_values.shape == base_values.shape
        for i in range(old_values.shape[0]):
            for j in range(old_values.shape[1]):
                if old_values[i, j] != c_x.background_color and new_values[i, j] == c_x.background_color:
                    new_values[base_values == base_values[i, j]] = old_values[i, j]
        c_new = Case()
        c_new.initialize(new_values)
        q.test_x_list.append(c_new)
    return q
