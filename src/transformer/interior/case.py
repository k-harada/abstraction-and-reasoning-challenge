from src.data import Case, Matter
from .matter import interior_dir4_zero as mat_int


def interior_dir4_zero(c: Case) -> Case:
    new_case = c.copy()
    m: Matter
    new_case.matter_list = [mat_int(m) for m in c.matter_list]
    return new_case
