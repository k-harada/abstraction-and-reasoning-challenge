from typing import Tuple
import numpy as np
from src.data import Matter
from .array import point_cross_cnt_arr, point_cross_fit_arr


def point_cross_cnt_mat(m: Matter, y_arr: np.array) -> Tuple[np.array, int]:
    assert m.n_color() == 1
    color_cnt = m.color_count()
    color_cnt[m.background_color] = 0
    m_color = [c for c in range(10) if color_cnt[c] > 0][0]
    x_arr = np.zeros(y_arr.shape, dtype=np.int)
    try:
        x_arr[m.x0:m.x0+m.shape[0], m.y0:m.y0+m.shape[1]] = m.values
    except:
        print(x_arr, y_arr, m.x0, m.x0+m.shape[0], m.y0, m.y0+m.shape[1])
        raise
    return point_cross_cnt_arr(x_arr, y_arr, m_color), m_color


def point_cross_fit_mat(m: Matter, n_row, n_col, op_arr: np.array) -> Matter:
    assert m.n_color() == 1
    color_cnt = m.color_count()
    color_cnt[m.background_color] = 0
    m_color = [c for c in range(10) if color_cnt[c] > 0][0]

    x_arr = np.zeros((n_row, n_col), dtype=np.int)
    x_arr[m.x0:m.x0 + m.shape[0], m.y0:m.y0 + m.shape[1]] = m.values

    res_arr = point_cross_fit_arr(x_arr, m_color, op_arr[m_color])
    new_values = np.zeros(x_arr.shape, dtype=int)
    new_values[res_arr == 1] = m_color
    new_values[res_arr == 0] = m.background_color
    new_matter = m.copy()
    new_matter.set_values(new_values)
    new_matter.x0 = 0
    new_matter.y0 = 0

    return new_matter
