import numpy as np
from src.data import Problem


def eval_distance(problem: Problem) -> np.int:
    return problem.eval_distance()
