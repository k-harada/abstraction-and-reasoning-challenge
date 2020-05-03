from typing import Tuple
import numpy as np


def is_line_symmetry_row(x_arr: np.array, background: np.int = 0) -> Tuple[np.array, np.array]:

    # center row
    res_arr_center = np.zeros(x_arr.shape[0], dtype=np.bool)
    for i0 in range(x_arr.shape[0]):
        res_flag = True
        for i in range(1, i0 + 1):
            if i0 + i >= x_arr.shape[0]:
                break
            diff_arr = (x_arr[i0 - i, :] != x_arr[i0 + i, :]) * (
                    x_arr[i0 - i, :] != background) * (x_arr[i0 + i, :] != background)
            # print(i, i0, diff_arr.sum())
            if diff_arr.sum():
                res_flag = False
                break
        res_arr_center[i0] = res_flag

    # mid row
    res_arr_mid = np.zeros(x_arr.shape[0], dtype=np.bool)
    for i0 in range(x_arr.shape[0]):
        res_flag = True
        for i in range(i0 + 1):
            if i0 + 1 + i >= x_arr.shape[0]:
                break
            diff_arr = (x_arr[i0 - i, :] != x_arr[i0 + 1 + i, :]) * (
                    x_arr[i0 - i, :] != background) * (x_arr[i0 + 1 + i, :] != background)
            # print(i, i0, diff_arr.sum())
            if diff_arr.sum():
                res_flag = False
                break
        res_arr_mid[i0] = res_flag

    return res_arr_center, res_arr_mid


if __name__ == "__main__":
    x = np.array([[1, 2, 3], [4, 2, 3], [5, 2, 3]])
    print(is_line_symmetry_row(x))
