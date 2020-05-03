from src.transformer.array import connect_line
from src.data import Matter


def connect_row(m: Matter) -> Matter:
    new_values = connect_line.connect_row(m.values, m.background_color)
    return Matter(new_values, m.x0, m.y0, m.background_color)


def connect_col(m: Matter) -> Matter:
    new_values = connect_line.connect_col(m.values, m.background_color)
    return Matter(new_values, m.x0, m.y0, m.background_color)


def connect_row_col(m: Matter) -> Matter:
    new_values = connect_line.connect_row_col(m.values, m.background_color)
    return Matter(new_values, m.x0, m.y0, m.background_color)


def connect_diagonal(m: Matter) -> Matter:
    new_values = connect_line.connect_diagonal(m.values, m.background_color)
    return Matter(new_values, m.x0, m.y0, m.background_color)
