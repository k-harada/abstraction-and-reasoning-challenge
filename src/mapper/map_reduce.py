from src.data import Problem
from src.mapper.case_map import *


def set_map_reduce(p: Problem, map_command: str, reduce_command: str) -> Problem:
    q: Problem
    q = p.copy()
    # map
    if map_command == "split_row_col":
        q.train_x_list = [split_row_col(x, p.d_row, p.d_col) for x in p.train_x_list]
        q.test_x_list = [split_row_col(x, p.d_row, p.d_col) for x in p.test_x_list]
    else:
        q.train_x_list = [eval(f'{map_command}(x)') for x in p.train_x_list]
        q.test_x_list = [eval(f'{map_command}(x)') for x in p.test_x_list]
    # reduce
    for case in q.train_x_list:
        case.reducer = reduce_command
    for case in q.test_x_list:
        case.reducer = reduce_command
    q.train_y_list = [x for x in p.train_y_list]
    return q
