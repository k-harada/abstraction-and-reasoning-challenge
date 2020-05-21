from collections import deque
import numpy as np
from src.data import Problem, Case, Matter
from src.operator.solver.common.color import only_color


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


def count_hole(x_arr: np.array, background: int) -> int:
    res_arr = background * np.ones((x_arr.shape[0] + 2, x_arr.shape[1] + 2), dtype=int)
    res_arr[1:-1, 1:-1] = x_arr
    n_holes = -1
    for i in range(res_arr.shape[0]):
        for j in range(res_arr.shape[1]):
            if res_arr[i, j] != background:
                continue
            queue = deque([(i, j)])
            n_holes += 1
            while len(queue) > 0:
                x0, y0 = queue.popleft()
                res_list = neighbors((x0, y0), res_arr.shape[0], res_arr.shape[1], allow_diagonal=False)
                for x1, y1 in res_list:
                    if res_arr[x1, y1] == background:
                        res_arr[x1, y1] = background + 1
                        queue.append((x1, y1))

    return n_holes


class CountHole:
    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter) -> Matter:
        m: Matter
        new_matter = m.deepcopy()
        new_matter.a = count_hole(m.values, m.background_color)
        return new_matter

    @classmethod
    def case(cls, c: Case) -> Case:
        m: Matter
        new_case = c.copy()
        new_case.matter_list = [cls.matter(m) for m in c.matter_list]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    xx = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    print(count_hole(xx, 0))
    xx = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]])
    print(count_hole(xx, 0))
    xx = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 1, 1], [1, 0, 1]])
    print(count_hole(xx, 0))
