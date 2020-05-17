import numpy as np
from src.data import Problem, Case, Matter
from src.operator.mapper.map_connect import MapConnect


class RectangleHole:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter, hole_type: str) -> Matter:
        if m.is_filled_rectangle() and min(m.shape) >= 3:
            new_matter = m.copy()
            new_values = m.values.copy()
            if hole_type == "simple":
                new_values[1:-1, 1:-1] = m.background_color
            elif hole_type == "mesh":
                new_values[1:-1:2, 1:-1:2] = m.background_color
            elif hole_type == "mesh_x":
                new_values[1:-1:2, 1:-1:2] = m.background_color
                new_values[2:-1:2, 2:-1:2] = m.background_color
            else:
                raise NotImplementedError
            new_matter.set_values(new_values)
            return new_matter
        else:
            return m

    @classmethod
    def case(cls, c: Case, hole_type: str) -> Case:
        new_case: Case = c.copy()
        m: Matter
        new_case.matter_list = [cls.matter(m, hole_type) for m in c.matter_list]
        return new_case

    @classmethod
    def problem(cls, p: Problem, hole_type: str) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, hole_type) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, hole_type) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    xx = np.ones((9, 9), dtype=int)
    yy1 = xx.copy()
    yy1[1:-1, 1:-1] = 0
    print(yy1)
    yy2 = xx.copy()
    yy2[1:-1:2, 1:-1:2] = 0
    print(yy2)
    yy3 = xx.copy()
    yy3[1:-1:2, 1:-1:2] = 0
    yy3[2:-1:2, 2:-1:2] = 0
    print(yy3)
    pp = Problem.load(84)
    qq = MapConnect.problem(pp, allow_diagonal=True)
    rr = RectangleHole.problem(qq, "mesh")
    print(rr)
