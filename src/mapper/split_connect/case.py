from src.data import Case
from .matter import split_connect as split_connect_mat


def split_connect(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = split_connect_mat(c.matter_list[0], True)
    # a <- n_cell by default
    for m in new_case.matter_list:
        m.a = m.n_cell()
    return new_case


def split_connect_4(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = split_connect_mat(c.matter_list[0], False)
    # a <- n_cell by default
    for m in new_case.matter_list:
        m.a = m.n_cell()
    return new_case
