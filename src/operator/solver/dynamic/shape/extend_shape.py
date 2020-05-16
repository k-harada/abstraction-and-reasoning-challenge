import numpy as np
from src.data import Problem, Case, Matter
from src.operator.solver.common.shape import is_constant


def extend_shape_case(c: Case, n_row: int, n_col: int) -> Case:
    assert c.shape != n_row, n_col
    assert c.shape[0] <= n_row
    assert c.shape[1] <= n_col

    base_values = c.repr_values()
    new_background = -1
    for color in range(10):
        if (base_values == color).sum() == 0:
            new_background = color
            break
    assert new_background != -1
    new_values = new_background * np.ones((n_row, n_col), dtype=np.int)
    new_values[:c.shape[0], :c.shape[1]] = base_values

    new_case = c.copy()
    m: Matter
    new_case.matter_list = [m.deepcopy() for m in c.matter_list]
    for m in new_case.matter_list:
        m.background_color = new_background
    new_case.shape = n_row, n_col
    new_case.background_color = new_background
    return new_case


def extend_shape(p: Problem) -> Problem:
    """Expand shape so as to fit y, filled with new color for each case, that color is new background"""
    flag, n_row, n_col = is_constant(p)
    assert flag

    q: Problem
    q = p.copy()
    q.train_x_list = [extend_shape_case(c, n_row, n_col) for c in p.train_x_list]
    q.test_x_list = [extend_shape_case(c, n_row, n_col) for c in p.test_x_list]
    return q
