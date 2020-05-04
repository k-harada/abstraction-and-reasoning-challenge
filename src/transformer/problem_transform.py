import numpy as np
from src.data import Problem, Case
from src.transformer.case import *


def run_transform(p: Problem, command: str) -> Problem:
    q: Problem
    q = p.copy()
    q.train_x_list = [eval(f'{command}(x)') for x in p.train_x_list]
    q.test_x_list = [eval(f'{command}(x)') for x in p.test_x_list]
    q.train_y_list = [x for x in p.train_y_list]
    if command == "extend_shape":
        q.background_color = -1
    return q
