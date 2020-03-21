import numpy as np


def transpose(x_arr: np.array) -> np.array:
    return x_arr.copy().transpose()


def rev_row(x_arr: np.array) -> np.array:
    return x_arr.copy()[::-1, :]


def rev_col(x_arr: np.array) -> np.array:
    return x_arr.copy()[:, ::-1]


def rot_180(x_arr: np.array) -> np.array:
    return x_arr.copy()[::-1, ::-1]


def rot_rev_180(x_arr: np.array) -> np.array:
    return x_arr.copy().transpose()[::-1, ::-1]


def rot_90(x_arr: np.array) -> np.array:
    return x_arr.copy().transpose()[:, ::-1]


def rot_270(x_arr: np.array) -> np.array:
    return x_arr.copy().transpose()[::-1, :]
