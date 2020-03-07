import numpy as np
from src.data import MatterFactory, CaseFactory


def pick_max_color(case):
    color_count_temp = case.color_count.copy()
    color_count_temp[case.background_color] = 0
    new_color = color_count_temp.argmax()
    new_case = CaseFactory.from_matter_list(
        [m.copy() for m in case.matter_list if m.color == new_color], case.shape, case.background_color
    )
    return new_case


def pick_min_color(case):
    color_count_temp = case.color_count.copy()
    color_count_temp[case.background_color] = 0
    color_count_temp[color_count_temp == 0] = 100000
    new_color = color_count_temp.argmin()
    new_case = CaseFactory.from_matter_list(
        [m.copy() for m in case.matter_list if m.color == new_color], case.shape, case.background_color
    )
    return new_case
