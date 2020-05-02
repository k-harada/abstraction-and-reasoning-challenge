from typing import List
import numpy as np
import numba


@numba.jit('i1[:, :, :](i1[:, :], i1[:, :], i1)', nopython=True)
def find_replace_rule_33_one(x_arr, y_arr, background):
    res_arr = np.int8(-1) * np.ones((10, 3, 3), dtype=np.int8)
    assert x_arr.shape == y_arr.shape

    # pick 3x3
    n_row, n_col = x_arr.shape

    for i in range(n_row):
        for j in range(n_col):
            c = x_arr[i, j]
            if c == background:
                continue
            # left up
            if i > 0 and j > 0:
                if x_arr[i - 1, j - 1] == background:
                    new_c = y_arr[i - 1, j - 1]
                    if res_arr[c, 0, 0] == np.int8(-1):
                        res_arr[c, 0, 0] = new_c
                    assert res_arr[c, 0, 0] == new_c
            # left
            if j > 0:
                if x_arr[i, j - 1] == background:
                    new_c = y_arr[i, j - 1]
                    if res_arr[c, 1, 0] == np.int8(-1):
                        res_arr[c, 1, 0] = new_c
                    assert res_arr[c, 1, 0] == new_c
            # left down
            if i < n_row - 1 and j > 0:
                if x_arr[i + 1, j - 1] == background:
                    new_c = y_arr[i + 1, j - 1]
                    if res_arr[c, 2, 0] == np.int8(-1):
                        res_arr[c, 2, 0] = new_c
                    assert res_arr[c, 2, 0] == new_c
            # up
            if i > 0:
                if x_arr[i - 1, j] == background:
                    new_c = y_arr[i - 1, j]
                    if res_arr[c, 0, 1] == np.int8(-1):
                        res_arr[c, 0, 1] = new_c
                    assert res_arr[c, 0, 1] == new_c
            # center
            new_c = y_arr[i, j]
            if res_arr[c, 1, 1] == np.int8(-1):
                res_arr[c, 1, 1] = new_c
            assert res_arr[c, 1, 1] == new_c
            # down
            if i < n_row - 1:
                if x_arr[i + 1, j] == background:
                    new_c = y_arr[i + 1, j]
                    if res_arr[c, 2, 1] == -1:
                        res_arr[c, 2, 1] = new_c
                    assert res_arr[c, 2, 1] == new_c
            # right up
            if i > 0 and j < n_col - 1:
                if x_arr[i - 1, j + 1] == background:
                    new_c = y_arr[i - 1, j + 1]
                    if res_arr[c, 0, 2] == np.int8(-1):
                        res_arr[c, 0, 2] = new_c
                    assert res_arr[c, 0, 2] == new_c
            # right
            if j < n_col - 1:
                if x_arr[i, j + 1] == background:
                    new_c = y_arr[i, j + 1]
                    if res_arr[c, 1, 2] == np.int8(-1):
                        res_arr[c, 1, 2] = new_c
                    assert res_arr[c, 1, 2] == new_c
            # right down
            if i < n_row - 1 and j < n_col - 1:
                if x_arr[i + 1, j + 1] == background:
                    new_c = y_arr[i + 1, j + 1]
                    if res_arr[c, 2, 2] == np.int8(-1):
                        res_arr[c, 2, 2] = new_c
                    assert res_arr[c, 2, 2] == new_c

    for c in range(10):
        for i in range(3):
            for j in range(3):
                if res_arr[c, i, j] == np.int8(-1):
                    res_arr[c, i, j] = background

    return res_arr


def find_replace_rule_33(x_arr_list: List[np.array], y_arr_list: List[np.array], background: np.int8 = 0) -> np.array:

    res_arr = background * np.ones((10, 3, 3), dtype=np.int8)
    n = len(x_arr_list)

    # pick 3x3
    for k in range(n):
        x_arr = x_arr_list[k]
        y_arr = y_arr_list[k]
        assert x_arr.shape == y_arr.shape
        res_arr_one = find_replace_rule_33_one(x_arr, y_arr, background)

        for c in range(10):
            for i in range(3):
                for j in range(3):
                    if res_arr_one[c, i, j] == background:
                        pass
                    elif res_arr[c, i, j] == background:
                        res_arr[c, i, j] = res_arr_one[c, i, j]
                    else:
                        assert res_arr[c, i, j] == res_arr_one[c, i, j]

    return res_arr


