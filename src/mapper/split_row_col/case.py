from src.data import Case
from .matter import split_row_col as split_row_col_matter


def split_row_col(c: Case, d_row: int, d_col: int) -> Case:
    assert len(c.matter_list) == 1
    assert (d_row, d_col) != (1, 1)
    new_case = c.copy()
    new_case.matter_list = split_row_col_matter(c.matter_list[0], d_row, d_col)
    new_case.shape = new_case.matter_list[0].shape
    return new_case
