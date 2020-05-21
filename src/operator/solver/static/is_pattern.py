import numpy as np
from src.data import Problem, Case
from src.operator.solver.dynamic.pattern.fill_pattern import is_pattern_y


def set_is_pattern(p: Problem) -> None:
    if is_pattern_y(p):
        p.is_pattern = True
    return None
