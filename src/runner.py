from src.data import Problem
from src.operator.problem.map_reduce import set_map_reduce
from src.operator.problem.transform import run_transform
from src.solver.static import set_problem_color, set_is_pattern
from src.solver.dynamic import fill_pattern


mappers = [
    "identity", "color", "connect", "interior_dir4_zero", "mesh_split", "mesh_2", "mesh_align",
    "split_row_col", "split_row", "split_col"
]
reducers = ["simple", "pick", "bitwise", "fractal"]
transformers = [
    "connect_row", "connect_col", "connect_row_col", "connect_diagonal", "auto_fill_row_col",
    "transpose", "rev_row", "rev_col", "rot_180",
    "rot_rev_180", "rot_90", "rot_270", "trim_background", "paste_color", "n_cell", "arg_sort"
]
static_solvers = ["set_problem_color", "set_is_pattern"]
dynamic_solvers = ["fill_pattern"]


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
    def pre_solve(cls, problem: Problem, command: str) -> Problem:
        if command in static_solvers:
            return eval(f'{command}(problem)')
        else:
            raise NotImplementedError

    @classmethod
    def run_solve(cls, problem: Problem, command: str) -> Problem:
        if command in dynamic_solvers:
            return eval(f'{command}(problem)')
        else:
            raise NotImplementedError
