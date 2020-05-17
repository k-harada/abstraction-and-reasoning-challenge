from typing import List
import numpy as np
from src.data import Problem, Case, Matter
from src.operator.solver.static import is_symmetry
from src.operator.solver.static import is_periodic
from src.operator.solver.static import is_pattern


def fusion_arr_train(x_arr: np.array, y_arr: np.array):
    # find a color with rectangle and same shape with y_arr
    for c in range(10):
        # first criteria
        if (x_arr == c).sum() != y_arr.shape[0] * y_arr.shape[1]:
            # print(c, (x_arr == c).sum(), y_arr.shape)
            continue
        x_arr_x = (x_arr == c).sum(axis=1)
        x_arr_y = (x_arr == c).sum(axis=0)
        x0 = min([i for i in range(x_arr.shape[0]) if x_arr_x[i] > 0])
        x1 = max([i for i in range(x_arr.shape[0]) if x_arr_x[i] > 0]) + 1
        y0 = min([j for j in range(x_arr.shape[1]) if x_arr_y[j] > 0])
        y1 = max([j for j in range(x_arr.shape[1]) if x_arr_y[j] > 0]) + 1
        # criteria
        if x1 - x0 != y_arr.shape[0] or y1 - y0 != y_arr.shape[1]:
            # print(c, x1 - x0, y1 - y0, y_arr.shape)
            continue
        new_y_arr = x_arr.copy()
        new_y_arr[x0:x1, y0:y1] = y_arr

        return new_y_arr, x0, x1, y0, y1, c
    raise AssertionError


def fusion_arr_test(x_arr: np.array, c_suggest: int = 0):

    # check suggested color first
    c = c_suggest
    x_arr_x = (x_arr == c).sum(axis=1)
    x_arr_y = (x_arr == c).sum(axis=0)
    if (x_arr == c).sum() > 0:
        x0 = min([i for i in range(x_arr.shape[0]) if x_arr_x[i] > 0])
        x1 = max([i for i in range(x_arr.shape[0]) if x_arr_x[i] > 0]) + 1
        y0 = min([j for j in range(x_arr.shape[1]) if x_arr_y[j] > 0])
        y1 = max([j for j in range(x_arr.shape[1]) if x_arr_y[j] > 0]) + 1

        if (x1 - x0) * (y1 - y0) == (x_arr == c).sum():
            return x0, x1, y0, y1, c

    # search
    for c in range(10):
        x_arr_x = (x_arr == c).sum(axis=1)
        x_arr_y = (x_arr == c).sum(axis=0)
        if (x_arr == c).sum() == 0:
            continue
        x0 = min([i for i in range(x_arr.shape[0]) if x_arr_x[i] > 0])
        x1 = max([i for i in range(x_arr.shape[0]) if x_arr_x[i] > 0]) + 1
        y0 = min([j for j in range(x_arr.shape[1]) if x_arr_y[j] > 0])
        y1 = max([j for j in range(x_arr.shape[1]) if x_arr_y[j] > 0]) + 1

        if (x1 - x0) * (y1 - y0) == (x_arr == c).sum():
            return x0, x1, y0, y1, c
    raise AssertionError


class Fusion:

    def __init__(self):
        pass

    @classmethod
    def matter_x(cls, m_x: Matter) -> Matter:
        return m_x.deepcopy()

    @classmethod
    def matter_y(cls, m_y: Matter, y_arr: np.array) -> Matter:
        new_matter_y = m_y.copy()
        new_matter_y.set_values(y_arr)
        return new_matter_y

    @classmethod
    def case_x(cls, c_x: Case, x0: int, x1: int, y0: int, y1: int) -> Case:
        new_case_x = c_x.copy()
        new_case_x.matter_list = [cls.matter_x(m_x) for m_x in c_x.matter_list]
        new_case_x.display_x0 = x0
        new_case_x.display_x1 = x1
        new_case_x.display_y0 = y0
        new_case_x.display_y1 = y1
        return new_case_x

    @classmethod
    def case_y(cls, c_y: Case, new_y_arr, x0: int, x1: int, y0: int, y1: int) -> Case:
        new_case_y = c_y.copy()
        new_case_y.matter_list = [cls.matter_y(c_y.matter_list[0], new_y_arr)]
        new_case_y.shape = new_y_arr.shape
        new_case_y.display_x0 = x0
        new_case_y.display_x1 = x1
        new_case_y.display_y0 = y0
        new_case_y.display_y1 = y1
        return new_case_y

    @classmethod
    def problem(cls, p: Problem) -> Problem:

        q = p.copy()
        q.train_x_list = []
        q.train_y_list = []
        q.test_x_list = []

        # check if fusion-able
        c_x: Case
        c_y: Case
        c_list = []
        for c_x, c_y in zip(p.train_x_list, p.train_y_list):
            x_arr = c_x.repr_values()
            y_arr = c_y.repr_values()
            new_y_arr, x0, x1, y0, y1, c = fusion_arr_train(x_arr, y_arr)
            # print(new_y_arr)
            # print(new_y_arr, x0, x1, y0, y1, c)
            q.train_x_list.append(cls.case_x(c_x, x0, x1, y0, y1))
            q.train_y_list.append(cls.case_y(c_y, new_y_arr, x0, x1, y0, y1))
            c_list.append(c)

        for c_x in p.test_x_list:
            x_arr = c_x.repr_values()
            c_suggest = c_list[0]
            x0, x1, y0, y1, c = fusion_arr_test(x_arr, c_suggest)
            q.test_x_list.append(cls.case_x(c_x, x0, x1, y0, y1))

        # pre_solve again
        is_pattern.set_is_pattern(q)
        is_periodic.set_is_periodic_row(q)
        is_periodic.set_is_periodic_col(q)
        is_symmetry.set_is_line_symmetry_row(q)
        is_symmetry.set_is_line_symmetry_col(q)
        return q


if __name__ == "__main__":
    pp = Problem.load(383, "eval")
    qq = Fusion.problem(pp)
    print(qq)
    print(qq.is_line_symmetry_row, qq.is_line_symmetry_col)

