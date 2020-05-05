from src.data import Case, Problem
from src.transformer.fill_pattern.periodicity_row_col import AutoFillRowColPeriodicity

IGNORE_N_LINES = 3


def is_periodic_row(p: Problem) -> bool:

    c: Case
    for c in p.train_y_list:
        c_arr = c.repr_values()
        if c_arr.shape[0] <= IGNORE_N_LINES:
            return False
        if AutoFillRowColPeriodicity.find_periodicity_row(c_arr, -1) == c_arr.shape[0]:
            return False

    return True


def is_periodic_col(p: Problem) -> bool:
    c: Case
    for c in p.train_y_list:
        c_arr = c.repr_values()
        if c_arr.shape[1] <= IGNORE_N_LINES:
            return False
        if AutoFillRowColPeriodicity.find_periodicity_col(c_arr, -1) == c_arr.shape[1]:
            return False

    return True
