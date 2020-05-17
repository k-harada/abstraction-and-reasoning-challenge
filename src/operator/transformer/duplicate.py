import numpy as np
from src.data import Problem, Case, Matter
from src.operator.transformer.arithmetic.n_color import NColor


def duplicate_array(x_arr, m_row, m_col):
    n_row, n_col = x_arr.shape
    res_arr = np.zeros((n_row * m_row, n_col * m_col), dtype=np.int)
    for i in range(m_row):
        for j in range(m_col):
            res_arr[i * n_row:(i + 1) * n_row, j * n_col:(j + 1) * n_col] = x_arr
    return res_arr


class DuplicateTransformer:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter, n_row, n_col):
        assert m.a is not None
        assert m.a > 0
        if m.b is None:
            assert max(m.a * n_row, m.a * n_col) <= 30
            new_matter: Matter = m.copy()
            new_matter.set_values(duplicate_array(m.values, m.a, m.a))
            new_matter.x0 = 0
            new_matter.y0 = 0
            return new_matter, m.a, m.a
        else:
            assert m.b > 0
            assert max(m.a * n_row, m.b * n_col) <= 30
            new_matter: Matter = m.copy()
            new_matter.set_values(duplicate_array(m.values, m.a, m.b))
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
    print(duplicate_array(x, 2, 3))
    pp = Problem.load(251, "eval")
    qq = NColor.problem(pp)
    rr = DuplicateTransformer.problem(qq)
    print(rr)
