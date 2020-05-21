import numpy as np
from src.data import Problem, Case, Matter
from src.operator.mapper.map_color_connect import MapColorConnect
from src.operator.transformer.reducer.collect_mesh import CollectMax


class RectangleKeeper:
    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter) -> bool:
        if m.is_filled_rectangle() and min(m.shape) >= 3:
            return True
        else:
            return False

    @classmethod
    def case(cls, c: Case) -> Case:
        m: Matter
        new_case = c.copy()
        new_case.matter_list = [m for m in c.matter_list if cls.matter(m)]
        assert len(new_case.matter_list) > 0
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    pp = Problem.load(11, "eval")
    qq = MapColorConnect.problem(pp, allow_diagonal=True)
    rr = RectangleKeeper.problem(qq)
    ss = CollectMax.problem(rr)
    print(ss)
