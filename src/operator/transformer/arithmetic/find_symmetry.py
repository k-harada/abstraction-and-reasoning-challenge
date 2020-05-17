import numpy as np
from src.data import Problem, Case, Matter
from src.operator.mapper.map_connect import MapConnect
from src.operator.transformer.reducer.trim_background import TrimBackground


def find_symmetry(x_arr) -> np.int:
    # assume trimmed
    # row
    res_row = 0
    for i in range(x_arr.shape[0] // 2):
        res_row += (x_arr[i, :] != x_arr[x_arr.shape[0] - 1 - i, :]).sum()
    # col
    res_col = 0
    for j in range(x_arr.shape[1] // 2):
        res_col += (x_arr[:, j] != x_arr[:, x_arr.shape[1] - 1 - j]).sum()
    res = 0
    if res_row == 0:
        res += 1
    if res_col == 0:
        res += 2
    # print(res)
    return res


class SymmetryFinder:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter) -> bool:
        new_matter = m.deepcopy()
        new_matter.a = find_symmetry(m.values)
        return new_matter

    @classmethod
    def case(cls, c: Case) -> Case:
        assert len(c.matter_list) > 1
        new_case: Case = c.copy()
        new_case.matter_list = list(sorted([cls.matter(m) for m in c.matter_list], key=lambda x: -x.a))
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    pp = Problem.load(327, "eval")
    qq = MapConnect.problem(pp, allow_diagonal=True)
    rr = SymmetryFinder.problem(qq)
    ss = TrimBackground.problem(rr)
    print(ss)
