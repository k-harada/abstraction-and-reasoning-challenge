from typing import List
import numpy as np

from src.data import Matter
from src.mapper.interior import array


def interior_dir4_zero(m: Matter) -> List[Matter]:
    res_bool = array.interior_dir4_zero(m.bool_represents())
    if m.color_add is not None:
        new_values = res_bool.astype(np.int) * m.color_add
    else:
        new_values = res_bool.astype(np.int) * m.max_color()
    return [m, Matter(new_values, m.x0, m.y0, m.background_color)]
