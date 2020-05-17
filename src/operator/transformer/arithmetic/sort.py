import numpy as np
from src.data import Problem, Case, Matter


class Sort:
    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case, descending: bool = False) -> Case:
        new_case = c.copy()
        for m in c.matter_list:
            assert m.a is not None
        if descending:
            new_case.matter_list = list(sorted(c.matter_list, key=lambda x: -x.a))
        else:
            new_case.matter_list = list(sorted(c.matter_list, key=lambda x: x.a))
        return new_case

    @classmethod
    def problem(cls, p: Problem, descending: bool = False) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, descending) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, descending) for c in p.test_x_list]
        return q
