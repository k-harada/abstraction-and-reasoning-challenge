from collections import deque
import numpy as np
from src.data import Problem, Case, Matter
from src.solver.common.shape import is_same


class Interior:
    """fill interior with Case's color_add"""
    def __init__(self):
        pass

    @classmethod
    def array(cls, x_arr: np.array) -> np.array:
        """
        find interiors of x_arr that is background
        :param x_arr: np.array(bool or int), if int, background is 0
        :return: np.array(bool)
        """
        res = np.ones(x_arr.shape, dtype=np.bool)
        assert x_arr.shape[0] > 0
        assert x_arr.shape[1] > 0

        queue = deque()

        # from boundary
        for i in range(x_arr.shape[0]):
            j = 0
            res[i, j] = False
            if not x_arr[i, j]:
                queue.append((i, j))
            j = x_arr.shape[1] - 1
            res[i, j] = False
            if not x_arr[i, j]:
                queue.append((i, j))

        for j in range(x_arr.shape[1]):
            i = 0
            res[i, j] = False
            if not x_arr[i, j]:
                queue.append((i, j))
            i = x_arr.shape[0] - 1
            res[i, j] = False
            if not x_arr[i, j]:
                queue.append((i, j))

        for i in range(x_arr.shape[0]):
            for j in range(x_arr.shape[1]):
                if x_arr[i, j]:
                    res[i, j] = False

        while len(queue) > 0:
            i0, j0 = queue.popleft()
            i1, j1 = min(i0 + 1, x_arr.shape[0] - 1), j0
            if res[i1, j1]:
                res[i1, j1] = False
                queue.append((i1, j1))
            i1, j1 = max(i0 - 1, 0), j0
            if res[i1, j1]:
                res[i1, j1] = False
                queue.append((i1, j1))
            i1, j1 = i0, min(j0 + 1, x_arr.shape[1] - 1)
            if res[i1, j1]:
                res[i1, j1] = False
                queue.append((i1, j1))
            i1, j1 = i0, max(j0 - 1, 0)
            if res[i1, j1]:
                res[i1, j1] = False
                queue.append((i1, j1))

        return res

    @classmethod
    def matter(cls, m: Matter, color_add: int) -> Matter:
        res_bool = cls.array(m.values)
        new_values = m.values.copy()

        new_values[res_bool] = color_add

        new_m: Matter = m.copy()
        new_m.set_values(new_values)

        return new_m

    @classmethod
    def case(cls, c: Case) -> Case:
        new_case = c.copy()
        m: Matter
        if c.color_add is not None:
            color_add = c.color_add
        else:
            color_add = c.max_color()
        new_case.matter_list = [cls.matter(m, color_add) for m in c.matter_list]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        assert is_same(p)
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    x = np.zeros((5, 5))
    x[1, :] = 1
    x[4, :] = 1
    x[:, 1] = 1
    x[:, 3] = 1
    print(Interior.array(x))
