from typing import Tuple
import numpy as np
from src.data import Matter
from .array import point_cross_cnt_arr, point_cross_fit_arr


def point_cross_cnt_mat(m: Matter, y_arr: np.array) -> Tuple[np.array, int]:
    assert m.color is not None
    assert m.shape == y_arr.shape
    return point_cross_cnt_arr(m.values, y_arr, m.color), m.color


def point_cross_fit_mat(m: Matter, op_arr: np.array) -> Matter:

    assert m.color is not None

    res_arr = point_cross_fit_arr(m.values, m.color, op_arr[m.color])
    new_values = np.zeros(m.shape, dtype=int)
    new_values[res_arr == 1] = m.color
    new_values[res_arr == 0] = m.background_color
    new_matter = m.copy()
    new_matter.values = new_values

    return new_matter
