from src.data import Case, Problem
from src.operator.transformer.reducer.fill_pattern.symmetry_delete import is_line_symmetry_row
from src.operator.transformer.reducer.fill_pattern.symmetry_delete import is_line_symmetry_col
from src.operator.transformer.reducer.fill_pattern.symmetry_rot import is_rot_symmetry_point, is_rot_symmetry_valley


IGNORE_N_LINES = 4


def set_is_line_symmetry_row(p: Problem) -> None:

    c: Case
    for c in p.train_y_list:
        c_arr = c.repr_values()
        if c_arr.shape[0] <= IGNORE_N_LINES:
            p.is_line_symmetry_row = False
            return None
        if c.color_add is None:
            res_arr = is_line_symmetry_row(c_arr, -1)
        else:
            res_arr = is_line_symmetry_row(c_arr, c.color_add)
        # print(res_arr)
        if c_arr.shape[0] < 8:
            # must be all
            if c_arr.shape[0] % 2 == 0:
                if res_arr[c_arr.shape[0] // 2 - 1, 1] < 0:
                    p.is_line_symmetry_row = False
                    return None
            else:
                if res_arr[c_arr.shape[0] // 2, 0] < 0:
                    p.is_line_symmetry_row = False
                    return None
        elif res_arr[3:-3, :].max() < 0:
            p.is_line_symmetry_row = False
            return None
    p.is_line_symmetry_row = True
    return None


def set_is_line_symmetry_col(p: Problem) -> None:

    c: Case
    for c in p.train_y_list:
        c_arr = c.repr_values()
        if c_arr.shape[1] <= IGNORE_N_LINES:
            p.is_line_symmetry_col = False
            return None
        if c.color_add is None:
            res_arr = is_line_symmetry_col(c_arr, -1)
        else:
            res_arr = is_line_symmetry_col(c_arr, c.color_add)
        # print(res_arr)
        if c_arr.shape[1] < 8:
            # must be all
            if c_arr.shape[1] % 2 == 0:
                if res_arr[c_arr.shape[1] // 2 - 1, 1] < 0:
                    p.is_line_symmetry_col = False
                    return None
            else:
                if res_arr[c_arr.shape[1] // 2, 0] < 0:
                    p.is_line_symmetry_col = False
                    return None
        elif res_arr[3:-3, :].max() < 0:
            p.is_line_symmetry_col = False
            return None
    p.is_line_symmetry_col = True
    return None


def set_is_rot_symmetry(p: Problem) -> None:

    c: Case
    for c in p.train_y_list:
        c_arr = c.repr_values()
        if c_arr.shape[0] <= IGNORE_N_LINES or c_arr.shape[1] <= IGNORE_N_LINES:
            p.is_rot_symmetry = False
            return None
        if c.color_add is None:
            res_arr_1 = is_rot_symmetry_point(c_arr, -1)
            res_arr_2 = is_rot_symmetry_valley(c_arr, -1)
        else:
            res_arr_1 = is_rot_symmetry_point(c_arr, c.color_add)
            res_arr_2 = is_rot_symmetry_valley(c_arr, c.color_add)
        # print(c.color_add)
        # must be in center
        # print(res_arr_1, res_arr_2)
        res_arr_1[:res_arr_1.shape[0] // 3, :] = -1
        res_arr_1[-res_arr_1.shape[0] // 3:, :] = -1
        res_arr_1[:, :res_arr_1.shape[1] // 3] = -1
        res_arr_1[:, -res_arr_1.shape[1] // 3:] = -1
        res_arr_2[:res_arr_2.shape[0] // 3, :] = -1
        res_arr_2[-res_arr_2.shape[0] // 3:, :] = -1
        res_arr_2[:, :res_arr_2.shape[1] // 3] = -1
        res_arr_2[:, -res_arr_2.shape[1] // 3:] = -1
        # print(res_arr_1, res_arr_2)
        if max(res_arr_1.max(), res_arr_2.max()) <= 20:
            p.is_rot_symmetry = False
            return None
    p.is_rot_symmetry = True
    return None
