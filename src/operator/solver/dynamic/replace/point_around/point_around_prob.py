import numpy as np
from src.data import Problem, Case, Matter
from src.operator.solver.dynamic.replace.point_around.point_around_arr import *


def fit_replace_rule_33(p: Problem) -> Problem:
    # assert
    case_x: Case
    case_y: Case

    x_arr_list = []
    y_arr_list = []

    for case_x, case_y in zip(p.train_x_list, p.train_y_list):
        # same shape
        x_values = case_x.repr_values()
        y_values = case_y.repr_values()
        assert x_values.shape == y_values.shape

        x_arr_list.append(x_values)
        y_arr_list.append(y_values)

    rule_33 = find_replace_rule_33(x_arr_list, y_arr_list, p.background_color)

    q: Problem
    q = p.copy()
    q.train_x_list = []
    q.test_x_list = []
    c_x: Case
    c_x_new: Case
    for c_x in p.train_x_list:
        c_x_new = c_x.copy()
        new_values = fit_replace_rule_33_one(c_x.repr_values(), rule_33, p.background_color)
        c_x_new.matter_list = [Matter(new_values, background_color=p.background_color, new=True)]
        q.train_x_list.append(c_x_new)

    for c_x in p.test_x_list:
        c_x_new = c_x.copy()
        new_values = fit_replace_rule_33_one(c_x.repr_values(), rule_33, p.background_color)
        c_x_new.matter_list = [Matter(new_values, background_color=p.background_color, new=True)]
        q.test_x_list.append(c_x_new)

    return q


def fit_replace_rule_33_all(p: Problem) -> Problem:
    # assert
    case_x: Case
    case_y: Case

    x_arr_list = []
    y_arr_list = []

    for case_x, case_y in zip(p.train_x_list, p.train_y_list):
        # same shape
        x_values = case_x.repr_values()
        y_values = case_y.repr_values()
        assert x_values.shape == y_values.shape

        x_arr_list.append(x_values)
        y_arr_list.append(y_values)

    rule_33 = find_replace_rule_33_all(x_arr_list, y_arr_list, p.background_color)

    q: Problem
    q = p.copy()
    q.train_x_list = []
    q.test_x_list = []
    c_x: Case
    c_x_new: Case
    for c_x in p.train_x_list:
        c_x_new = c_x.copy()
        new_values = fit_replace_rule_33_one_all(c_x.repr_values(), rule_33, p.background_color)
        c_x_new.matter_list = [Matter(new_values, background_color=p.background_color, new=True)]
        q.train_x_list.append(c_x_new)

    for c_x in p.test_x_list:
        c_x_new = c_x.copy()
        new_values = fit_replace_rule_33_one_all(c_x.repr_values(), rule_33, p.background_color)
        c_x_new.matter_list = [Matter(new_values, background_color=p.background_color, new=True)]
        q.test_x_list.append(c_x_new)

    return q


if __name__ == "__main__":
    pp = Problem.load(378, "eval")
    print(pp.eval_distance())
    qq = fit_replace_rule_33(pp)
    print(qq.eval_distance())
    print(qq)
