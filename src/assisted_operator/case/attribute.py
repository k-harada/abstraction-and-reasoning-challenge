import numpy as np
from src.data import Case
from src.assisted_operator.matter import attribute as attr_mat


def set_color_add(c: Case, color_add: np.int8) -> Case:
    new_case = c.copy()
    new_case.matter_list = [attr_mat.set_color_add(m, color_add) for m in c.matter_list]
    new_case.color_add = color_add
    return new_case