@numba.jit('i1[:, :](i1[:, :], i1[:, :, :], i1)', nopython=True)
def fit_replace_rule_33_one(x_arr, rule, background):
    n_row, n_col = x_arr.shape
    y_arr = background * np.ones((n_row, n_col), dtype=np.int8)

    for i in range(n_row):
        for j in range(n_col):
            c = x_arr[i, j]
            if c == background:
                continue
            # left up
            if i > 0 and j > 0:
                if x_arr[i - 1, j - 1] == background:
                    y_arr[i - 1, j - 1] = rule[c, 0, 0]
            # left
            if j > 0:
                if x_arr[i, j - 1] == background:
                    y_arr[i, j - 1] = rule[c, 1, 0]
            # left down
            if i < n_row - 1 and j > 0:
                if x_arr[i + 1, j - 1] == background:
                    y_arr[i + 1, j - 1] = rule[c, 2, 0]
            # up
            if i > 0:
                if x_arr[i - 1, j] == background:
                    y_arr[i - 1, j] = rule[c, 0, 1]
            # center
            y_arr[i, j] = rule[c, 1, 1]
            # down
            if i < n_row - 1:
                if x_arr[i + 1, j] == background:
                    y_arr[i + 1, j] = rule[c, 2, 1]
            # right up
            if i > 0 and j < n_col - 1:
                if x_arr[i - 1, j + 1] == background:
                    y_arr[i - 1, j + 1] = rule[c, 0, 2]
            # right
            if j < n_col - 1:
                if x_arr[i, j + 1] == background:
                    y_arr[i, j + 1] = rule[c, 1, 2]
            # right down
            if i < n_row - 1 and j < n_col - 1:
                if x_arr[i + 1, j + 1] == background:
                    y_arr[i + 1, j + 1] = rule[c, 2, 2]

    return y_arr


@numba.jit('i1[:, :](i1[:, :], i1[:, :], i1)', nopython=True)
def find_replace_rule_33_one_all(x_arr, y_arr, background):
    res_arr = np.int8(-1) * np.ones((3, 3), dtype=np.int8)
    assert x_arr.shape == y_arr.shape

    # pick 3x3
    n_row, n_col = x_arr.shape

    for i in range(n_row):
        for j in range(n_col):
            c = x_arr[i, j]
            if c == background:
                continue
            # left up
            if i > 0 and j > 0:
                if x_arr[i - 1, j - 1] == background:
                    new_c = y_arr[i - 1, j - 1]
                    if res_arr[0, 0] == np.int8(-1):
                        res_arr[0, 0] = new_c
                    if res_arr[0, 0] == background or new_c == background:
                        res_arr[0, 0] = background
                    else:
                        assert res_arr[0, 0] == new_c
            # left
            if j > 0:
                if x_arr[i, j - 1] == background:
                    new_c = y_arr[i, j - 1]
                    if res_arr[1, 0] == np.int8(-1):
                        res_arr[1, 0] = new_c
                    if res_arr[1, 0] == background or new_c == background:
                        res_arr[1, 0] = background
                    else:
                        assert res_arr[1, 0] == new_c
            # left down
            if i < n_row - 1 and j > 0:
                if x_arr[i + 1, j - 1] == background:
                    new_c = y_arr[i + 1, j - 1]
                    if res_arr[2, 0] == np.int8(-1):
                        res_arr[2, 0] = new_c
                    if res_arr[2, 0] == background or new_c == background:
                        res_arr[2, 0] = background
                    else:
                        assert res_arr[2, 0] == new_c
            # up
            if i > 0:
                if x_arr[i - 1, j] == background:
                    new_c = y_arr[i - 1, j]
                    if res_arr[0, 1] == np.int8(-1):
                        res_arr[0, 1] = new_c
                    if res_arr[0, 1] == background or new_c == background:
                        res_arr[0, 1] = background
                    else:
                        assert res_arr[0, 1] == new_c
            # skip center
            # down
            if i < n_row - 1:
                if x_arr[i + 1, j] == background:
                    new_c = y_arr[i + 1, j]
                    if res_arr[2, 1] == -1:
                        res_arr[2, 1] = new_c
                    if res_arr[2, 1] == background or new_c == background:
                        res_arr[2, 1] = background
                    else:
                        assert res_arr[2, 1] == new_c
            # right up
            if i > 0 and j < n_col - 1:
                if x_arr[i - 1, j + 1] == background:
                    new_c = y_arr[i - 1, j + 1]
                    if res_arr[0, 2] == np.int8(-1):
                        res_arr[0, 2] = new_c
                    if res_arr[0, 2] == background or new_c == background:
                        res_arr[0, 2] = background
                    else:
                        assert res_arr[0, 2] == new_c
            # right
            if j < n_col - 1:
                if x_arr[i, j + 1] == background:
                    new_c = y_arr[i, j + 1]
                    if res_arr[1, 2] == np.int8(-1):
                        res_arr[1, 2] = new_c
                    if res_arr[1, 2] == background or new_c == background:
                        res_arr[1, 2] = background
                    else:
                        assert res_arr[1, 2] == new_c
            # right down
            if i < n_row - 1 and j < n_col - 1:
                if x_arr[i + 1, j + 1] == background:
                    new_c = y_arr[i + 1, j + 1]
                    if res_arr[2, 2] == np.int8(-1):
                        res_arr[2, 2] = new_c
                    if res_arr[2, 2] == background or new_c == background:
                        res_arr[2, 2] = background
                    else:
                        assert res_arr[2, 2] == new_c

    for i in range(3):
        for j in range(3):
            if res_arr[i, j] == np.int8(-1):
                res_arr[i, j] = background

    return res_arr


