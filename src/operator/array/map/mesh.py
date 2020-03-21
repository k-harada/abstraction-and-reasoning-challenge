import numpy as np


def find_mesh(x_arr):
    """
    :param x_arr: np.array(int8)
    :return: int8, color, -1 if no mesh
    """
    for c in range(9, -1, -1):
        compare = np.zeros(x_arr.shape, dtype=np.int8)
        # row
        sum_r = (x_arr == c).sum(axis=1)
        for i in range(x_arr.shape[0]):
            if sum_r[i] == x_arr.shape[1]:
                compare[i, :] = 1
        # col
        sum_c = (x_arr == c).sum(axis=0)
        for j in range(x_arr.shape[1]):
            if sum_c[j] == x_arr.shape[0]:
                compare[:, j] = 1

        if np.abs((compare == 1) ^ (x_arr == c)).sum() == 0 and compare.sum() > 0:
            return c
    return -1


def split_by_mesh(x_arr, background=0):
    """
    :param x_arr: np.array(int8)
    :param background: int8
    :return: List[np.array], mesh split array
    """
    c = find_mesh(x_arr)
    mesh = x_arr.copy()
    mesh[mesh != c] = background
    res_list = []
    row_split = np.where((x_arr == c).sum(axis=1) == x_arr.shape[1])[0]
    col_split = np.where((x_arr == c).sum(axis=0) == x_arr.shape[0])[0]
    # rows
    if row_split.shape[0] == 0:
        r0_list = [0]
        r1_list = [x_arr.shape[0]]
    elif row_split[0] != 0:
        if row_split[-1] != x_arr.shape[0] - 1:
            r0_list = [0] + list(row_split + 1)
            r1_list = list(row_split) + [x_arr.shape[0]]
        else:
            r0_list = [0] + list(row_split[:-1] + 1)
            r1_list = list(row_split)
    else:
        if row_split[-1] != x_arr.shape[0] - 1:
            r0_list = list(row_split + 1)
            r1_list = list(row_split[1:]) + [x_arr.shape[0]]
        else:
            r0_list = list(row_split[:-1] + 1)
            r1_list = list(row_split[1:])
    # cols
    if col_split.shape[0] == 0:
        c0_list = [0]
        c1_list = [x_arr.shape[1]]
    elif col_split[0] != 0:
        if col_split[-1] != x_arr.shape[1] - 1:
            c0_list = [0] + list(col_split + 1)
            c1_list = list(col_split) + [x_arr.shape[1]]
        else:
            c0_list = [0] + list(col_split[:-1] + 1)
            c1_list = list(col_split)
    else:
        if col_split[-1] != x_arr.shape[1] - 1:
            c0_list = list(col_split + 1)
            c1_list = list(col_split[1:]) + [x_arr.shape[1]]
        else:
            c0_list = list(col_split[:-1] + 1)
            c1_list = list(col_split[1:])

    for r0, r1 in zip(r0_list, r1_list):
        for c0, c1 in zip(c0_list, c1_list):
            res_list.append((x_arr[r0:r1, c0:c1], (r0, c0)))

    return res_list, mesh


if __name__ == "__main__":
    x = np.array([[0, 2, 0], [2, 2, 2], [4, 2, 9]])
    print(find_mesh(x))
    print(split_by_mesh(x))

