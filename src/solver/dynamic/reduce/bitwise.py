import numpy as np
from src.data import Problem, Case, Matter
from ..color.color_change import color_change


def bitwise_case(c: Case) -> Case:
    # length 2 and shape shape
    assert len(c.matter_list) == 2
    m0: Matter
    m1: Matter
    m0 = c.matter_list[0]
    m1 = c.matter_list[1]
    assert m0.shape == m1.shape == c.shape
    new_values = (m0.values != m0.background_color).astype(np.int64) + (
            m1.values != m1.background_color).astype(np.int64)
    new_case = c.copy()
    new_case.matter_list = [Matter(new_values, background_color=-1)]
    new_case.background_color = -1
    return new_case


def reduce_bitwise(p: Problem) -> Problem:
    q: Problem
    q = p.copy()
    q.train_x_list = []
    q.test_x_list = []
    q.background_color = -1

    c: Case
    for c in p.train_x_list:
        q.train_x_list.append(bitwise_case(c))
    for c in p.test_x_list:
        q.test_x_list.append(bitwise_case(c))

    return q
