from src.data import Case, Problem
from src.operator.transformer.reducer.fill_pattern.periodicity_row_col import find_periodicity_row, AutoFillRowColPeriodicity

IGNORE_N_LINES = 3


def set_is_periodic_row(p: Problem) -> None:

    c: Case
    for c in p.train_y_list:
        c_arr = c.repr_values()
        if c_arr.shape[0] <= IGNORE_N_LINES:
            p.is_periodic_row = False
            return None
        if find_periodicity_row(c_arr, -1) == c_arr.shape[0]:
            p.is_periodic_row = False
            return None
    p.is_periodic_row = True
    return None


def set_is_periodic_col(p: Problem) -> None:
    c: Case
    for c in p.train_y_list:
        c_arr = c.repr_values()
        if c_arr.shape[1] <= IGNORE_N_LINES:
            p.is_periodic_col = False
            return None
        if AutoFillRowColPeriodicity.find_periodicity_col(c_arr, -1) == c_arr.shape[1]:
            p.is_periodic_col = False
            return None
    p.is_periodic_col = True
    return None
