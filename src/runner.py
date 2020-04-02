from src.data import Problem
from src.operator.problem.map import run_map
from src.operator.problem.transform import run_transform
from src.operator.problem.reduce import run_reduce

mappers = ["color", "fractal", "interior_dir4_zero", "mesh", "split_row_col", "split_row", "split_col"]
transformers = [
    "connect_row", "connect_col", "connect_diagonal", "auto_fill_row_col",
    "transpose", "rev_row", "rev_col", "rot_180",
    "rot_rev_180", "rot_90", "rot_270", "trim_background", "set_problem_color"
]
reducers = [
    "bitwise_or", "bitwise_and", "bitwise_xor", "bitwise_not_xor", "bitwise_not_or", "bitwise_not_and",

]
all_operators = mappers + transformers + reducers


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
