import numpy as np
from src.data import Problem, Case, Matter


class NCell:
    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case, keep_none: bool) -> Case:
        m: Matter
        new_case = c.copy()
        new_case.matter_list = [m.deepcopy() for m in c.matter_list]
        none_cnt = 0
        for m in new_case.matter_list:
            if m.a is None and keep_none:
                none_cnt += 1
            else:
                m.a = m.n_cell()

        if none_cnt:
            pass
        else:
            new_case.matter_list = list(sorted(new_case.matter_list, key=lambda x: -x.a))
        return new_case

    @classmethod
    def problem(cls, p: Problem, keep_none: bool = False) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, keep_none) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, keep_none) for c in p.test_x_list]
        return q
