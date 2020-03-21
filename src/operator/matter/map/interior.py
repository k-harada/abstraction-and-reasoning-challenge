from typing import List
import numpy as np

from src.data import Matter
from src.operator.array.map import interior


def interior_dir4_zero(m: Matter) -> List[Matter]:
    res_bool = interior.interior_dir4_zero(m.bool_represents)
    new_values = res_bool.astype(np.int8) * m.color_a
    return [m, Matter(new_values, m.x0, m.y0, m.background_color)]
