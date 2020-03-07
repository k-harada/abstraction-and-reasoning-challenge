import numpy as np
from src.data import MatterFactory, CaseFactory
from src.util.periodictity import auto_fill_row_col as auto_fill_row_col_arr


def auto_fill_row_col(case):
    values = case.repr_values
    new_values = auto_fill_row_col_arr(values, case.background_color)
    new_case = CaseFactory.from_values(new_values, case.background_color)
    return new_case
