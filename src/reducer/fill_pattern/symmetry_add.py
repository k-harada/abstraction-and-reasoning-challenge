import numpy as np
from src.data import Problem, Case, Matter


def is_line_symmetry_row_strict(x_arr: np.array, background: np.int) -> np.array:

    # center row
    res_arr = np.zeros((x_arr.shape[0], 2), dtype=np.int64)
    for i0 in range(x_arr.shape[0]):
        res = 0
        for i in range(1, i0 + 1):
            if i0 + i >= x_arr.shape[0]:
                break
            for j in range(x_arr.shape[1]):
                if x_arr[i0 - i, j] == x_arr[i0 + i, j] != background:
                    res += 1
                elif x_arr[i0 - i, j] != x_arr[i0 + i, j]:
                    res = -1
                    break
            if res == -1:
                break
        res_arr[i0, 0] = res

    # mid row
    for i0 in range(x_arr.shape[0]):
        res = 0
        for i in range(i0 + 1):
            if i0 + 1 + i >= x_arr.shape[0]:
                break
            for j in range(x_arr.shape[1]):
                if x_arr[i0 - i, j] == x_arr[i0 + 1 + i, j] != background:
                    res += 1
                elif x_arr[i0 - i, j] != x_arr[i0 + 1 + i, j]:
                    res = -1
                    break
            if res == -1:
                break
        res_arr[i0, 1] = res

    return res_arr


def is_line_symmetry_col_strict(x_arr: np.array, background: np.int) -> np.array:
    return is_line_symmetry_row_strict(x_arr.transpose(), background)


def fill_symmetry_row(x_arr: np.array, background: np.int, i0: np.int, center: bool) -> np.array:

    res_arr = x_arr.copy()

    if center:
        # center row exists
        for i in range(1, i0 + 1):
            if i0 + i >= x_arr.shape[0]:
                break
            for j in range(x_arr.shape[1]):
                if x_arr[i0 + i, j] != background:
                    res_arr[i0 - i, j] = x_arr[i0 + i, j]
                elif x_arr[i0 - i, j] != background:
                    res_arr[i0 + i, j] = x_arr[i0 - i, j]

    else:
        # mid row
        for i in range(i0 + 1):
            if i0 + 1 + i >= x_arr.shape[0]:
                break
            for j in range(x_arr.shape[1]):
                if x_arr[i0 + 1 + i, j] != background:
                    res_arr[i0 - i, j] = x_arr[i0 + 1 + i, j]
                elif x_arr[i0 - i, j] != background:
                    res_arr[i0 + 1 + i, j] = x_arr[i0 - i, j]

    return res_arr


def fill_symmetry_col(x_arr: np.array, background: np.int, j0: np.int, center: bool) -> np.array:

    return fill_symmetry_row(x_arr.transpose(), background, j0, center).transpose()


