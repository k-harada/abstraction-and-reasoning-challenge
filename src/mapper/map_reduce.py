from src.data import Problem
from .map_problem import run_map


def set_map_reduce(p: Problem, map_command: str, reduce_command: str) -> Problem:
    q: Problem
    # map
    q = run_map(p, map_command)
    # reduce
    for case in q.train_x_list:
        case.reducer = reduce_command
    for case in q.test_x_list:
        case.reducer = reduce_command
    q.train_y_list = [x for x in p.train_y_list]
    return q
