from src.transformer.array.trim_background import trim_background as trim_background_array
from src.data import Matter


def trim_background(m: Matter) -> Matter:
    new_values, xy0 = trim_background_array(m.values, m.background_color)
    return Matter(new_values, 0, 0, m.background_color)
