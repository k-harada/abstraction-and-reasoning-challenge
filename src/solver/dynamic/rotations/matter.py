from src.solver.dynamic.rotations import array
from src.data import Matter


def transpose(m: Matter) -> Matter:
    assert m.is_square
    return Matter(array.transpose(m.values), m.y0, m.x0, m.background_color)


def rev_row(m: Matter) -> Matter:
    return Matter(array.rev_row(m.values), m.x0, m.y0, m.background_color)


def rev_col(m: Matter) -> Matter:
    return Matter(array.rev_col(m.values), m.x0, m.y0, m.background_color)


def rot_180(m: Matter) -> Matter:
    return Matter(array.rot_180(m.values), m.x0, m.y0, m.background_color)


def rot_rev_180(m: Matter) -> Matter:
    assert m.is_square
    return Matter(array.rot_rev_180(m.values), m.y0, m.x0, m.background_color)


def rot_90(m: Matter) -> Matter:
    assert m.is_square
    return Matter(array.rot_90(m.values), m.y0, m.x0, m.background_color)


def rot_270(m: Matter) -> Matter:
    assert m.is_square
    return Matter(array.rot_270(m.values), m.y0, m.x0, m.background_color)
