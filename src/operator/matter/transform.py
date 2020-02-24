import numpy as np
from src.data import Matter

# matter -> matter


def trim_background(m):

    x_sum = (m.values != m.background_color).sum(axis=1)
    y_sum = (m.values != m.background_color).sum(axis=0)

    if x_sum.sum() == 0:
        matter_c = Matter(m.values)
        matter_c.placement = [0, 0]
        return matter_c

    min_x = min([i for i in range(m.shape[0]) if x_sum[i]])
    max_x = max([i for i in range(m.shape[0]) if x_sum[i]])
    min_y = min([i for i in range(m.shape[1]) if y_sum[i]])
    max_y = max([i for i in range(m.shape[1]) if y_sum[i]])
    new_m_value = m.values[min_x:max_x + 1, min_y:max_y + 1]
    matter_c = Matter(new_m_value)
    matter_c.placement = [min_x, min_y]
    matter_c.color = m.color
    matter_c.background_color = m.background_color
    matter_c.base_value = m.base_value

    return matter_c


def resize(m):

    r, c = m.shape

    assert m.base_value > 1
    assert max(r * 2, c * 2) <= 30

    new_m_value = np.repeat(np.repeat(m.values, m.base_value, axis=0), m.base_value, axis=1)
    matter_c = Matter(new_m_value)
    matter_c.placement = m.placement.copy()
    matter_c.color = m.color
    matter_c.background_color = m.background_color
    matter_c.base_value = m.base_value

    return matter_c


def fractal(m):

    r, c = m.shape

    assert max(r ** 2, c ** 2) <= 30

    new_m_value = np.ones((r ** 2, c ** 2), dtype=np.int) * m.background_color

    for i in range(r):
        for j in range(c):
            if m.values[i, j] != m.background_color:
                new_m_value[i * r: (i + 1) * r, j * c: (j + 1) * c] = m.values
    matter_c = Matter(new_m_value)
    matter_c.placement = m.placement.copy()
    matter_c.color = m.color
    matter_c.background_color = m.background_color
    matter_c.base_value = m.base_value

    return matter_c


def paint(m):

    assert m.color != -1
    assert m.color != m.background_color

    new_m_value = np.ones(m.values.shape, dtype=np.int) * m.background_color
    new_m_value[m.values != m.background_color] = m.color

    matter_c = Matter(new_m_value)
    matter_c.placement = m.placement.copy()
    matter_c.color = m.color
    matter_c.background_color = m.background_color
    matter_c.base_value = m.base_value

    return matter_c


def pick_one_color(m, c):

    new_m_value = np.ones(m.values.shape, dtype=np.int) * m.background_color
    new_m_value[m.values == c] = c

    matter_c = Matter(new_m_value)
    matter_c.placement = m.placement.copy()
    matter_c.color = c
    matter_c.background_color = m.background_color
    matter_c.base_value = m.base_value

    return matter_c