class AutoFillLineSymmetryAdd:

    def __init__(self):
        pass

    @classmethod
    def auto_fill_symmetry_row(cls, x_arr: np.array, background: np.int = 0) -> np.array:
        assert x_arr.shape[0] > 0 and x_arr.shape[1] > 0
        max_c = -1
        res_max = 0
        for color in range(10):
            if color == background:
                continue
            w_arr = x_arr.copy()
            w_arr[x_arr == color] = background
            res_arr = is_line_symmetry_row_strict(w_arr, background)
            if res_arr.max() > res_max:
                res_max = res_arr.max()
                max_c = color

        if max_c == -1:
            return x_arr

        # max_c
        w_arr = x_arr.copy()
        w_arr[x_arr == max_c] = background
        res_cnt_arr = is_line_symmetry_row_strict(w_arr, background)

        for i in range(x_arr.shape[0]):
            if res_cnt_arr[i, 0] == res_max:
                return fill_symmetry_row(x_arr, background, i, True)
            elif res_cnt_arr[i, 1] == res_max:
                return fill_symmetry_row(x_arr, background, i, False)

        raise AssertionError

    @classmethod
    def auto_fill_symmetry_col(cls, x_arr: np.array, background: np.int = 0) -> np.array:
        assert x_arr.shape[0] > 0 and x_arr.shape[1] > 0
        max_c = -1
        res_max = 0
        for color in range(10):
            if color == background:
                continue
            w_arr = x_arr.copy()
            w_arr[x_arr == color] = background
            res_arr = is_line_symmetry_col_strict(w_arr, background)
            if res_arr.max() > res_max:
                res_max = res_arr.max()
                max_c = color

        if max_c == -1:
            return x_arr

        # max_c
        w_arr = x_arr.copy()
        w_arr[x_arr == max_c] = background
        res_cnt_arr = is_line_symmetry_col_strict(w_arr, background)

        for j in range(x_arr.shape[1]):
            if res_cnt_arr[j, 0] == res_max:
                return fill_symmetry_col(x_arr, background, j, True)
            elif res_cnt_arr[j, 1] == res_max:
                return fill_symmetry_col(x_arr, background, j, False)

        raise AssertionError

    @classmethod
    def auto_fill_symmetry_row_col(cls, x_arr: np.array, background: np.int = 0) -> np.array:
        assert x_arr.shape[0] > 0 and x_arr.shape[1] > 0
        max_c = -1
        res_max = 0
        for color in range(10):
            if color == background:
                continue
            w_arr = x_arr.copy()
            w_arr[x_arr == color] = background
            res_arr_row = is_line_symmetry_row_strict(w_arr, background)
            res_arr_col = is_line_symmetry_col_strict(w_arr, background)
            if res_arr_row.max() * res_arr_col.max() > res_max:
                res_max = res_arr_row.max() * res_arr_col.max()
                max_c = color

        if max_c == -1:
            return x_arr

        # max_c
        w_arr = x_arr.copy()
        w_arr[x_arr == max_c] = background
        # print(max_c)
        res_cnt_arr_row = is_line_symmetry_row_strict(w_arr, background)
        res_cnt_arr_col = is_line_symmetry_col_strict(w_arr, background)
        # print(res_cnt_arr_row, res_cnt_arr_col)
        res_max_row, res_max_col = res_cnt_arr_row.max(), res_cnt_arr_col.max()
        y_arr = x_arr * 0

        for i in range(x_arr.shape[0]):
            if res_cnt_arr_row[i, 0] == res_max_row:
                y_arr = fill_symmetry_row(x_arr, background, i, True)
                break
            elif res_cnt_arr_row[i, 1] == res_max_row:
                y_arr = fill_symmetry_row(x_arr, background, i, False)
                break

        assert y_arr.sum()
        # print(y_arr)

        for j in range(x_arr.shape[1]):
            if res_cnt_arr_col[j, 0] == res_max_col:
                return fill_symmetry_col(y_arr, background, j, True)
            elif res_cnt_arr_col[j, 1] == res_max_col:
                return fill_symmetry_col(y_arr, background, j, False)

        raise AssertionError

    @classmethod
    def case_row(cls, c: Case) -> Case:
        new_case = c.copy()
        new_values = cls.auto_fill_symmetry_row(c.repr_values(), c.background_color)
        new_case.matter_list = [Matter(new_values, background_color=c.background_color, new=True)]
        return new_case

    @classmethod
    def case_col(cls, c: Case) -> Case:
        new_case = c.copy()
        new_values = cls.auto_fill_symmetry_col(c.repr_values(), c.background_color)
        new_case.matter_list = [Matter(new_values, background_color=c.background_color, new=True)]
        return new_case

    @classmethod
    def case_row_col(cls, c: Case) -> Case:
        new_case = c.copy()
        new_values = cls.auto_fill_symmetry_row_col(c.repr_values(), c.background_color)
        new_case.matter_list = [Matter(new_values, background_color=c.background_color, new=True)]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        if p.is_line_symmetry_row and p.is_line_symmetry_col:
            q: Problem = p.copy()
            q.train_x_list = [cls.case_row_col(c) for c in p.train_x_list]
            q.test_x_list = [cls.case_row_col(c) for c in p.test_x_list]
        elif p.is_line_symmetry_row:
            q: Problem = p.copy()
            q.train_x_list = [cls.case_row(c) for c in p.train_x_list]
            q.test_x_list = [cls.case_row(c) for c in p.test_x_list]
        elif p.is_line_symmetry_col:
            q: Problem = p.copy()
            q.train_x_list = [cls.case_col(c) for c in p.train_x_list]
            q.test_x_list = [cls.case_col(c) for c in p.test_x_list]
        else:
            raise AssertionError
        return q


if __name__ == "__main__":
    import time
    x = np.array([[1, 2, 3], [4, 2, 3], [1, 0, 3]])
    t0 = time.time()
    print(is_line_symmetry_row_strict(x, 0))
    print(time.time() - t0)
    t0 = time.time()
    print(is_line_symmetry_col_strict(x, 0))
    print(time.time() - t0)
    t0 = time.time()
    print(fill_symmetry_row(x, 0, 1, True))
    print(time.time() - t0)
    x = np.array([[1, 2, 3], [4, 2, 3], [0, 0, 0], [0, 0, 0]])
    print(is_line_symmetry_row_strict(x, 0))
    print(is_line_symmetry_col_strict(x, 0))
    print(fill_symmetry_row(x, 0, 1, False))
    y = x.transpose()
    print(y)
    print(fill_symmetry_col(y, 0, 1, False))
