import numpy as np
from src.data import Case, Matter


def trivial_reducer(c: Case) -> np.array:
    # pile up
    # paste background
    repr_values = np.ones(c.shape, dtype=np.int) * c.background_color
    # collect values
    m: Matter
    for m in c.matter_list:
        if not m.bool_show:
            continue
        for i in range(m.shape[0]):
            for j in range(m.shape[1]):
                if m.values[i, j] != m.background_color:
                    if m.values[i, j] != repr_values[m.x0 + i, m.y0 + j]:
                        assert repr_values[m.x0 + i, m.y0 + j] == c.background_color
                        repr_values[m.x0 + i, m.y0 + j] = m.values[i, j]

    return repr_values
