import numpy as np
from src.data import Matter

# matter -> matter


def trim_background(m):

    x_sum = (m.value != m.background_color).sum(axis=1)
    y_sum = (m.value != m.background_color).sum(axis=0)
    min_x = min([i for i in range(m.shape[0]) if x_sum[i]])
    max_x = max([i for i in range(m.shape[0]) if x_sum[i]])
    min_y = min([i for i in range(m.shape[1]) if y_sum[i]])
    max_y = max([i for i in range(m.shape[1]) if y_sum[i]])
    new_m_value = m.value[min_x:max_x + 1, min_y:max_y + 1]
    matter_c = Matter(new_m_value)
    matter_c.placement = [min_x, min_y]

    return matter_c
