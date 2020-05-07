import numpy as np
import numba
from src.data import Problem, Case, Matter
from src.solver.common.shape import is_same


@numba.jit('i8(i8[:, :], i8)', nopython=True)
def find_periodicity_row(x_arr, background):
    """
    :param x_arr: np.array(int)
    :param background: int
    :return: int, minimum period
    """
    for p in range(1, x_arr.shape[0]):

        res = True

        i = 0
        while i < p and res:
            for j in range(x_arr.shape[1]):
                colors = np.unique(x_arr[i::p, j])
                if len(colors) >= 3:
                    res = False
                    break
                elif colors.shape[0] == 2 and background not in list(colors):
                    res = False
                    break
            i += 1
        if res:
            return p
    return x_arr.shape[0]


@numba.jit('i8[:, :](i8[:, :], i8, i8)', nopython=True)
def fill_periodicity_row(x_arr, p, background):
    """
    :param x_arr: np.array(int)
    :param p: period
    :param background: int
    :return: np.array(int), filled array
    """
    # assertion
    assert x_arr.shape[0] > 0 and x_arr.shape[1] > 0

    # trivial case
    if p == x_arr.shape[0]:
        return x_arr.copy()

    y_arr = x_arr.copy()

    for i in range(p):
        for j in range(x_arr.shape[1]):
            v = background
            for a in x_arr[i::p, j]:
                if a != background:
                    v = a
            y_arr[i::p, j] = v

    return y_arr


class AutoFillRowColPeriodicity:

    def __init__(self):
        pass

    @classmethod
    def find_periodicity_col(cls, x_arr, background=0):
        """
        :param x_arr: np.array(int)
        :param background: int
        :return: int, minimum period
        """
        return find_periodicity_row(x_arr.transpose(), background)

    @classmethod
    def auto_fill_row(cls, x_arr, background=0):
        """
        :param x_arr: np.array(int), must be >= 0 otherwise returns x_arr.copy()
        :param background: int
        :return: np.array(int), filled array in row_wise
        """
        p_row = find_periodicity_row(x_arr, background)
        return fill_periodicity_row(x_arr, p_row, background)

    @classmethod
    def auto_fill_col(cls, x_arr, background=0):
        """
        :param x_arr: np.array(int), must be >= 0 otherwise returns x_arr.copy()
        :param background: int
        :return: np.array(int), filled array in col_wise
        """
        return cls.auto_fill_row(x_arr.transpose(), background).transpose()

    @classmethod
    def auto_fill_row_col(cls, x_arr, background=0):
        """
        :param x_arr: np.array(int), must be >= 0 otherwise returns x_arr.copy()
        :param background: int
        :return: np.array(int), filled array in row_wise and col_wise, row first
        """
        y_arr = x_arr.copy()

        iter_times = 0
        while iter_times < 10000:
            z_arr, y_arr = y_arr, cls.auto_fill_row(y_arr, background)
            z_arr, y_arr = y_arr, cls.auto_fill_col(y_arr, background)
            if np.abs(z_arr - y_arr).sum() == 0:
                return z_arr
            iter_times += 1
        assert iter_times == -1  # break by assertion error
        return None

    @classmethod
    def auto_fill_row_col_background(cls, x_arr):
        cost = 10000
        background_res = 0
        for background in range(10):
            z_arr = cls.auto_fill_row_col(x_arr, background)
            cost_temp = find_periodicity_row(z_arr, background) * cls.find_periodicity_col(z_arr, background)
            if cost_temp < cost:
                cost = cost_temp
                background_res = background
        return cls.auto_fill_row_col(x_arr, background_res)

    @classmethod
    def case_row(cls, c: Case) -> Case:
        new_case = c.copy()
        new_values = cls.auto_fill_row(c.repr_values(), c.background_color)
        new_case.matter_list = [Matter(new_values, background_color=c.background_color, new=True)]
        return new_case

    @classmethod
    def case_col(cls, c: Case) -> Case:
        new_case = c.copy()
        new_values = cls.auto_fill_col(c.repr_values(), c.background_color)
        new_case.matter_list = [Matter(new_values, background_color=c.background_color, new=True)]
        return new_case

    @classmethod
    def case_row_col(cls, c: Case) -> Case:
        new_case = c.copy()
        new_values = cls.auto_fill_row_col(c.repr_values(), c.background_color)
        new_case.matter_list = [Matter(new_values, background_color=c.background_color, new=True)]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        assert is_same(p)
        if p.is_periodic_row and p.is_periodic_col:
            q: Problem = p.copy()
            q.train_x_list = [cls.case_row_col(c) for c in p.train_x_list]
            q.test_x_list = [cls.case_row_col(c) for c in p.test_x_list]
        elif p.is_periodic_row:
            q: Problem = p.copy()
            q.train_x_list = [cls.case_row(c) for c in p.train_x_list]
            q.test_x_list = [cls.case_row(c) for c in p.test_x_list]
        elif p.is_periodic_col:
            q: Problem = p.copy()
            q.train_x_list = [cls.case_col(c) for c in p.train_x_list]
            q.test_x_list = [cls.case_col(c) for c in p.test_x_list]
        else:
            raise AssertionError
        return q


if __name__ == "__main__":
    x = np.ones((5, 3), dtype=np.int)
    print(find_periodicity_row(x, 0))
    x[1, :] = 2
    print(find_periodicity_row(x, 0))
    x[3, :] = 2
    print(find_periodicity_row(x, 0))
    print(AutoFillRowColPeriodicity.find_periodicity_col(x))
    x = np.zeros((5, 3), dtype=np.int)
    print(find_periodicity_row(x, 0))
    print(find_periodicity_row(x, -1))
    x[1, :] = 2
    print(find_periodicity_row(x, 0))
    print(find_periodicity_row(x, -1))
    x[3, :] = 2
    print(find_periodicity_row(x, 0))
    print(find_periodicity_row(x, -1))
    print(AutoFillRowColPeriodicity.find_periodicity_col(x))
    print(AutoFillRowColPeriodicity.find_periodicity_col(x, -1))

    x = np.zeros((5, 3), dtype=np.int)
    x[1, :] = 2
    print(fill_periodicity_row(x, 2, 0))
    print(fill_periodicity_row(x, 3, 0))
    x = np.zeros((5, 3), dtype=np.int)
    x[:2, :2] = 1
    x[1, 1] = 2
    print(find_periodicity_row(x, 0))
    print(fill_periodicity_row(x, 2, 0))
    print(AutoFillRowColPeriodicity.auto_fill_row(x))
    print(AutoFillRowColPeriodicity.auto_fill_row_col(x))

    x = np.ones((5, 3), dtype=np.int)
    x[1, :] = 3
    x[3:, :] = 5
    print(x)
    print(AutoFillRowColPeriodicity.auto_fill_row_col_background(x))

