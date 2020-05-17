import numpy as np
from src.data import Problem, Case, Matter
from src.operator.transformer.arithmetic.n_color import NColor


def zoom_array(x_arr, m_row, m_col):
    return np.repeat(np.repeat(x_arr, m_row, axis=0), m_col, axis=1)


class ZoomTransformer:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter, n_row, n_col):
        assert m.a is not None
        assert m.a > 0
        if m.b is None:
            assert max(m.a * n_row, m.a * n_col) <= 30
            new_matter: Matter = m.copy()
            new_matter.set_values(zoom_array(m.values, m.a, m.a))
            new_matter.x0 = 0
            new_matter.y0 = 0
            return new_matter, m.a, m.a
        else:
            assert m.b > 0
            assert max(m.a * n_row, m.b * n_col) <= 30
            new_matter: Matter = m.copy()
            new_matter.set_values(zoom_array(m.values, m.a, m.b))
            new_matter.x0 = 0
            new_matter.y0 = 0
            return new_matter, m.a, m.b

    @classmethod
    def case(cls, c: Case) -> Case:
        assert len(c.matter_list) == 1
        new_case: Case = c.copy()
        new_matter, m_row, m_col = cls.matter(c.matter_list[0], c.shape[0], c.shape[1])
        new_case.matter_list = [new_matter]
        new_case.shape = c.shape[0] * m_row, c.shape[1] * m_col
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    x = np.array([[1, 2], [3, 4]])
    print(zoom_array(x, 2, 3))
    pp = Problem.load(325, "eval")
    qq = NColor.problem(pp)
    rr = ZoomTransformer.problem(qq)
    print(rr)
