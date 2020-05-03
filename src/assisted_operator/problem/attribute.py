from typing import Tuple
import numpy as np
from src.data import Problem
from src.assisted_operator.case import attribute as attr_case


def set_color_add(p: Problem, color_add: int) -> Problem:
    q: Problem
    q = p.copy()
    q.color_add = color_add
    q.train_x_list = [attr_case.set_color_add(x, color_add) for x in p.train_x_list]
    q.test_x_list = [attr_case.set_color_add(x, color_add) for x in p.test_x_list]
    q.train_y_list = [x for x in p.train_y_list]
    return q


def set_is_pattern(p: Problem, is_pattern: bool) -> Problem:
    q: Problem
    q = p.copy()
    q.is_pattern = is_pattern
    return q


def set_shape(p: Problem, new_shape: Tuple[int, int]) -> Problem:
    q: Problem
    q = p.copy()
    q.train_x_list = [attr_case.set_shape(x, new_shape) for x in p.train_x_list]
    q.test_x_list = [attr_case.set_shape(x, new_shape) for x in p.test_x_list]
    q.train_y_list = [x for x in p.train_y_list]
    return q
