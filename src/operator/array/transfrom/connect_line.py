import numpy as np


def connect_row(x_arr: np.array, background: np.int8 = 0) -> np.array:
    """
    :param x_arr: np.array(np.int8)
    :param background: np.int8, must be one of 0-9
    :return: new_array connected, colors over color, map-apply-reduce if necessary
    """
    new_x_arr = x_arr.copy()
    for c in range(10):
        if c == background:
            continue
        # row
        for i in range(x_arr.shape[0]):
            if c in x_arr[i, :]:
                j0 = min([j for j in range(x_arr.shape[1]) if x_arr[i, j] == c])
                j1 = max([j for j in range(x_arr.shape[1]) if x_arr[i, j] == c])
                new_x_arr[i, j0:j1 + 1] = c

    return new_x_arr


def connect_col(x_arr: np.array, background: np.int8 = 0) -> np.array:
    """
    :param x_arr: np.array(np.int8)
    :param background: np.int8, must be one of 0-9
    :return: new_array connected, colors over color, map-apply-reduce if necessary
    """
    new_x_arr = x_arr.copy()
    for c in range(10):
        if c == background:
            continue
        # col
        for j in range(x_arr.shape[1]):
            if c in x_arr[:, j]:
                i0 = min([i for i in range(x_arr.shape[0]) if x_arr[i, j] == c])
                i1 = max([i for i in range(x_arr.shape[0]) if x_arr[i, j] == c])
                new_x_arr[i0:i1 + 1, j] = c

    return new_x_arr


def connect_diagonal(x_arr: np.array, background: np.int8 = 0) -> np.array:
    """
    :param x_arr: np.array(np.int8)
    :param background: np.int8, must be one of 0-9
    :return: new_array connected, colors over color, map-apply-reduce if necessary
    """
    n_row, n_col = x_arr.shape
    diff_max = max(n_row, n_col)
    sum_max = n_row + n_col
    new_x_arr = x_arr.copy()
    for c in range(10):
        if c == background:
            continue
        # right-down
        for d in range(-diff_max, diff_max):
            i_d_list = []
            for i in range(n_row):
                if 0 <= i - d < n_col:
                    if x_arr[i, i - d] == c:
                        i_d_list.append(i)
            if len(i_d_list) >= 2:
                for i in range(i_d_list[0], i_d_list[-1] + 1):
                    new_x_arr[i, i - d] = c
        # left-down
        for d in range(sum_max):
            i_d_list = []
            for i in range(n_row):
                if 0 <= d - i < n_col:
                    if x_arr[i, d - i] == c:
                        i_d_list.append(i)
            if len(i_d_list) >= 2:
                for i in range(i_d_list[0], i_d_list[-1] + 1):
                    new_x_arr[i, d - i] = c

    return new_x_arr


if __name__ == "__main__":
    x = np.array([[1, 0, 0, 1], [0, 2, 0, 0], [0, 0, 0, 0], [0, 2, 0, 3]])
    print(connect_row(x))
    x = np.array([[0, 2, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0], [0, 2, 0, 3]])
    print(connect_row(x))
    x = np.array([[1, 0, 0, 1], [0, 0, 2, 0], [0, 2, 0, 0], [3, 0, 0, 1]])
    print(connect_diagonal(x))
    x = np.array([[1, 0, 2, 1], [0, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 1]])
    print(connect_diagonal(x))
