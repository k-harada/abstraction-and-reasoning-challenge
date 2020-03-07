import numpy as np
from src.data import Matter

# matter -> List[matter]


def split_rotations(m):
    if m.values.shape[0] == m.values.shape[1]:
        return [m.copy(), rev_col(m), rev_row(m), rot_180(m), transpose(m), rot_90(m), rot_rev_180(m), rot_270(m)]
    else:
        return [m.copy(), rev_col(m), rev_row(m), rot_180(m)]


def transpose(m):
    matter_c = m.copy()
    matter_c.values = m.values.copy().transpose()
    return matter_c


def rev_row(m):
    matter_c = m.copy()
    matter_c.values = m.values.copy()[::-1, :]
    return matter_c


def rev_col(m):
    matter_c = m.copy()
    matter_c.values = m.values.copy()[:, ::-1]
    return matter_c


def rot_180(m):
    matter_c = m.copy()
    matter_c.values = m.values.copy()[::-1, ::-1]
    return matter_c


def rot_rev_180(m):
    matter_c = m.copy()
    matter_c.values = m.values.copy().transpose()[::-1, ::-1]
    return matter_c


def rot_90(m):
    matter_c = m.copy()
    matter_c.values = m.values.copy().transpose()[:, ::-1]
    return matter_c


def rot_270(m):
    matter_c = m.copy()
    matter_c.values = m.values.copy().transpose()[::-1, :]
    return matter_c
