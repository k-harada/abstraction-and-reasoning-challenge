from typing import List
import numpy as np
from src.data import Problem, Case


def monotone_color(p: Problem) -> np.int:
    color_count = np.array([case.color_count() for case in p.train_y_list]).sum(axis=0)
    # ignore background
    color_count[p.background_color] = 0
    # only color other than background
    if (color_count > 0).sum() == 1:
        color_add = color_count.argmax()
    else:
        color_add = -1
    return np.int(color_add)


def new_color(p: Problem) -> List[int]:
    case_x: Case
    case_y: Case

    new_color_count = np.zeros(10, dtype=np.int)
    new_color_count_diff = np.zeros(10, dtype=np.int)
    for case_x, case_y in zip(p.train_x_list, p.train_y_list):
        y_values = case_y.repr_values()
        x_values = case_x.repr_values()
        if x_values.shape != y_values.shape:
            return []
        # find not equal, add y color
        for i in range(y_values.shape[0]):
            for j in range(y_values.shape[1]):
                if y_values[i, j] != x_values[i, j]:
                    new_color_count[y_values[i, j]] += 1
        # ignore colors in x
        x_cnt = case_x.color_count()
        for c in range(10):
            if x_cnt[c] == 0:
                new_color_count_diff[c] += new_color_count[c]
    # only one color is new
    new_color_diff = [c for c in range(10) if new_color_count_diff[c] > 0]
    if len(new_color_diff) > 0:
        return new_color_diff
    else:
        return [c for c in range(10) if new_color_count[c] > 0]


def deleted_color(p: Problem) -> List[int]:
    case_x: Case
    case_y: Case
    deleted_color_flag = np.ones(10, dtype=np.int)
    for case_x, case_y in zip(p.train_x_list, p.train_y_list):
        # color count
        y_cnt = case_y.color_count()
        x_cnt = case_x.color_count()
        for c in range(10):
            if y_cnt[c] > 0 or x_cnt[c] == 0:
                deleted_color_flag[c] = 0
    for case_x in p.test_x_list:
        x_cnt = case_x.color_count()
        for c in range(10):
            if x_cnt[c] == 0:
                deleted_color_flag[c] = 0

    return [c for c in range(10) if deleted_color_flag[c] > 0]
