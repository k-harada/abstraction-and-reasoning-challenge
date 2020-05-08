import numpy as np
from src.data import Problem, Case, Matter
from src.solver.common.shape import is_same


class PasteColor:
    """pick first matter and trim background"""
    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case, full: bool) -> Case:
        new_case: Case = c.copy()
        m: Matter
        if full:
            new_case.matter_list = [m.paste_color_full() for m in c.matter_list]
        else:
            new_case.matter_list = [m.paste_color() for m in c.matter_list]
        return new_case

    @classmethod
    def problem(cls, p: Problem, full: bool) -> Problem:
        assert is_same(p)
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, full) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, full) for c in p.test_x_list]
        return q
