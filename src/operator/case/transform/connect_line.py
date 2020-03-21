from src.data import Case
from src.operator.matter.transform import connect_line as cnl_mat


def connect_row(c: Case) -> Case:
    new_case = c.copy()
    new_case.matter_list = [cnl_mat.connect_row(m) for m in c.matter_list]
    return new_case


def connect_col(c: Case) -> Case:
    new_case = c.copy()
    new_case.matter_list = [cnl_mat.connect_col(m) for m in c.matter_list]
    return new_case


def connect_diagonal(c: Case) -> Case:
    new_case = c.copy()
    new_case.matter_list = [cnl_mat.connect_diagonal(m) for m in c.matter_list]
    return new_case