def find_replace_rule_33_all(x_arr_list: List[np.array], y_arr_list: List[np.array], background: np.int8 = 0
                             ) -> np.array:

    res_arr = background * np.ones((3, 3), dtype=np.int8)
    n = len(x_arr_list)

    # pick 3x3
    for k in range(n):
        x_arr = x_arr_list[k]
        y_arr = y_arr_list[k]
        assert x_arr.shape == y_arr.shape
        res_arr_one = find_replace_rule_33_one_all(x_arr, y_arr, background)

        for i in range(3):
            for j in range(3):
                if res_arr_one[i, j] == background:
                    pass
                elif res_arr[i, j] == background:
                    res_arr[i, j] = res_arr_one[i, j]
                else:
                    assert res_arr[i, j] == res_arr_one[i, j]

    return res_arr


@numba.jit('i1[:, :](i1[:, :], i1[:, :], i1)', nopython=True)
def fit_replace_rule_33_one_all(x_arr, rule, background):
    n_row, n_col = x_arr.shape
    y_arr = background * np.ones((n_row, n_col), dtype=np.int8)

    for i in range(n_row):
        for j in range(n_col):
            c = x_arr[i, j]
            if c == background:
                continue
            # left up
            if i > 0 and j > 0:
                if x_arr[i - 1, j - 1] == background != rule[0, 0]:
                    y_arr[i - 1, j - 1] = rule[0, 0]
            # left
            if j > 0:
                if x_arr[i, j - 1] == background != rule[1, 0]:
                    y_arr[i, j - 1] = rule[1, 0]
            # left down
            if i < n_row - 1 and j > 0:
                if x_arr[i + 1, j - 1] == background != rule[2, 0]:
                    y_arr[i + 1, j - 1] = rule[2, 0]
            # up
            if i > 0:
                if x_arr[i - 1, j] == background != rule[0, 1]:
                    y_arr[i - 1, j] = rule[0, 1]
            # center
            y_arr[i, j] = x_arr[i, j]
            # down
            if i < n_row - 1:
                if x_arr[i + 1, j] == background != rule[2, 1]:
                    y_arr[i + 1, j] = rule[2, 1]
            # right up
            if i > 0 and j < n_col - 1:
                if x_arr[i - 1, j + 1] == background != rule[0, 2]:
                    y_arr[i - 1, j + 1] = rule[0, 2]
            # right
            if j < n_col - 1:
                if x_arr[i, j + 1] == background != rule[1, 2]:
                    y_arr[i, j + 1] = rule[1, 2]
            # right down
            if i < n_row - 1 and j < n_col - 1:
                if x_arr[i + 1, j + 1] == background != rule[2, 2]:
                    y_arr[i + 1, j + 1] = rule[2, 2]

    return y_arr


if __name__ == "__main__":

    x_list = [
        np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=np.int8),
        np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=np.int8)
    ]
    y_list = [
        np.array([[5, 0, 5], [0, 4, 0], [5, 0, 5]], dtype=np.int8),
        np.array([[4, 0, 0], [0, 5, 0], [0, 0, 0]], dtype=np.int8)
    ]
    rule_easy = find_replace_rule_33(x_list, y_list)
    print(rule_easy)
    print(fit_replace_rule_33_one(x_list[0], rule_easy, 0))
    x_list = [
        np.array([[0, 0, 0], [0, 1, 0], [0, 2, 0]], dtype=np.int8),
        np.array([[1, 0, 0], [0, 1, 0], [0, 2, 0]], dtype=np.int8)
    ]
    y_list = [
        np.array([[5, 5, 5], [5, 1, 5], [5, 2, 5]], dtype=np.int8),
        np.array([[1, 5, 5], [5, 1, 5], [5, 2, 5]], dtype=np.int8)
    ]
    rule_easy = find_replace_rule_33_all(x_list, y_list)
    print(rule_easy)
    print(fit_replace_rule_33_one_all(x_list[0], rule_easy, 0))

