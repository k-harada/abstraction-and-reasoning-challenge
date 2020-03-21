from src.data import Case
from src.operator.matter import map as matter_map


def color(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.color(c.matter_list[0])
    return new_case


def fractal(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    m = c.matter_list[0]
    new_case.matter_list = matter_map.fractal(m)
    r1, c1 = m.shape
    r2, c2 = m.bool_copy.shape
    new_case.shape = r1 * r2, c1 * c2
    return new_case


def interior_dir4_zero(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.interior_dir4_zero(c.matter_list[0])
    return new_case


def mesh(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.mesh(c.matter_list[0])
    return new_case


def split_row_col(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.split_row_col(c.matter_list[0])
    return new_case


def split_row(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.split_row(c.matter_list[0])
    return new_case


def split_col(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.split_col(c.matter_list[0])
    return new_case
