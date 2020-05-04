from src.data import Case
from .matter import fill_rectangle as fill_rectangle_mat


def fill_rectangle(c: Case) -> Case:

    assert c.color_add is not None

    new_c: Case = c.copy()
    new_c.matter_list = [fill_rectangle_mat(m, c.color_add) for m in c.matter_list]

    return new_c
