import numpy as np


def point_cross_cnt_arr(x_arr: np.array, y_arr: np.array, c: int) -> np.array:

    base_arr = (x_arr == c)
    compare_arr = (y_arr == c)
    # row
    sum_i = base_arr.sum(axis=1, keepdims=True)
    row_loss = (sum_i != compare_arr).astype(int).sum()
    # col
    sum_j = base_arr.sum(axis=0, keepdims=True)
    col_loss = (sum_j != compare_arr).astype(int).sum()
    # cross
    cross_arr = np.minimum(sum_i + sum_j, 1)
    cross_loss = (cross_arr != compare_arr).astype(int).sum()
    # delete
    del_loss = compare_arr.astype(int).sum()
    # keep
    keep_loss = (base_arr != compare_arr).astype(int).sum()

    return np.array([del_loss, keep_loss, row_loss, col_loss, cross_loss])


def point_cross_fit_arr(x_arr: np.array, c: int, op: int) -> np.array:

    if op == 0:
        return np.zeros(x_arr.shape, dtype=np.int)
    base_arr = (x_arr == c)
    # row
    sum_i = base_arr.sum(axis=1, keepdims=True)
    # col
    sum_j = base_arr.sum(axis=0, keepdims=True)
    # cross
    cross_arr = np.minimum(sum_i + sum_j, 1)

    if op == 1:
        return base_arr.astype(np.int)
    elif op == 4:
        return cross_arr
    elif op == 2:
        return sum_i @ np.ones((1, x_arr.shape[1]), dtype=np.int)
    else:  # op == 3
        return np.ones((x_arr.shape[0], 1), dtype=np.int) @ sum_j


if __name__ == "__main__":
    # point_cross_cnt_arr
    x = np.array([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
    y = np.array([[0, 1, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0]])
    print(point_cross_cnt_arr(x, y, 1))
    x = np.array([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
    y = np.array([[0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0]])
    print(point_cross_cnt_arr(x, y, 1))
    x = np.array([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    y = np.array([[0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0], [0, 0, 0, 0]])
    print(point_cross_cnt_arr(x, y, 1))
    x = np.array([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    y = np.array([[0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 0], [0, 1, 0, 0]])
    print(point_cross_cnt_arr(x, y, 1))

    # point_cross_fit_arr
    x = np.array([[0, 5, 0, 0], [0, 1, 0, 0], [0, 0, 7, 0]])
    print(point_cross_fit_arr(x, 1, 0))
    print(point_cross_fit_arr(x, 1, 1))
    print(point_cross_fit_arr(x, 1, 2))
    print(point_cross_fit_arr(x, 1, 3))
    print(point_cross_fit_arr(x, 1, 4))


