import numpy as np
from typing import List

from src.data import Matter


def split_row_col_v(m: Matter, m_row: np.int8, m_col: np.int8) -> List[Matter]:

    assert m.shape[0] % m_row == 0
    mrh = m.shape[0] // m_row
    assert mrh != 0

    assert m.shape[1] % m_col == 0
    mch = m.shape[1] // m_col
    assert mch != 0

    res_list = []
    for i in range(m_row):
        for j in range(m_col):
            new_matter = Matter(
                m.values[mrh * i:mrh * (i + 1), mch * j:mch * (j + 1)], i * mrh, j * mch, m.background_color
            )
            res_list.append(new_matter)
    return res_list


def split_row(m: Matter) -> List[Matter]:
    return split_row_col_v(m, m.m_row, np.int8(1))


def split_col(m: Matter) -> List[Matter]:
    return split_row_col_v(m, np.int8(1), m.m_col)


def split_row_col(m: Matter) -> List[Matter]:
    return split_row_col_v(m, m.m_row, m.m_col)
