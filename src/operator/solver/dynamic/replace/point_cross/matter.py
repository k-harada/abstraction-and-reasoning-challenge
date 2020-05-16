from typing import Tuple
import numpy as np
from src.data import Matter
from .array import point_cross_cnt_arr, point_cross_fit_arr


def point_cross_cnt_mat(m: Matter, y_arr: np.array) -> Tuple[np.array, int]:
    assert m.n_color() == 1
    color_cnt = m.color_count()
    color_cnt[m.background_color] = 0
    m_color = [c for c in range(10) if color_cnt[c] > 0][0]
    assert m.shape == y_arr.shape
    return point_cross_cnt_arr(m.values, y_arr, m_color), m_color


def point_cross_fit_mat(m: Matter, op_arr: np.array) -> Matter:
    assert m.n_color() == 1
    color_cnt = m.color_count()
    color_cnt[m.background_color] = 0
    m_color = [c for c in range(10) if color_cnt[c] > 0][0]

    res_arr = point_cross_fit_arr(m.values, m_color, op_arr[m_color])
    new_values = np.zeros(m.shape, dtype=int)
    new_values[res_arr == 1] = m_color
    new_values[res_arr == 0] = m.background_color
    new_matter = m.copy()
    new_matter.set_values(new_values)

    return new_matter
