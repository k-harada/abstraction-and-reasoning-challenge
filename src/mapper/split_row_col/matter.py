import numpy as np
from typing import List

from src.data import Matter


def split_row_col(m: Matter, d_row: np.int, d_col: np.int) -> List[Matter]:

    assert m.shape[0] % d_row == 0
    mrh = m.shape[0] // d_row
    assert mrh != 0

    assert m.shape[1] % d_col == 0
    mch = m.shape[1] // d_col
    assert mch != 0

    res_list = []
    for i in range(d_row):
        for j in range(d_col):
            new_matter = Matter(
                m.values[mrh * i:mrh * (i + 1), mch * j:mch * (j + 1)], 0, 0, m.background_color
            )
            res_list.append(new_matter)
    return res_list
