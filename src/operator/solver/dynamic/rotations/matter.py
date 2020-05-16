from src.operator.solver.dynamic.rotations import array
from src.data import Matter


def transpose(m: Matter) -> Matter:
    assert m.is_square()
    new_matter: Matter = m.copy()
    new_matter.set_values(array.transpose(m.values))
    return new_matter


def rev_row(m: Matter) -> Matter:
    new_matter: Matter = m.copy()
    new_matter.set_values(array.rev_row(m.values))
    return new_matter


def rev_col(m: Matter) -> Matter:
    new_matter: Matter = m.copy()
    new_matter.set_values(array.rev_col(m.values))
    return new_matter


def rot_180(m: Matter) -> Matter:
    new_matter: Matter = m.copy()
    new_matter.set_values(array.rot_180(m.values))
    return new_matter


def rot_rev_180(m: Matter) -> Matter:
    assert m.is_square()
    new_matter: Matter = m.copy()
    new_matter.set_values(array.rot_rev_180(m.values))
    return new_matter


def rot_90(m: Matter) -> Matter:
    assert m.is_square()
    new_matter: Matter = m.copy()
    new_matter.set_values(array.rot_90(m.values))
    return new_matter


def rot_270(m: Matter) -> Matter:
    assert m.is_square()
    new_matter: Matter = m.copy()
    new_matter.set_values(array.rot_270(m.values))
    return new_matter
