import numpy as np
from src.data import Problem, Case, Matter
from src.solver.common.color import monotone_color, new_color


def set_problem_color(p: Problem) -> None:
    # only one color
    color_add = monotone_color(p)
    if color_add == -1:
        # one color added
        color_add = new_color(p)
    if color_add != -1:
        p.color_add = color_add
        c: Case
        m: Matter
        for c in p.train_x_list:
            c.color_add = color_add
            for m in c.matter_list:
                m.color_add = color_add
        for c in p.test_x_list:
            c.color_add = color_add
            for m in c.matter_list:
                m.color_add = color_add
    return None
