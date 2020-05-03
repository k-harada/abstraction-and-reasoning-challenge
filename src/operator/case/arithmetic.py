import numpy as np
from src.data import Case, Matter


def n_cell(c: Case) -> Case:
    m: Matter
    new_case = c.copy()
    new_case.matter_list = [m.copy() for m in c.matter_list]
    for m in new_case.matter_list:
        m.a = m.n_cell()
    return new_case


def arg_sort(c: Case) -> Case:
    m: Matter
    new_case = c.copy()
    a_list = [m.a for m in c.matter_list if m.a is not None]
    assert len(a_list) == len(c.matter_list)
    a_arg_sort = np.argsort(a_list).astype(np.int)
    a_arg_sort_inv = [0] * len(a_arg_sort)
    color = 0
    value_map = dict()
    for i in a_arg_sort:
        if color == c.background_color:
            color += 1
        if a_list[i] not in value_map.keys():
            value_map[a_list[i]] = color
            color += 1
    for i, a in enumerate(a_list):
        a_arg_sort_inv[i] = value_map[a]
    new_case.matter_list = [m.copy() for m in c.matter_list]
    for m, new_a in zip(new_case.matter_list, a_arg_sort_inv):
        m.a = new_a
    return new_case
