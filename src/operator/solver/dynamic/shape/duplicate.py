import numpy as np
from src.data import Problem, Case, Matter
from src.operator.solver.common.shape import is_multiple, is_constant


def duplicate(p: Problem) -> Problem:

    flag, m_row, m_col = is_multiple(p)
    flag_n = False

    if not flag:
        flag, nc_row, nc_col = is_constant(p)
        flag_n = True

    assert flag

    q: Problem
    q = p.copy()
    q.train_x_list = []
    q.test_x_list = []
    c_x: Case
    c_x_new: Case
    for c_x in p.train_x_list:
        c_x_new = c_x.copy()
        base_values = c_x.repr_values()
        n_row, n_col = base_values.shape
        if flag_n:
            assert nc_row % n_row == 0
            assert nc_col % n_col == 0
            m_row = nc_row // n_row
            m_col = nc_col // n_col
        c_x_new.shape = m_row * n_row, m_col * n_col
        new_values = np.zeros((m_row * n_row, m_col * n_col), dtype=np.int)
        for i in range(m_row):
            for j in range(m_col):
                new_values[i * n_row:(i + 1) * n_row, j * n_col:(j + 1) * n_col] = base_values
        c_x_new.matter_list = [Matter(new_values, background_color=c_x.background_color, new=True)]
        q.train_x_list.append(c_x_new)

    for c_x in p.test_x_list:
        c_x_new = c_x.copy()
        base_values = c_x.repr_values()
        n_row, n_col = base_values.shape
        c_x_new.shape = m_row * n_row, m_col * n_col
        new_values = np.zeros((m_row * n_row, m_col * n_col), dtype=np.int)
        for i in range(m_row):
            for j in range(m_col):
                new_values[i * n_row:(i + 1) * n_row, j * n_col:(j + 1) * n_col] = base_values
        c_x_new.matter_list = [Matter(new_values, background_color=c_x.background_color, new=True)]
        q.test_x_list.append(c_x_new)

    return q
