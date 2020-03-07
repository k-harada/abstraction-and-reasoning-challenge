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
        new_m_value = np.ones(m.values.shape, dtype=np.int) * m.background_color
        new_m_value[m.values == c] = c
        matter_c = Matter(new_m_value)
        matter_c.color = c
        res_list.append(matter_c)

    return res_list
