import numpy as np
from src.data import Problem, Case, Matter
from src.operator.mapper.split_mesh_normal import SplitMesh
from src.operator.transformer.arithmetic.n_cell import NCell
from src.operator.transformer.paste_color import PasteColor


class MaxKeeper:
    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case) -> Case:
        m: Matter
        new_case = c.copy()
        max_a = -1000000
        for m in c.matter_list:
            if m.is_mesh:
                continue
            assert m.a is not None
            max_a = max(m.a, max_a)
        new_case.matter_list = [m for m in c.matter_list if m.a == max_a or m.is_mesh]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    pp = Problem.load(58)
    qq = SplitMesh.problem(pp)
    rr = NCell.problem(qq)
    ss = MaxKeeper.problem(rr)
    tt = PasteColor.problem(ss, full=True)
    print(tt)
