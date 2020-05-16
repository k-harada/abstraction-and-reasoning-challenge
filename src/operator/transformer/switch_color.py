import numpy as np
from src.data import Problem, Case, Matter


class SwitchColor:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter) -> Matter:
        assert m.n_color() <= 2
        if m.is_mesh:
            return m
        elif m.n_color() == 0:
            return m
        elif m.n_color() == 1:
            color_count = m.color_count()
            for c in range(10):
                if color_count[c] > 0 and c != m.background_color:
                    base_color = c
            new_matter: Matter = m.copy()
            new_values = m.background_color * np.ones(m.shape, dtype=np.int)
            new_values[m.values == m.background_color] = base_color
            new_matter.set_values(new_values)
            return new_matter
        else:  # m.n_color() == 2
            color_count = m.color_count()
            switch = []
            for c in range(10):
                if color_count[c] > 0 and c != m.background_color:
                    switch.append(c)
            new_matter: Matter = m.copy()
            new_values = m.background_color * np.ones(m.shape, dtype=np.int)
            new_values[m.values == switch[0]] = switch[1]
            new_values[m.values == switch[1]] = switch[0]
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
