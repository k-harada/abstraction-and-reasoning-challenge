import numpy as np
from src.data import Case
from .matter import point_cross_cnt_mat, point_cross_fit_mat


def point_cross_cnt_case(c: Case, y_arr) -> np.array:

    return [point_cross_cnt_mat(m, y_arr) for m in c.matter_list]


def point_cross_fit_case(c: Case, op_arr: np.array) -> Case:

    new_case: Case = c.copy()
    new_case.matter_list = [point_cross_fit_mat(m, c.shape[0], c.shape[1], op_arr) for m in c.matter_list]

    return new_case
