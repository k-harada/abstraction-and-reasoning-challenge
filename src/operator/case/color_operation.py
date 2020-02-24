import numpy as np
from src.operator.matter.transform import pick_one_color


def pick_color(case):

    new_case = case.copy()
    new_case.matter_list = []
    for m in case.matter_list:
        new_case.matter_list.append(pick_one_color(m, case.metadata.color))
    return new_case


def max_color(case):

    if case.metadata.color_value.sum() == 0:
        new_case = count_color(case)
    else:
        new_case = case.deep_copy()
    v = new_case.metadata.color_value.copy()
    if new_case.metadata.background_color != -1:
        v[new_case.metadata.background_color] = 0
    new_case.metadata.color = np.argmax(v)

    return new_case


def min_color(case):

    if case.metadata.color_value.sum() == 0:
        new_case = count_color(case)
    else:
        new_case = case.deep_copy()
    v = new_case.metadata.color_value.copy()
    v[v == 0] = 1000000
    v[new_case.metadata.background_color] = 1000000
    new_case.metadata.color = np.argmin(v)

    return new_case


def count_color(case):

    new_case = case.deep_copy()
    new_case.metadata.color_value *= 0
    for m in new_case.matter_list:
        for c in range(10):
            new_case.metadata.color_value[c] += (m.values == c).sum()
    return new_case

