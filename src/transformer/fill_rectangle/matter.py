from src.data import Matter


def fill_rectangle(m: Matter, color_add) -> Matter:

    new_values = m.values.copy()
    new_values[new_values == m.background_color] = color_add
    new_m = Matter(new_values, m.x0, m.y0, m.background_color)

    return new_m
