from src.data import Problem
from src.operator.problem.map import run_map
from src.operator.problem.transform import run_transform
from src.operator.problem.reduce import run_reduce
from src.solver.static.color import set_problem_color
from src.solver.static.is_pattern import set_is_pattern
from src.solver.dynamic.pattern.fill_pattern import fill_pattern


mappers = ["color", "fractal", "interior_dir4_zero", "mesh_split", "mesh_2", "mesh_align", "split_row_col", "split_row", "split_col"]
transformers = [
    "connect_row", "connect_col", "connect_row_col", "connect_diagonal", "auto_fill_row_col",
    "transpose", "rev_row", "rev_col", "rot_180",
    "rot_rev_180", "rot_90", "rot_270", "trim_background"
]
reducers = [
    "bitwise_or", "bitwise_and", "bitwise_xor", "bitwise_not_xor", "bitwise_not_or", "bitwise_not_and"
]
static_solvers = ["set_problem_color", "set_is_pattern"]
dynamic_solvers = ["fill_pattern"]
solvers = static_solvers + dynamic_solvers
all_operators = mappers + transformers + reducers + solvers


class Runner:

    def __init__(self):
        pass

    @classmethod
    def run(cls, problem: Problem, command: str) -> Problem:
        if command in mappers:
            return cls.run_map(problem, command)
        elif command in transformers:
            return cls.run_transform(problem, command)
        elif command in reducers:
            return cls.run_reduce(problem, command)
        else:
            raise NotImplementedError

    @classmethod
    def run_map(cls, problem: Problem, command: str) -> Problem:
        if command in mappers:
            return run_map(problem, command)
        else:
            raise NotImplementedError

    @classmethod
    def run_transform(cls, problem: Problem, command: str) -> Problem:
        if command in transformers:
            return run_transform(problem, command)
        else:
            raise NotImplementedError

    @classmethod
    def run_reduce(cls, problem: Problem, command: str) -> Problem:
        if command in reducers:
            return run_reduce(problem, command)
        else:
            raise NotImplementedError

    @classmethod
    def run_solve(cls, problem: Problem, command: str) -> Problem:
        if command in solvers:
            return eval(f'{command}(problem)')
        else:
            raise NotImplementedError
