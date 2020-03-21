from src.operator.array.transfrom import rotations
from src.data import Matter


def transpose(m: Matter) -> Matter:
    assert m.is_square
    return Matter(rotations.transpose(m.values), m.x0, m.y0, m.background_color)


def rev_row(m: Matter) -> Matter:
    return Matter(rotations.rev_row(m.values), m.x0, m.y0, m.background_color)


def rev_col(m: Matter) -> Matter:
    return Matter(rotations.rev_col(m.values), m.x0, m.y0, m.background_color)


def rot_180(m: Matter) -> Matter:
    return Matter(rotations.rot_180(m.values), m.x0, m.y0, m.background_color)


def rot_rev_180(m: Matter) -> Matter:
    assert m.is_square
    return Matter(rotations.rot_rev_180(m.values), m.x0, m.y0, m.background_color)


def rot_90(m: Matter) -> Matter:
    assert m.is_square
    return Matter(rotations.rot_90(m.values), m.x0, m.y0, m.background_color)


def rot_270(m: Matter) -> Matter:
    assert m.is_square
    return Matter(rotations.rot_270(m.values), m.x0, m.y0, m.background_color)
