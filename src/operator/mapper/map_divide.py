from typing import List
import numpy as np
from src.data import Problem, Case, Matter
from src.operator.solver.common.shape import is_division


class Divide:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter, d_row: np.int, d_col: np.int) -> List[Matter]:

        assert m.shape[0] % d_row == 0
        mrh = m.shape[0] // d_row
        assert mrh != 0

        assert m.shape[1] % d_col == 0
        mch = m.shape[1] // d_col
        assert mch != 0

        res_list = []
        for i in range(d_row):
            for j in range(d_col):
                new_matter = Matter(
                    m.values[mrh * i:mrh * (i + 1), mch * j:mch * (j + 1)], 0, 0, m.background_color, new=True
                )
                res_list.append(new_matter)
        return res_list

    @classmethod
    def case(cls, c: Case, d_row: int, d_col: int) -> Case:
        assert len(c.matter_list) == 1
        assert (d_row, d_col) != (1, 1)
        new_case = c.copy()
        new_case.matter_list = cls.matter(c.matter_list[0], d_row, d_col)
        new_case.shape = new_case.matter_list[0].shape
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        flag, d_row, d_col = is_division(p)
        assert flag
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, d_row, d_col) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, d_row, d_col) for c in p.test_x_list]
        return q
