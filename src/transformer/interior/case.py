from src.data import Case, Matter
from .matter import interior_dir4_zero as mat_int


def interior_dir4_zero(c: Case) -> Case:
    new_case = c.copy()
    m: Matter
    if c.color_add is not None:
        color_add = c.color_add
    else:
        color_add = c.max_color()
    new_case.matter_list = [mat_int(m, color_add) for m in c.matter_list]
    return new_case
