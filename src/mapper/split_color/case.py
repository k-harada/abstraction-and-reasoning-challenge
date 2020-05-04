from src.data import Case
from .matter import split_color as split_color_mat


def split_color(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = split_color_mat(c.matter_list[0])
    return new_case
