import numpy as np
from src.data import Problem, Case, Matter
from src.common.trivial_reducer import trivial_reducer
from src.operator.solver.common.shape import is_same


class DropDuplicates:

    def __init__(self):
        pass

    @classmethod
    def array(cls, x_arr) -> np.array:

        # drop_row
        keep_rows = [0]
        assert x_arr.shape[0] > 0 and x_arr.shape[1] > 0
        for i in range(x_arr.shape[0]):
            if (x_arr[i, :] != x_arr[keep_rows[-1], :]).max():
                keep_rows.append(i)
        y_arr = np.zeros((len(keep_rows), x_arr.shape[1]), dtype=int)
        # print(keep_rows)
        for i, xi in enumerate(keep_rows):
            y_arr[i, :] = x_arr[xi, :]
        # drop_col
        keep_cols = [0]
        assert y_arr.shape[0] > 0 and y_arr.shape[1] > 0
        for j in range(y_arr.shape[1]):
            if (y_arr[:, j] != y_arr[:, keep_cols[-1]]).max():
                keep_cols.append(j)
        # print(keep_cols)
        z_arr = np.zeros((y_arr.shape[0], len(keep_cols)), dtype=int)
        for j, yj in enumerate(keep_cols):
            z_arr[:, j] = y_arr[:, yj]

        return z_arr

    @classmethod
    def case(cls, c: Case) -> Case:
        new_case = c.copy()
        x_arr = trivial_reducer(c)
        # print(x_arr)
        new_values = cls.array(x_arr)
        new_case.matter_list = [Matter(new_values, background_color=c.background_color, new=True)]
        new_case.shape = new_values.shape
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        assert not is_same(p)
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    x = np.array([[1, 2, 1, 1], [3, 4, 2, 2], [3, 4, 2, 2]])
    print(DropDuplicates.array(x))
    pp = Problem.load(314, "eval")
    qq = DropDuplicates.problem(pp)
    print(qq)
