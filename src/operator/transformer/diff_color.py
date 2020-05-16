from src.data import Problem, Case, Matter
from src.operator.solver.common.shape import is_same
from src.common.trivial_reducer import trivial_reducer


class DiffColor:
    """pick first matter and trim background"""
    def __init__(self):
        pass

    @classmethod
    def case_21(cls, c: Case, compare_c: Case) -> Case:
        assert c.color_add is not None

        new_values = trivial_reducer(c)
        compare_values = trivial_reducer(compare_c)

        assert new_values.shape == compare_values.shape
        new_values[new_values != compare_values] = c.color_add

        new_case: Case = c.copy()
        new_case.matter_list = [Matter(new_values, background_color=c.background_color, new=True)]

        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        assert is_same(p)
        q: Problem = p.copy()
        q.train_x_list = [cls.case_21(c1, c2) for c1, c2 in zip(p.train_x_list, p.train_x_initial_list)]
        q.test_x_list = [cls.case_21(c1, c2) for c1, c2 in zip(p.test_x_list, p.test_x_initial_list)]
        return q
