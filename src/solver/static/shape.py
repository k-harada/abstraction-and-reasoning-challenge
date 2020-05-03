import numpy as np
from src.data import Problem, Case, Matter
from src.assisted_operator.problem import attribute as attr_prob
from src.solver.common.shape import is_same, is_constant, is_multiple, is_division


def set_problem_shape(p: Problem) -> None:
    c: Case
    m: Matter

    # same
    p.is_same_shape = is_same(p)

    # constant
    flag, n_row, n_col = is_constant(p)
    if flag:
        p.n_row, p.n_col = n_row, n_col
        for c in p.train_x_list:
            c.n_row, c.n_col = n_row, n_col
        for c in p.test_x_list:
            c.n_row, c.n_col = n_row, n_col

    # multiple
    flag, m_row, m_col = is_multiple(p)
    if flag:
        p.m_row, p.m_col = m_row, m_col
        for c in p.train_x_list:
            c.m_row, c.m_col = m_row, m_col
        for c in p.test_x_list:
            c.m_row, c.m_col = m_row, m_col

    # division
    flag, d_row, d_col = is_division(p)
    if flag:
        p.d_row, p.d_col = d_row, d_col
        for c in p.train_x_list:
            c.d_row, c.d_col = d_row, d_col
        for c in p.test_x_list:
            c.d_row, c.d_col = d_row, d_col

    return None

