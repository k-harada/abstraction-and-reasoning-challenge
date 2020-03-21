from src.operator.array.transfrom import periodictity
from src.data import Matter


def auto_fill_row_col(m: Matter) -> Matter:
    new_values = periodictity.auto_fill_row_col(m.values, m.background_color)
    return Matter(new_values, m.x0, m.y0, m.background_color)
