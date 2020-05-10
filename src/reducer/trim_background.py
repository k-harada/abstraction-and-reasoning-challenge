import numpy as np
from src.data import Problem, Case, Matter
from src.solver.common.shape import is_same


class TrimBackground:
    """pick first matter and trim background"""
    def __init__(self):
        pass

    @classmethod
    def array(cls, x_arr, background=0):
        """
        :param x_arr: np.array(int), array to trim
        :param background: int, must be one of 0-9
        :return: List[np.array(np.int)]
        """

        x_sum = (x_arr != background).sum(axis=1)
        y_sum = (x_arr != background).sum(axis=0)

        if x_sum.sum() == 0:
            return x_arr.copy(), (0, 0)

        min_x = min([i for i in range(x_arr.shape[0]) if x_sum[i]])
        max_x = max([i for i in range(x_arr.shape[0]) if x_sum[i]])
        min_y = min([i for i in range(x_arr.shape[1]) if y_sum[i]])
        max_y = max([i for i in range(x_arr.shape[1]) if y_sum[i]])

        new_values = x_arr[min_x:max_x + 1, min_y:max_y + 1].copy()
        return new_values, (0, 0)

    @classmethod
    def matter(cls, m: Matter) -> Matter:
        new_values, xy0 = cls.array(m.values, m.background_color)
        return Matter(new_values, 0, 0, m.background_color, new=True)

    @classmethod
    def case(cls, c: Case) -> Case:
        new_case = c.copy()
        new_case.matter_list = [cls.matter(c.matter_list[0])]
        new_case.shape = new_case.matter_list[0].shape
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    x = np.array([[3, 2, 0], [0, 1, 0], [0, 0, 0]])
    print(TrimBackground.array(x))
