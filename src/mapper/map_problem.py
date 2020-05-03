from src.data import Problem
from src.mapper.case_map import *


# initial map
def run_map(p: Problem, command: str) -> Problem:
    q: Problem
    q = p.copy()
    if command == "split_row_col":
        q.train_x_list = [split_row_col(x, p.d_row, p.d_col) for x in p.train_x_list]
        q.test_x_list = [split_row_col(x, p.d_row, p.d_col) for x in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    else:
        q.train_x_list = [eval(f'{command}(x)') for x in p.train_x_list]
        q.test_x_list = [eval(f'{command}(x)') for x in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    return q
