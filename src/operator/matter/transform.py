import numpy as np
from src.data import Matter

# matter -> matter


def fractal(m):

    r, c = m.values.shape

    assert max(r ** 2, c ** 2) <= 30

    new_m_value = np.ones((r ** 2, c ** 2), dtype=np.int) * m.background_color

    for i in range(r):
        for j in range(c):
            if m.values[i, j] != m.background_color:
                new_m_value[i * r: (i + 1) * r, j * c: (j + 1) * c] = m.values
    matter_c = m.replace(x_arr=new_m_value, x0=None, x1=None, y0=None, y1=None, ground_rows=None, ground_cols=None)

    return matter_c

