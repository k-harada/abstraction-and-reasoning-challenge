import numpy as np
from src.data import Matter


def set_color_add(m: Matter, color_add: np.int8) -> Matter:
    new_matter: Matter
    new_matter = m.copy()
    new_matter.color_add = color_add
    return new_matter
