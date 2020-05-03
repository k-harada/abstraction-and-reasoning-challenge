import numpy as np
from src.data import Case
from . import matter_map


def identity(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = [c.matter_list[0]]
    return new_case


def color(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.color(c.matter_list[0])
    return new_case


def connect(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.connect(c.matter_list[0])
    # a <- n_cell by default
    for m in new_case.matter_list:
        m.a = m.n_cell()
    return new_case


def interior_dir4_zero(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.interior_dir4_zero(c.matter_list[0])
    return new_case


def mesh_split(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.mesh_split(c.matter_list[0])
    return new_case


def mesh_2(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.mesh_2(c.matter_list[0])
    return new_case


def mesh_align(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.mesh_align(c.matter_list[0])
    new_case.shape = new_case.matter_list[0].shape
    return new_case


def split_row_col(c: Case, d_row: np.int, d_col: np.int) -> Case:
    assert len(c.matter_list) == 1
    assert (d_row, d_col) != (1, 1)
    new_case = c.copy()
    new_case.matter_list = matter_map.split_row_col(c.matter_list[0], d_row, d_col)
    new_case.shape = new_case.matter_list[0].shape
    return new_case