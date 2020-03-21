from src.operator.array.transfrom.trim_background import trim_background as trim_background_array
from src.data import Matter


def trim_background(m: Matter) -> Matter:
    new_values, xy0 = trim_background_array(m.values, m.background_color)
    return Matter(new_values, m.x0, m.y0, m.background_color)
