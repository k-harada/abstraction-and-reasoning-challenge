import numpy as np
from src.data import Problem, Case, Matter
from src.solver.common.shape import is_constant


def extend_shape_case(c: Case, n_row: int, n_col: int) -> Case:
    assert c.shape != n_row, n_col
    assert c.shape[0] <= n_row
    assert c.shape[1] <= n_col

    base_values = c.repr_values()
    new_values = (-1) * np.ones((n_row, n_col), dtype=np.int)
    new_values[:c.shape[0], :c.shape[1]] = base_values

    new_case = c.copy()
    m: Matter
    new_case.matter_list = [m.deepcopy() for m in c.matter_list]
    for m in new_case.matter_list:
        m.background_color = -1
    new_case.shape = n_row, n_col
    new_case.background_color = -1
    return new_case


def extend_shape(p: Problem) -> Problem:
    flag, n_row, n_col = is_constant(p)
    assert flag

    q: Problem
    q = p.copy()
    q.train_x_list = [extend_shape_case(c, n_row, n_col) for c in p.train_x_list]
    q.test_x_list = [extend_shape_case(c, n_row, n_col) for c in p.test_x_list]
    return q
