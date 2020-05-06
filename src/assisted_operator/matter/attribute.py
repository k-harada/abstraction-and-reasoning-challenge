import numpy as np
from src.data import Matter


def set_color_add(m: Matter, color_add: int) -> Matter:
    new_matter: Matter = m.deepcopy()
    new_matter.color_add = color_add
    return new_matter
