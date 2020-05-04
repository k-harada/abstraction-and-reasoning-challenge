from src.data import Problem
from src.transformer.case import *
from .interior.case import interior_dir4_zero
from .fill_rectangle.case import fill_rectangle
from .diff_color.case import diff_color


def run_transform(p: Problem, command: str) -> Problem:
    q: Problem
    q = p.copy()
    if command == "diff_color":
        q.train_x_list = [diff_color(c1, c2) for c1, c2 in zip(p.train_x_list, p.train_x_initial_list)]
        q.test_x_list = [diff_color(c1, c2) for c1, c2 in zip(p.test_x_list, p.test_x_initial_list)]
        q.train_y_list = [x for x in p.train_y_list]
    else:
        q.train_x_list = [eval(f'{command}(x)') for x in p.train_x_list]
        q.test_x_list = [eval(f'{command}(x)') for x in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    return q
