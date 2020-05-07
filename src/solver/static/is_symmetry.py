from src.data import Case, Problem
from src.reducer.fill_pattern.symmetry import is_line_symmetry_row
from src.reducer.fill_pattern.symmetry import is_line_symmetry_col

IGNORE_N_LINES = 4


def set_is_line_symmetry_row(p: Problem) -> None:

    c: Case
    for c in p.train_y_list:
        c_arr = c.repr_values()
        if c_arr.shape[0] <= IGNORE_N_LINES:
            p.is_line_symmetry_row = False
            return None
        res_arr = is_line_symmetry_row(c_arr, -1)
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
        res_arr = is_line_symmetry_col(c_arr, -1)
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
