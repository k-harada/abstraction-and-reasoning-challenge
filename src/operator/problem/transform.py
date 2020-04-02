import numpy as np
from src.data import Problem
from src.operator.case.transform import *
from src.assisted_operator.problem import attribute as attr_prob


def run_transform(p: Problem, command: str) -> Problem:
    if command == "set_problem_color":
        return set_problem_color(p)
    else:
        q: Problem
        q = p.copy()
        q.train_x_list = [eval(f'{command}(x)') for x in p.train_x_list]
        q.test_x_list = [eval(f'{command}(x)') for x in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
        return q


def set_problem_color(p: Problem) -> Problem:
    color_count = np.array([case.color_count for case in p.train_y_list]).sum(axis=0)
    # ignore background
    color_count[p.background_color] = 0
    # only color other than background
    if (color_count > 0).sum() == 1:
        color_add = color_count.argmax()
    elif False:
        # TODO new color appear
        pass
    else:
        # maximum color in y
        color_add = color_count.argmax()
    q: Problem
    q = attr_prob.set_color_add(p, color_add=color_add)
    return q
