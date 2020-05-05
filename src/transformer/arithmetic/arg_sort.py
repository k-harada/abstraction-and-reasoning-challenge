import numpy as np
from src.data import Problem, Case, Matter


class ArgSort:
    """pick first matter and trim background"""
    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case) -> Case:
        m: Matter
        new_case = c.copy()
        a_list = [m.a for m in c.matter_list if m.a is not None]
        assert len(a_list) == len(c.matter_list)
        a_arg_sort = np.argsort(a_list).astype(np.int)
        a_arg_sort_inv = [0] * len(a_arg_sort)
        color = 0
        value_map = dict()
        for i in a_arg_sort:
            if color == c.background_color:
                color += 1
            if a_list[i] not in value_map.keys():
                value_map[a_list[i]] = color
                color += 1
        for i, a in enumerate(a_list):
            a_arg_sort_inv[i] = value_map[a]
        new_case.matter_list = [m.deepcopy() for m in c.matter_list]
        for m, new_a in zip(new_case.matter_list, a_arg_sort_inv):
            m.a = new_a
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
