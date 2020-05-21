from src.data import Problem, Case, Matter
from src.operator.solver.common.shape import is_same


class PasteColor:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter, full: bool) -> Case:
        if full:
            return m.paste_color_full()
        else:
            return m.paste_color()

    @classmethod
    def case(cls, c: Case, full: bool) -> Case:
        new_case: Case = c.copy()
        m: Matter
        new_case.matter_list = [m if m.is_mesh else cls.matter(m, full) for m in c.matter_list]
        return new_case

    @classmethod
    def problem(cls, p: Problem, full: bool) -> Problem:
        assert is_same(p)
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, full) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, full) for c in p.test_x_list]
        return q
