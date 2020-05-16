from src.data import Problem, Case, Matter
from src.operator.solver.common.shape import is_same


class FillRectangle:
    """paste background with case's color_add"""
    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter, color_add: int) -> Matter:
        new_matter: Matter = m.copy()
        new_values = m.values.copy()
        new_values[new_values == m.background_color] = color_add
        new_matter.set_values(new_values)
        return new_matter

    @classmethod
    def case(cls, c: Case) -> Case:
        assert c.color_add is not None
        new_case: Case = c.copy()
        new_case.matter_list = [cls.matter(m, c.color_add) for m in c.matter_list]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        assert is_same(p)
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
