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
        res_list = []
        for arr in arr_list:
            x_arr = arr[0]
            # trim
            x_sum = (x_arr != m.background_color).sum(axis=1)
            y_sum = (x_arr != m.background_color).sum(axis=0)

            min_x = min([i for i in range(x_arr.shape[0]) if x_sum[i]])
            max_x = max([i for i in range(x_arr.shape[0]) if x_sum[i]])
            min_y = min([i for i in range(x_arr.shape[1]) if y_sum[i]])
            max_y = max([i for i in range(x_arr.shape[1]) if y_sum[i]])

            new_values = x_arr[min_x:max_x + 1, min_y:max_y + 1].copy()
            m = Matter(new_values, min_x, min_y, background_color=m.background_color, new=True)
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
