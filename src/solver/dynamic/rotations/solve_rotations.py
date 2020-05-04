import numpy as np

from src.data import Problem, Case, Matter
from src.transformer.array import rotations as rot_arr
from src.transformer.matter import rotations as rot_mat


operations = ["identity", "transpose", "rev_row", "rev_col", "rot_180", "rot_rev_180", "rot_90", "rot_270"]


def solve_rotations(p: Problem) -> Problem:

    case_x: Case
    case_y: Case
    m: Matter

    # assert same length
    case_x = p.train_x_list[0]
    base_len = len(case_x.matter_list)
    for case_x in p.train_x_list:
        assert base_len == len(case_x.matter_list)
    for case_x in p.test_x_list:
        assert base_len == len(case_x.matter_list)

    # search
    for case_x, case_y in zip(p.train_x_list, p.train_y_list):
        # assert same size
        assert case_x.shape == case_y.shape

        y_repr = case_y.repr_values()
        good_operations = np.ones((base_len, 8), dtype=np.int)
        for i in range(base_len):
            m = case_x.matter_list[i]
            compare = y_repr[m.x0: m.x0 + m.shape[0], m.y0: m.y0 + m.shape[1]]

            if (m.values != compare).sum():
                good_operations[i, 0] = 0
            if not m.is_square():
                good_operations[i, 1] = 0
            elif (rot_arr.transpose(m.values) != compare).sum():
                good_operations[i, 1] = 0
            if (rot_arr.rev_row(m.values) != compare).sum():
                good_operations[i, 2] = 0
            if (rot_arr.rev_col(m.values) != compare).sum():
                good_operations[i, 3] = 0
            if (rot_arr.rot_180(m.values) != compare).sum():
                good_operations[i, 4] = 0
            if not m.is_square():
                good_operations[i, 5] = 0
            elif (rot_arr.rot_rev_180(m.values) != compare).sum():
                good_operations[i, 5] = 0
            if not m.is_square():
                good_operations[i, 6] = 0
            elif (rot_arr.rot_90(m.values) != compare).sum():
                good_operations[i, 6] = 0
            if not m.is_square():
                good_operations[i, 7] = 0
            elif (rot_arr.rot_270(m.values) != compare).sum():
                good_operations[i, 7] = 0
            # some solution exists
            assert good_operations.max(axis=1).min() == 1

    # check shape for test_x
    for case_x in p.test_x_list:
        for i in range(base_len):
            m = case_x.matter_list[i]
            if not m.is_square():
                good_operations[i, 1] = 0
                good_operations[i, 5] = 0
                good_operations[i, 6] = 0
                good_operations[i, 7] = 0

    assert good_operations.max(axis=1).min() == 1

    q: Problem = p.copy()
    q.train_x_list = []
    q.test_x_list = []
    new_case_x: Case
    for case_x in p.train_x_list:
        new_case_x = case_x.copy()
        new_case_x.matter_list = []
        for i in range(base_len):
            m = case_x.matter_list[i]
            ind = good_operations[i].argmax()
            if ind == 0:
                new_case_x.matter_list.append(m.copy())
            elif ind == 1:
                new_case_x.matter_list.append(rot_mat.transpose(m))
            elif ind == 2:
                new_case_x.matter_list.append(rot_mat.rev_row(m))
            elif ind == 3:
                new_case_x.matter_list.append(rot_mat.rev_col(m))
            elif ind == 4:
                new_case_x.matter_list.append(rot_mat.rot_180(m))
            elif ind == 5:
                new_case_x.matter_list.append(rot_mat.rot_rev_180(m))
            elif ind == 6:
                new_case_x.matter_list.append(rot_mat.rot_90(m))
            elif ind == 7:
                new_case_x.matter_list.append(rot_mat.rot_270(m))
        q.train_x_list.append(new_case_x)

    for case_x in p.test_x_list:
        new_case_x = case_x.copy()
        new_case_x.matter_list = []
        for i in range(base_len):
            m = case_x.matter_list[i]
            ind = good_operations[i].argmax()
            if ind == 0:
                new_case_x.matter_list.append(m.copy())
            elif ind == 1:
                new_case_x.matter_list.append(rot_mat.transpose(m))
            elif ind == 2:
                new_case_x.matter_list.append(rot_mat.rev_row(m))
            elif ind == 3:
                new_case_x.matter_list.append(rot_mat.rev_col(m))
            elif ind == 4:
                new_case_x.matter_list.append(rot_mat.rot_180(m))
            elif ind == 5:
                new_case_x.matter_list.append(rot_mat.rot_rev_180(m))
            elif ind == 6:
                new_case_x.matter_list.append(rot_mat.rot_90(m))
            elif ind == 7:
                new_case_x.matter_list.append(rot_mat.rot_270(m))
        q.test_x_list.append(new_case_x)

    return q
