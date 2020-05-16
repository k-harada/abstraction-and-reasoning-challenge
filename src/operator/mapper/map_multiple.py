from src.data import Problem, Case, Matter
from src.operator.solver.common.shape import is_multiple


class Multiple:

    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case, m_row: int, m_col: int) -> Case:
        new_case: Case = c.copy()
        new_case.matter_list = []
        m: Matter = c.matter_list[0]
        for i in range(m_row):
            for j in range(m_col):
                x0 = i * m.shape[0]
                y0 = j * m.shape[1]
                new_matter: Matter = m.deepcopy()
                new_matter.x0 = x0
                new_matter.y0 = y0
                new_case.matter_list.append(new_matter)
        new_case.shape = m.shape[0] * m_row, m.shape[1] * m_col
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        flag, m_row, m_col = is_multiple(p)
        assert flag
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, m_row, m_col) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, m_row, m_col) for c in p.test_x_list]
        return q
