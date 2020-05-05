from collections import deque
from typing import List
import numpy as np
from src.data import Problem, Case, Matter


class MapConnect:

    def __init__(self):
        pass

    @classmethod
    def neighbors(cls, p, r, c, allow_diagonal=True):
        x, y = p
        res_list = []
        if x > 0:
            res_list.append((x - 1, y))
        if x < r - 1:
            res_list.append((x + 1, y))
        if y > 0:
            res_list.append((x, y - 1))
        if y < c - 1:
            res_list.append((x, y + 1))
        # diagonal
        if allow_diagonal:
            if x > 0 and y > 0:
                res_list.append((x - 1, y - 1))
            if x > 0 and y < c - 1:
                res_list.append((x - 1, y + 1))
            if x < r - 1 and y > 0:
                res_list.append((x + 1, y - 1))
            if x < r - 1 and y < c - 1:
                res_list.append((x + 1, y + 1))

        return res_list

    @classmethod
    def array(cls, x_arr: np.array, allow_diagonal: bool = True, background: np.int = 0) -> List[np.array]:
        """
        :param x_arr: np.array(int), array to split
        :param allow_diagonal: bool, whether or not regard diagonal connected
        :param background: int, must be one of 0-9
        :return: List[np.array(np.int)]
        """
        res_list = []
        r, c = x_arr.shape
        con_map = np.zeros((r, c), dtype=np.int)
        ind = 0
        for i in range(r):
            for j in range(c):
                if x_arr[i, j] != background and con_map[i, j] == 0:
                    # start search
                    ind += 1
                    queue = deque()
                    queue.append((i, j))
                    con_map[i, j] = ind
                    while len(queue) > 0:
                        p = queue.popleft()
                        for q in cls.neighbors(p, r, c, allow_diagonal):
                            qi, qj = q
                            if x_arr[qi, qj] != background and con_map[qi, qj] == 0:
                                con_map[qi, qj] = ind
                                queue.append((qi, qj))

        # trivial case
        if ind == 0:
            return [x_arr.copy()]

        for s in range(ind):
            x_arr_s = x_arr.copy()
            x_arr_s[con_map != s + 1] = background
            res_list.append(x_arr_s)

        return list(sorted(res_list, key=lambda res: -(res != background).sum()))

    @classmethod
    def matter(cls, m: Matter, allow_diagonal: bool) -> List[Matter]:
        arr_list = cls.array(m.values, allow_diagonal, m.background_color)
        # avoid meaningless
        assert len(arr_list) >= 2

        res_list = []

        for x_arr in arr_list:
            # trim
            x_sum = (x_arr != m.background_color).sum(axis=1)
            y_sum = (x_arr != m.background_color).sum(axis=0)

            min_x = min([i for i in range(x_arr.shape[0]) if x_sum[i]])
            max_x = max([i for i in range(x_arr.shape[0]) if x_sum[i]])
            min_y = min([i for i in range(x_arr.shape[1]) if y_sum[i]])
            max_y = max([i for i in range(x_arr.shape[1]) if y_sum[i]])

            new_values = x_arr[min_x:max_x + 1, min_y:max_y + 1].copy()

            res_list.append(Matter(new_values, min_x, min_y, background_color=m.background_color, new=True))

        return res_list

    @classmethod
    def case(cls, c: Case, allow_diagonal: bool) -> Case:
        assert len(c.matter_list) == 1
        new_case = c.copy()
        new_case.matter_list = cls.matter(c.matter_list[0], allow_diagonal)
        # a <- n_cell by default
        for m in new_case.matter_list:
            m.a = m.n_cell()
        return new_case

    @classmethod
    def problem(cls, p: Problem, allow_diagonal: bool) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, allow_diagonal) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, allow_diagonal) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    xx = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
    print(MapConnect.array(xx, False))
    print(MapConnect.array(xx, True))
    xx = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 1]])
    print(MapConnect.array(xx, False))
    print(MapConnect.array(xx, True))
