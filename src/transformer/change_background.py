import numpy as np
from src.data import Problem, Case, Matter


class ChangeBackground:
    """Max color of case -> background"""

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter, new_background: np.int) -> Matter:
        new_matter: Matter = m.copy()
        new_matter.background_color = new_background
        new_values = m.values.copy()
        new_matter.set_values(new_values)
        return new_matter

    @classmethod
    def case(cls, c: Case) -> Case:
        new_case: Case = c.copy()
        new_background = c.max_color()
        m: Matter
        new_case.matter_list = [cls.matter(m, new_background) for m in c.matter_list]
        new_case.background_color = new_background
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
