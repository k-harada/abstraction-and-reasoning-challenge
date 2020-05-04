from src.data import Problem
from src.mapper.map_problem import run_map
from src.transformer.problem_transform import run_transform
from src.solver.static import *
from src.solver.dynamic import *


mappers = [
    "identity", "color", "connect", "connect4", "mesh_split", "mesh_2", "mesh_align", "divide_row_col",
    "spread_row_col", "fractal"
]
transformers = [
    "connect_row", "connect_col", "connect_row_col", "connect_diagonal", "auto_fill_row_col",
    "interior_dir4_zero", "trim_background", "paste_color", "n_cell", "arg_sort", "fill_rectangle"
]
static_solvers = ["set_problem_color", "set_is_pattern"]
dynamic_solvers = [
    "duplicate", "extend_shape"
]
final_solvers = [
    "fit_replace_rule_33", "fit_replace_rule_33_all", "reduce_bitwise", "color_change", "rotations", "fill_pattern"
]


class Runner:

    def __init__(self):
        pass

    @classmethod
    def run_map(cls, problem: Problem, command: str) -> Problem:
        if command in mappers:
            new_problem = run_map(problem, command)
            new_problem.history.append(command)
            return new_problem
        else:
            raise NotImplementedError

    @classmethod
    def run_transform(cls, problem: Problem, command: str) -> Problem:
        if command in transformers:
            new_problem = run_transform(problem, command)
            new_problem.history.append(command)
            return new_problem
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
        if command in dynamic_solvers or command in final_solvers:
            new_problem = eval(f'{command}(problem)')
            new_problem.history.append(command)
            return new_problem
        else:
            raise NotImplementedError
