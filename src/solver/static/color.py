import numpy as np
from src.data import Problem, Case, Matter
from src.solver.common.color import monotone_color, new_color


def define_color(p: Problem) -> int:
    # only one color
    color_add = monotone_color(p)
    if color_add != -1:
        return color_add
    color_add_list = new_color(p)
    if len(color_add_list) == 1:
        return color_add_list[0]
    else:
        return -1


def set_problem_color(p: Problem) -> None:

    color_add = define_color(p)

    if color_add != -1:
        p.color_add = color_add
        c: Case
        m: Matter
        for c in p.train_x_list:
            c.color_add = color_add
        for c in p.test_x_list:
            c.color_add = color_add
    return None
