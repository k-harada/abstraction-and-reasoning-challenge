import numpy as np
from src.data import Problem, Case, Matter
from .simple import is_multiple


def duplicate(p: Problem) -> Problem:

    assert is_multiple(p)

    cx0: Case = p.train_x_list[0]
    cy0: Case = p.train_y_list[0]
    m_row: int = cy0.shape[0] // cx0.shape[0]
    m_col: int = cy0.shape[1] // cx0.shape[1]

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
        c_x_new.shape = m_row * n_row, m_col * n_col
        new_values = np.zeros((m_row * n_row, m_col * n_col), dtype=np.int8)
        for i in range(m_row):
            for j in range(m_col):
                new_values[i * n_row:(i + 1) * n_row, j * n_col:(j + 1) * n_col] = base_values
        c_x_new.matter_list = [Matter(new_values, c_x.background_color)]
        q.train_x_list.append(c_x_new)

    for c_x in p.test_x_list:
        c_x_new = c_x.copy()
        base_values = c_x.repr_values()
        n_row, n_col = base_values.shape
        c_x_new.shape = m_row * n_row, m_col * n_col
        new_values = np.zeros((m_row * n_row, m_col * n_col), dtype=np.int8)
        for i in range(m_row):
            for j in range(m_col):
                new_values[i * n_row:(i + 1) * n_row, j * n_col:(j + 1) * n_col] = base_values
        c_x_new.matter_list = [Matter(new_values, c_x.background_color)]
        q.test_x_list.append(c_x_new)

    return q
