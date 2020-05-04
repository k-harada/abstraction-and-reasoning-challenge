from src.data import Matter
from src.transformer.interior import array


def interior_dir4_zero(m: Matter, color_add) -> Matter:
    res_bool = array.interior_dir4_zero(m.values)
    new_values = m.values.copy()

    new_values[res_bool] = color_add

    new_m: Matter
    new_m = Matter(new_values, m.x0, m.y0, m.background_color)

    return new_m
