import numpy as np
from src.data import Problem, Case, Matter


class MinMax:
    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case) -> Case:
        m: Matter
        a_not_none = [m.a for m in c.matter_list if m.a is not None]
        assert len(a_not_none) > 0
        max_a = max(a_not_none)
        min_a = min(a_not_none)
        # print(max_a, min_a)
        new_case = c.copy()
        new_case.matter_list = [m.deepcopy() for m in c.matter_list]
        for m in new_case.matter_list:
            if m.a is not None:
                # print(m.a)
                if m.a == min_a:
                    m.a = 1
                elif m.a == max_a:
                    m.a = 2
                else:
                    m.a = 0
            else:
                pass
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
