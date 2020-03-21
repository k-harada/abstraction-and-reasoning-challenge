from src.data import Problem
from src.operator.case.transform import *


def run_transform(p: Problem, command: str) -> Problem:
    q: Problem
    q = p.copy()
    q.train_x_list = [eval(f'{command}(x)') for x in p.train_x_list]
    q.test_x_list = [eval(f'{command}(x)') for x in p.test_x_list]
    q.train_y_list = [x for x in p.train_y_list]
    return q
