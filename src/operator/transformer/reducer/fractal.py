import numpy as np
from src.data import Problem, Case, Matter


class Fractal:

    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case) -> Case:

        res_arr = c.repr_fractal_values()

        new_case: Case = c.copy()
        new_case.shape = res_arr.shape
        new_case.matter_list = [Matter(res_arr, background_color=c.background_color, new=True)]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
