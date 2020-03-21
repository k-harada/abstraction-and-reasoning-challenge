import numpy as np

from src.data import Case, Matter
from src.operator.array import reduce as array_reduce


def bitwise_or(c: Case) -> Case:
    assert len(c.matter_list) >= 2
    m0: Matter
    m1: Matter
    m0, m1 = c.matter_list[:2]
    new_value = array_reduce.bitwise_or(m0.bool_represents, m1.bool_represents).astype(np.int8) * c.color_a
    new_case = Case()
    new_case.initialize(new_value, c.background_color)
    return new_case


def bitwise_and(c: Case) -> Case:
    assert len(c.matter_list) >= 2
    m0: Matter
    m1: Matter
    m0, m1 = c.matter_list[:2]
    new_value = array_reduce.bitwise_and(m0.bool_represents, m1.bool_represents).astype(np.int8) * c.color_a
    new_case = Case()
    new_case.initialize(new_value, c.background_color)
    return new_case


def bitwise_xor(c: Case) -> Case:
    assert len(c.matter_list) >= 2
    m0: Matter
    m1: Matter
    m0, m1 = c.matter_list[:2]
    new_value = array_reduce.bitwise_xor(m0.bool_represents, m1.bool_represents).astype(np.int8) * c.color_a
    new_case = Case()
    new_case.initialize(new_value, c.background_color)
    return new_case


def bitwise_not_xor(c: Case) -> Case:
    assert len(c.matter_list) >= 2
    m0: Matter
    m1: Matter
    m0, m1 = c.matter_list[:2]
    new_value = array_reduce.bitwise_not_xor(m0.bool_represents, m1.bool_represents).astype(np.int8) * c.color_a
    new_case = Case()
    new_case.initialize(new_value, c.background_color)
    return new_case


def bitwise_not_or(c: Case) -> Case:
    assert len(c.matter_list) >= 2
    m0: Matter
    m1: Matter
    m0, m1 = c.matter_list[:2]
    new_value = array_reduce.bitwise_not_or(m0.bool_represents, m1.bool_represents).astype(np.int8) * c.color_a
    new_case = Case()
    new_case.initialize(new_value, c.background_color)
    return new_case


def bitwise_not_and(c: Case) -> Case:
    assert len(c.matter_list) >= 2
    m0: Matter
    m1: Matter
    m0, m1 = c.matter_list[:2]
    new_value = array_reduce.bitwise_not_and(m0.bool_represents, m1.bool_represents).astype(np.int8) * c.color_a
    new_case = Case()
    new_case.initialize(new_value, c.background_color)
    return new_case
