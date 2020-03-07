import numpy as np
from src.data import Matter, MatterFactory

# matter -> List[matter]


def split_row_2(m):
    mrh = m.values.shape[0] // 2
    if mrh == 0:
        return [m.copy()]
    elif m.values.shape[0] % 2 == 0:
        return [
            MatterFactory.slice(m, 0, mrh, 0, m.values.shape[1]),
            MatterFactory.slice(m, mrh, m.values.shape[0], 0, m.values.shape[1])
        ]
    else:
        return [
            MatterFactory.slice(m, 0, mrh, 0, m.values.shape[1]),
            MatterFactory.slice(m, mrh + 1, m.values.shape[0], 0, m.values.shape[1])
        ]


def split_col_2(m):
    mch = m.values.shape[1] // 2
    if mch == 0:
        return [m.copy()]
    elif m.values.shape[1] % 2 == 0:
        return [
            MatterFactory.slice(m, 0, m.values.shape[0], 0, mch),
            MatterFactory.slice(m, 0, m.values.shape[0], mch, m.values.shape[1])
        ]
    else:
        return [
            MatterFactory.slice(m, 0, m.values.shape[0], 0, mch),
            MatterFactory.slice(m, 0, m.values.shape[0], mch + 1, m.values.shape[1])
        ]


def split_row_col_const(m, nr, nc):
    """split without line"""
    assert m.values.shape[0] % nr == 0
    assert m.values.shape[1] % nc == 0
    mrh = m.values.shape[0] // nr
    mch = m.values.shape[1] // nc
    res_list = []
    for i in range(nr):
        for j in range(nc):
            res_list.append(MatterFactory.slice(m, i * mrh, (i + 1) * mrh, j * mch, (j + 1) * mch))
    return res_list
