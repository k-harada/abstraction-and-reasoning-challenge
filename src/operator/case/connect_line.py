from src.data import Case
from src.operator.matter import connect_line as cnl_mat


def connect_row(c: Case) -> Case:
    new_case = c.copy()
    new_case.matter_list = [m if m.is_mesh else cnl_mat.connect_row(m) for m in c.matter_list]
    return new_case


def connect_col(c: Case) -> Case:
    new_case = c.copy()
    new_case.matter_list = [m if m.is_mesh else cnl_mat.connect_col(m) for m in c.matter_list]
    return new_case


def connect_row_col(c: Case) -> Case:
    new_case = c.copy()
    new_case.matter_list = [m if m.is_mesh else cnl_mat.connect_row_col(m) for m in c.matter_list]
    return new_case


def connect_diagonal(c: Case) -> Case:
    new_case = c.copy()
    new_case.matter_list = [m if m.is_mesh else cnl_mat.connect_diagonal(m) for m in c.matter_list]
    return new_case
