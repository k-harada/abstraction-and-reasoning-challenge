import numpy as np
from src.data import Problem, Case, Matter
from src.operator.solver.common.shape import is_division, is_constant


def divide(p: Problem) -> Problem:

    flag, d_row, d_col = is_division(p)
    flag_n = False

    if not flag:
        flag, nc_row, nc_col = is_constant(p)
        flag_n = True
        cnt_arr = np.zeros((2, 2), dtype=int)
    else:
        cnt_arr = np.zeros((d_row, d_col), dtype=int)
    assert flag

    q: Problem
    q = p.copy()
    q.train_x_list = []
    q.test_x_list = []
    c_x: Case
    c_x_new: Case

    # find best
    for c_x, c_y in zip(p.train_x_list, p.train_y_list):
        base_values = c_x.repr_values()
        res_values = c_y.repr_values()
        n_row, n_col = base_values.shape
        if flag_n:
            assert n_row % nc_row == 0
            assert n_col % nc_col == 0
            d_row = n_row // nc_row
            d_col = n_col // nc_col
        q_row, q_col = n_row // d_row, n_col // d_col
        # print(d_row, d_col)
        # is_division -> any
        if not flag_n:
            for i in range(d_row):
                for j in range(d_col):
                    if (base_values[i * q_row:(i + 1) * q_row, j * q_col:(j + 1) * q_col] == res_values).min():
                        cnt_arr[i, j] += 1
        # is_constant -> 4 corners
        else:
            if (base_values[:q_row, :q_col] == res_values).min():
                cnt_arr[0, 0] += 1
            if (base_values[:q_row, -q_col:] == res_values).min():
                cnt_arr[0, 1] += 1
            if (base_values[-q_row:, :q_col] == res_values).min():
                cnt_arr[1, 0] += 1
            if (base_values[-q_row:, -q_col:] == res_values).min():
                cnt_arr[1, 1] += 1
    # print(cnt_arr)
    # fit
    i0, j0 = -1, -1
    for i in range(cnt_arr.shape[0]):
        for j in range(cnt_arr.shape[1]):
            if cnt_arr[i, j] == len(p.train_x_list):
                i0, j0 = i, j
                break
        if i0 >= 0:
            break
    assert i0 >= 0 and j0 >= 0

    # fit
    for c_x in p.train_x_list:
        base_values = c_x.repr_values()
        n_row, n_col = base_values.shape
        if flag_n:
            assert n_row % nc_row == 0
            assert n_col % nc_col == 0
            d_row = n_row // nc_row
            d_col = n_col // nc_col
        q_row, q_col = n_row // d_row, n_col // d_col

        # is_division -> any
        if not flag_n:
            new_values = base_values[i0 * q_row:(i0 + 1) * q_row, j0 * q_col:(j0 + 1) * q_col].copy()
        # is_constant -> 4 corners
        else:
            if i0 == 0 and j0 == 0:
                new_values = base_values[:q_row, :q_col].copy()
            elif i0 == 0 and j0 == 1:
                new_values = base_values[:q_row, -q_col:].copy()
            elif i0 == 1 and j0 == 0:
                new_values = base_values[-q_row:, :q_col].copy()
            else:
                new_values = base_values[-q_row:, -q_col:].copy()

        c_x_new = c_x.copy()
        c_x_new.shape = q_row, q_col
        c_x_new.matter_list = [Matter(new_values, background_color=c_x.background_color, new=True)]
        q.train_x_list.append(c_x_new)

    for c_x in p.test_x_list:
        base_values = c_x.repr_values()
        n_row, n_col = base_values.shape
        if flag_n:
            assert n_row % nc_row == 0
            assert n_col % nc_col == 0
            d_row = n_row // nc_row
            d_col = n_col // nc_col
        q_row, q_col = n_row // d_row, n_col // d_col

        # is_division -> any
        if not flag_n:
            new_values = base_values[i0 * q_row:(i0 + 1) * q_row, j0 * q_col:(j0 + 1) * q_col].copy()
        # is_constant -> 4 corners
        else:
            if i0 == 0 and j0 == 0:
                new_values = base_values[:q_row, :q_col].copy()
            elif i0 == 0 and j0 == 1:
                new_values = base_values[:q_row, -q_col:].copy()
            elif i0 == 1 and j0 == 0:
                new_values = base_values[-q_row:, :q_col].copy()
            else:
                new_values = base_values[-q_row:, -q_col:].copy()

        c_x_new = c_x.copy()
        c_x_new.shape = q_row, q_col
        c_x_new.matter_list = [Matter(new_values, background_color=c_x.background_color, new=True)]
        q.test_x_list.append(c_x_new)

    return q


if __name__ == "__main__":
    pp = Problem.load(66)
    qq = divide(pp)
    print(qq)
