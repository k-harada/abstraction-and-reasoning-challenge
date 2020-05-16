from typing import List
import numpy as np
from src.data import Problem, Case, Matter


class MapColor:

    def __init__(self):
        pass

    @classmethod
    def array(cls, x_arr: np.array, background: np.int = 0) -> List[np.array]:
        """
        :param x_arr: np.array(int), array to split
        :param background: int, must be one of 0-9
        :return: List[np.array(np.int)]
        """

        res_list = []
        for c in range(10):
            if c == background:
                continue
            if (x_arr == c).sum() == 0:
                continue
            new_m_value = np.ones(x_arr.shape, dtype=np.int) * background
            new_m_value[x_arr == c] = c
            res_list.append((new_m_value, c))

        assert len(res_list) > 0
        return list(sorted(res_list, key=lambda res: (res[0] != background).sum()))

    @classmethod
    def matter(cls, m: Matter) -> List[Matter]:

        arr_list = cls.array(m.values, m.background_color)
        # avoid meaningless
        assert len(arr_list) >= 2
        res_list = []
        for arr in arr_list:
            m = Matter(arr[0], background_color=m.background_color, new=True)
            m.color = arr[1]
            res_list.append(m)

        return res_list

    @classmethod
    def case(cls, c: Case) -> Case:
        assert len(c.matter_list) == 1
        new_case = c.copy()
        new_case.matter_list = cls.matter(c.matter_list[0])
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    x = np.array([[2, 2, 3], [2, 0, 3]])
    print(MapColor.array(x))
