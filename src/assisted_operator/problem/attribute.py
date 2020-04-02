import numpy as np
from src.data import Problem
from src.assisted_operator.case import attribute as attr_case


def set_color_add(p: Problem, color_add: np.int8) -> Problem:
    q: Problem
    q = p.copy()
    q.color_add = color_add
    q.train_x_list = [attr_case.set_color_add(x, color_add) for x in p.train_x_list]
    q.test_x_list = [attr_case.set_color_add(x, color_add) for x in p.test_x_list]
    q.train_y_list = [x for x in p.train_y_list]
    return q
