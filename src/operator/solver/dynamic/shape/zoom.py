import numpy as np
from src.data import Problem, Case, Matter
from src.operator.solver.common.shape import is_multiple, is_constant


def zoom_array(x_arr, m_row, m_col):
    return np.repeat(np.repeat(x_arr, m_row, axis=0), m_col, axis=1)


class ZoomSolver:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter, m_row, m_col) -> Matter:
        new_matter: Matter = m.copy()
        new_matter.set_values(zoom_array(m.values, m_row, m_col))
        new_matter.x0 = m.x0 * m_row
        new_matter.y0 = m.y0 * m_col
        return new_matter

    @classmethod
    def case_m(cls, c: Case, m_row, m_col) -> Case:
        new_case: Case = c.copy()
        new_case.matter_list = [cls.matter(m, m_row, m_col) for m in c.matter_list]
        new_case.shape = c.shape[0] * m_row, c.shape[1] * m_col
        return new_case

    @classmethod
    def case_n(cls, c: Case, n_row, n_col) -> Case:
        assert n_row % c.shape[0] == 0
        assert n_col % c.shape[1] == 0
        m_row = n_row // c.shape[0]
        m_col = n_col // c.shape[1]
        new_case: Case = c.copy()
        new_case.matter_list = [cls.matter(m, m_row, m_col) for m in c.matter_list]
        new_case.shape = c.shape[0] * m_row, c.shape[1] * m_col
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        flag, m_row, m_col = is_multiple(p)
        if flag:
            q.train_x_list = [cls.case_m(c, m_row, m_col) for c in p.train_x_list]
            q.test_x_list = [cls.case_m(c, m_row, m_col) for c in p.test_x_list]
            return q
        flag, n_row, n_col = is_constant(p)
        if flag:
            q.train_x_list = [cls.case_n(c, n_row, n_col) for c in p.train_x_list]
            q.test_x_list = [cls.case_n(c, n_row, n_col) for c in p.test_x_list]
            return q

        raise AssertionError


if __name__ == "__main__":

    x = np.array([[1, 2], [3, 4]])
    print(zoom_array(x, 2, 3))
    pp = Problem.load(222)
    qq = ZoomSolver.problem(pp)
    print(qq)
