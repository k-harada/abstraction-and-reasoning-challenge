from typing import Tuple
import numpy as np
from src.data import Case
from src.assisted_operator.matter import attribute as attr_mat


def set_color_add(c: Case, color_add: int) -> Case:
    new_case = c.copy()
    new_case.matter_list = [attr_mat.set_color_add(m, color_add) for m in c.matter_list]
    new_case.color_add = color_add
    return new_case


def set_shape(c: Case, new_shape: Tuple[int, int]) -> Case:
    assert new_shape[0] >= c.shape[0]
    assert new_shape[1] >= c.shape[1]
    new_case = c.copy()
    new_case.matter_list = c.matter_list[:]
    new_case.n_row, new_case.col = new_shape
    return new_case
