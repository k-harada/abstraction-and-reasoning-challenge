import numpy as np
from src.data import Problem, Case, Matter


class KeepMaxColor:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter) -> Matter:
        new_matter: Matter = m.copy()
        new_values = m.background_color * np.ones(m.shape, dtype=np.int)
        keep_color = m.max_color()
        new_values[m.values == keep_color] = keep_color
        new_matter.set_values(new_values)
        return new_matter

    @classmethod
    def case(cls, c: Case) -> Case:
        new_case: Case = c.copy()
        m: Matter
        new_case.matter_list = [cls.matter(m) for m in c.matter_list]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
