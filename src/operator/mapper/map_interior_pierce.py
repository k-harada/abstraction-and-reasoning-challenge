from collections import deque
from typing import List
import numpy as np
from src.data import Problem, Case, Matter
from src.operator.mapper.map_interior import MapInterior


def neighbors(p, r, c, allow_diagonal=True):
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


class MapInteriorPierce:

    def __init__(self):
        pass

    @classmethod
    def array(cls, x_arr: np.array, allow_diagonal: bool, background: np.int = 0) -> List[np.array]:
        """
        :param x_arr: np.array(int), array to split
        :param allow_diagonal: bool, whether or not regard diagonal connected
        :param background: int, must be one of 0-9
        :return: List[np.array(np.int)]
        """
        r, c = x_arr.shape
        con_map = np.zeros((r, c), dtype=np.int)
        queue = deque()
        for i in [0, r - 1]:
            for j in range(c):
                if x_arr[i, j] == background:
                    con_map[i, j] = -1
                    queue.append((i, j))
                else:
                    con_map[i, j] = 1
        for i in range(1, r - 1):
            for j in [0, c - 1]:
                if x_arr[i, j] == background:
                    queue.append((i, j))
                else:
                    con_map[i, j] = 1
        while len(queue) > 0:
            p = queue.popleft()
            for q in neighbors(p, r, c, allow_diagonal):
                qi, qj = q
                if x_arr[qi, qj] == background:
                    if con_map[qi, qj] == 0:
                        con_map[qi, qj] = -1
                        queue.append((qi, qj))
                elif con_map[qi, qj] == 0:
                    con_map[qi, qj] = 1

        x_arr_c = x_arr.copy()
        x_arr_c[con_map <= 0] = background
        return MapInterior.array(x_arr_c, allow_diagonal, background)

    @classmethod
    def matter(cls, m: Matter, allow_diagonal: bool, case_background, boundary_none) -> List[Matter]:
        arr_list = cls.array(m.values, allow_diagonal, m.background_color)
        # avoid meaningless
        assert len(arr_list) >= 2

        res_list = []

        for i, x_arr in enumerate(arr_list):
            if i > 0:
                # trim
                x_sum = (x_arr != 0).sum(axis=1)
                y_sum = (x_arr != 0).sum(axis=0)
                min_x = min([i for i in range(x_arr.shape[0]) if x_sum[i]])
                max_x = max([i for i in range(x_arr.shape[0]) if x_sum[i]])
                min_y = min([i for i in range(x_arr.shape[1]) if y_sum[i]])
                max_y = max([i for i in range(x_arr.shape[1]) if y_sum[i]])
                new_values = x_arr[min_x:max_x + 1, min_y:max_y + 1].copy()
                # print(new_values)
                if case_background == 0:
                    m_values = 1 - new_values
                    new_m: Matter = Matter(m_values, min_x, min_y, background_color=1, new=True)
                else:
                    new_m: Matter = Matter(new_values * case_background, min_x, min_y, background_color=0, new=True)
                if min_x > 0 and max_x < m.shape[0] - 1 and min_y > 0 and max_y < m.shape[1] - 1:
                    new_m.a = 1
                else:
                    if not boundary_none:
                        new_m.a = 0
            else:
                new_values = x_arr.copy()
                new_m: Matter = Matter(new_values, 0, 0, background_color=m.background_color, new=True)
                # new_m.a = None
            res_list.append(new_m)

        return res_list

    @classmethod
    def case(cls, c: Case, allow_diagonal: bool, boundary_none: bool) -> Case:
        assert len(c.matter_list) == 1
        new_case = c.copy()
        new_case.matter_list = cls.matter(c.matter_list[0], allow_diagonal, c.background_color, boundary_none)
        # print(len(new_case.matter_list))
        return new_case

    @classmethod
    def problem(cls, p: Problem, allow_diagonal: bool = False, boundary_none: bool = True) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, allow_diagonal, boundary_none) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, allow_diagonal, boundary_none) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    xx = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
    print(MapInteriorPierce.array(xx, False))
    print(MapInteriorPierce.array(xx, True))
    xx = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 1]])
    print(MapInteriorPierce.array(xx, False))
    print(MapInteriorPierce.array(xx, True))

    from src.operator.solver.dynamic.color.auto_paste_a import AutoPasteA
    pp = Problem.load(119)
    qq = MapInteriorPierce.problem(pp)
    rr = AutoPasteA.problem(qq)
    print(rr.eval_distance())
