from src.data import Problem
from src.mapper.map_reduce import set_map_reduce
from src.transformer.problem_transform import run_transform
from src.solver.static import *
from src.solver.dynamic import *


mappers = [
    "identity", "color", "connect", "interior_dir4_zero", "mesh_split", "mesh_2", "mesh_align", "split_row_col"
]
reducers = ["simple", "fractal", "pick"]
transformers = [
    "connect_row", "connect_col", "connect_row_col", "connect_diagonal", "auto_fill_row_col",  "extend_shape",
    "transpose", "rev_row", "rev_col", "rot_180",
    "rot_rev_180", "rot_90", "rot_270", "trim_background", "paste_color", "n_cell", "arg_sort"
]
static_solvers = ["set_problem_color", "set_is_pattern", "set_problem_shape"]
dynamic_solvers = [
    "fill_pattern", "fit_replace_rule_33", "fit_replace_rule_33_all", "duplicate", "color_change",
    "reduce_bitwise"
]


class Runner:

    def __init__(self):
        pass

    @classmethod
    def set_map_reduce(cls, problem: Problem, map_command: str, reduce_command: str) -> Problem:
        if map_command in mappers and reduce_command in reducers:
            return set_map_reduce(problem, map_command, reduce_command)
        else:
            raise NotImplementedError

    @classmethod
    def run_transform(cls, problem: Problem, command: str) -> Problem:
        if command in transformers:
            return run_transform(problem, command)
        else:
            raise NotImplementedError

    @classmethod
    def pre_solve(cls, problem: Problem, command: str) -> None:
        if command in static_solvers:
            eval(f'{command}(problem)')
            return None
        else:
            raise NotImplementedError

    @classmethod
    def run_solve(cls, problem: Problem, command: str) -> Problem:
        if command in dynamic_solvers:
            return eval(f'{command}(problem)')
        else:
            raise NotImplementedError
