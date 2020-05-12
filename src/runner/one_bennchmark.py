from typing import List
import numpy as np
from src.data import Problem, Case, Matter


class BenchMark:

    def __init__(self):
        pass

    @classmethod
    def problem(cls, p: Problem) -> List[Problem]:
        res_list = []
        c: Case
        for c in p.train_y_list:
            q: Problem = p.copy()
            new_values = c.repr_values()
            q.train_x_list = []
            for _ in range(p.len_train):
                new_case = Case(new=True)
                new_case.initialize(new_values)
                q.train_x_list.append(new_case)
            q.test_x_list = []
            for _ in range(p.len_test):
                new_case = Case(new=True)
                new_case.initialize(new_values)
                q.test_x_list.append(new_case)
            res_list.append(q)
        return res_list
