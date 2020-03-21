from typing import List
import numpy as np


def split_color(x_arr: np.array, background: np.int8 = 0) -> List[np.array]:
    """
    :param x_arr: np.array(int8), array to split
    :param background: int8, must be one of 0-9
    :return: List[np.array(np.int8)]
    """

    res_list = []
    for c in range(10):
        if c == background:
            continue
        if (x_arr == c).sum() == 0:
            continue
        new_m_value = np.ones(x_arr.shape, dtype=np.int8) * background
        new_m_value[x_arr == c] = c
        res_list.append(new_m_value)

    if len(res_list) == 0:
        return [x_arr.copy()]
    else:
        return res_list


if __name__ == "__main__":
    x = np.array([[0, 2, 3], [2, 0, 3]])
    print(split_color(x))
