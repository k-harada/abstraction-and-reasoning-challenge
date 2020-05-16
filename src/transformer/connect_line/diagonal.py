import numpy as np
import numba
from src.data import Problem, Case, Matter
from src.solver.common.shape import is_same


@numba.jit('i8[:, :](i8[:, :], i8)', nopython=True)
def connect_diagonal(x_arr, background) -> np.array:
    """
    :param x_arr: np.array(np.int)
    :param background: np.int, must be one of 0-9
    :return: new_array connected, colors over color, map-apply-reduce if necessary
    """
    n_row, n_col = x_arr.shape
    diff_max = max(n_row, n_col)
    sum_max = n_row + n_col
    new_x_arr = x_arr.copy()
    for c in range(10):
        if c == background:
            continue
        # right-down
        for d in range(-diff_max, diff_max):
            i_d_list = [0]
            i_d_list.pop()
            for i in range(n_row):
                if 0 <= i - d < n_col:
                    if x_arr[i, i - d] == c:
                        i_d_list.append(i)
            if len(i_d_list) >= 2:
                for i in range(i_d_list[0], i_d_list[-1] + 1):
                    if x_arr[i, i - d] == background:
                        new_x_arr[i, i - d] = c
        # left-down
        for d in range(sum_max):
            i_d_list = [0]
            i_d_list.pop()
            for i in range(n_row):
                if 0 <= d - i < n_col:
                    if x_arr[i, d - i] == c:
                        i_d_list.append(i)
            if len(i_d_list) >= 2:
                for i in range(i_d_list[0], i_d_list[-1] + 1):
                    if x_arr[i, d - i] == background:
                        new_x_arr[i, d - i] = c

    return new_x_arr


class ConnectDiagonal:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter) -> Matter:
        new_values = connect_diagonal(m.values, m.background_color)
        new_matter: Matter = m.copy()
        new_matter.set_values(new_values)
        return new_matter

    @classmethod
    def case(cls, c: Case) -> Case:
        new_case = c.copy()
        new_case.matter_list = [m if m.is_mesh else cls.matter(m) for m in c.matter_list]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        assert is_same(p)
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
