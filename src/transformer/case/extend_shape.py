import numpy as np
from src.data import Case, Matter


def extend_shape(c: Case) -> Case:
    assert c.shape != c.n_row, c.n_col
    assert c.shape[0] <= c.n_row
    assert c.shape[1] <= c.n_col

    base_values = c.repr_values()
    new_values = (-1) * np.ones((c.n_row, c.n_col), dtype=np.int)
    new_values[:c.shape[0], :c.shape[1]] = base_values

    new_case = c.copy()
    new_case.matter_list = [Matter(new_values, background_color=np.int(-1))]
    new_case.shape = new_case.n_row, new_case.n_col
    new_case.background_color = -1
    return new_case
