from src.data import Case, Problem
import numpy as np
from src.data import Problem, Case
from src.assisted_operator.problem import attribute as attr_prob


def is_constant(p: Problem) -> bool:

    cy0: Case = p.train_y_list[0]

    size_row: int = cy0.shape[0]
    size_col: int = cy0.shape[1]

    cy: Case

    for cy in p.train_y_list:
        if cy.shape[0] != size_row or cy.shape[1] != size_col:
            return False
    return True


def set_problem_shape(p: Problem) -> Problem:
    # same
    assert is_constant(p)
    cy0: Case = p.train_y_list[0]
    q: Problem
    q = attr_prob.set_shape(p, new_shape=cy0.shape)
    return q
