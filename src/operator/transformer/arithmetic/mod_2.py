import numpy as np
from src.data import Problem, Case, Matter


class Mod2:
    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case) -> Case:
        m: Matter
        new_case = c.copy()
        new_case.matter_list = [m.deepcopy() for m in c.matter_list]
        for m in new_case.matter_list:
            if m.a is None:
                pass
            else:
                m.a = m.a % 2
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
