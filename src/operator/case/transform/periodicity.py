from src.data import Case
from src.operator.matter.transform import periodicity as per_mat


def auto_fill_row_col(c: Case) -> Case:
    new_case = c.copy()
    new_case.matter_list = [per_mat.auto_fill_row_col(m) for m in c.matter_list]
    return new_case
