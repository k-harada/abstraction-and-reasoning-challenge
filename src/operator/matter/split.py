import numpy as np
from src.data import Matter

# matter -> List[matter]


def split_color(m):

    res_list = []
    for c in range(10):
        if c == m.background_color:
            continue
        if (m.values == c).sum() == 0:
            continue
        new_m_value = np.ones(m.shape, dtype=np.int) * m.background_color
        new_m_value[m.values == c] = c
        matter_c = Matter(new_m_value)
        matter_c.color = c
        res_list.append(matter_c)

    return res_list


def split_row_2(m):
    mrh = m.shape[0] // 2
    if mrh == 0:
        return [Matter(m.values)]
    elif m.shape[0] % 2 == 0:
        return [Matter(m.values[:mrh, :]), Matter(m.values[mrh:, :])]
    else:
        return [Matter(m.values[:mrh, :]), Matter(m.values[mrh + 1:, :])]


def split_col_2(m):
    mch = m.shape[1] // 2
    if mch == 0:
        return [Matter(m.values)]
    elif m.shape[1] % 2 == 0:
        return [Matter(m.values[:, :mch]), Matter(m.values[:, mch:])]
    else:
        return [Matter(m.values[:, :mch]), Matter(m.values[:, mch + 1:])]
