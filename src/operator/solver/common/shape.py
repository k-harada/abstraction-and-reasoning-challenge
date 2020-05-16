from typing import Tuple
import numpy as np
from src.data import Case, Problem


def is_same(p: Problem) -> bool:

    cx: Case
    cy: Case

    for cx, cy in zip(p.train_x_list, p.train_y_list):
        if cx.shape[0] != cy.shape[0] or cx.shape[1] != cy.shape[1]:
            return False
    return True


def is_multiple(p: Problem) -> Tuple[bool, int, int]:

    cx0: Case = p.train_x_list[0]
    cy0: Case = p.train_y_list[0]

    if cx0.shape[0] == 0 or cx0.shape[1] == 0:
        return False, -1, -1
    if cy0.shape[0] % cx0.shape[0] != 0 or cy0.shape[1] % cx0.shape[1] != 0:
        return False, -1, -1
    m_row: int = cy0.shape[0] // cx0.shape[0]
    m_col: int = cy0.shape[1] // cx0.shape[1]

    cx: Case
    cy: Case

    for cx, cy in zip(p.train_x_list, p.train_y_list):
        if cx.shape[0] * m_row != cy.shape[0] or cx.shape[1] * m_col != cy.shape[1]:
            return False, -1, -1
    return True, m_row, m_col


def is_division(p: Problem) -> Tuple[bool, int, int]:

    cx0: Case = p.train_x_list[0]
    cy0: Case = p.train_y_list[0]

    if cy0.shape[0] == 0 or cy0.shape[1] == 0:
        return False, -1, -1
    if cx0.shape[0] % cy0.shape[0] != 0 or cx0.shape[1] % cy0.shape[1] != 0:
        return False, -1, -1
    d_row: int = cx0.shape[0] // cy0.shape[0]
    d_col: int = cx0.shape[1] // cy0.shape[1]

    cx: Case
    cy: Case

    for cx, cy in zip(p.train_x_list, p.train_y_list):
        if cy.shape[0] * d_row != cx.shape[0] or cy.shape[1] * d_col != cx.shape[1]:
            return False, -1, -1
    return True, d_row, d_col


def is_constant(p: Problem) -> Tuple[bool, int, int]:

    cy0: Case = p.train_y_list[0]

    size_row: int = cy0.shape[0]
    size_col: int = cy0.shape[1]

    cy: Case

    for cy in p.train_y_list:
        if cy.shape[0] != size_row or cy.shape[1] != size_col:
            return False, -1, -1
    return True, size_row, size_col
