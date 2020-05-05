import numpy as np
from src.data import Problem, Case, Matter


class ConnectRow:

    def __init__(self):
        pass

    @classmethod
    def array(cls, x_arr: np.array, background: np.int = 0) -> np.array:
        """
        :param x_arr: np.array(np.int)
        :param background: np.int, must be one of 0-9
        :return: new_array connected, colors over color, map-apply-reduce if necessary
        """
        new_x_arr = x_arr.copy()
        for c in range(10):
            if c == background:
                continue
            # row
            for i in range(x_arr.shape[0]):
                if c in x_arr[i, :]:
                    j0 = min([j for j in range(x_arr.shape[1]) if x_arr[i, j] == c])
                    j1 = max([j for j in range(x_arr.shape[1]) if x_arr[i, j] == c])
                    if j0 < j1:
                        new_x_arr[i, j0:j1 + 1] = c

        return new_x_arr

    @classmethod
    def matter(cls, m: Matter) -> Matter:
        new_values = cls.array(m.values, m.background_color)
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
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
