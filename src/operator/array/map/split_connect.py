from collections import deque
from typing import List
import numpy as np


def neighbors(p, r, c, allow_diagonal=True):
    x, y = p
    res_list = []
    if x > 0:
        res_list.append((x - 1, y))
    if x < r - 1:
        res_list.append((x + 1, y))
    if y > 0:
        res_list.append((x, y - 1))
    if y < c - 1:
        res_list.append((x, y + 1))
    # diagonal
    if allow_diagonal:
        if x > 0 and y > 0:
            res_list.append((x - 1, y - 1))
        if x > 0 and y < c - 1:
            res_list.append((x - 1, y + 1))
        if x < r - 1 and y > 0:
            res_list.append((x + 1, y - 1))
        if x < r - 1 and y < c - 1:
            res_list.append((x + 1, y + 1))

    return res_list


def split_connect(x_arr: np.array, allow_diagonal: bool = True, background: np.int8 = 0) -> List[np.array]:
    """
    :param x_arr: np.array(int8), array to split
    :param allow_diagonal: bool, whether or not regard diagonal connected
    :param background: int8, must be one of 0-9
    :return: List[np.array(np.int8)]
    """
    res_list = []
    r, c = x_arr.shape
    con_map = np.zeros((r, c), dtype=np.int8)
    ind = 0
    for i in range(r):
        for j in range(c):
            if x_arr[i, j] != background and con_map[i, j] == 0:
                # start search
                ind += 1
                queue = deque()
                queue.append((i, j))
                con_map[i, j] = ind
                while len(queue) > 0:
                    p = queue.popleft()
                    for q in neighbors(p, r, c, allow_diagonal):
                        qi, qj = q
                        if x_arr[qi, qj] != background and con_map[qi, qj] == 0:
                            con_map[qi, qj] = ind
                            queue.append((qi, qj))

    # trivial case
    if ind == 0:
        return [x_arr.copy()]

    for s in range(ind):
        x_arr_s = x_arr.copy()
        x_arr_s[con_map != s + 1] = background
        res_list.append(x_arr_s)

    return list(sorted(res_list, key=lambda res: -(res != background).sum()))


if __name__ == "__main__":
    xx = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
    print(split_connect(xx, False))
    print(split_connect(xx, True))
    xx = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 1]])
    print(split_connect(xx, False))
    print(split_connect(xx, True))
