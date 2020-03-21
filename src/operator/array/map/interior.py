from collections import deque
import numpy as np


def interior_dir4_zero(x_arr: np.array) -> np.array:
    """
    find interiors of x_arr that is background
    :param x_arr: np.array(bool or int8), if int8, background is 0
    :return: np.array(bool)
    """
    res = np.ones(x_arr.shape, dtype=np.bool)

    queue = deque()

    # from boundary
    for i in range(x_arr.shape[0]):
        j = 0
        res[i, j] = False
        if not x_arr[i, j]:
            queue.append((i, j))
        j = x_arr.shape[1] - 1
        res[i, j] = False
        if not x_arr[i, j]:
            queue.append((i, j))

    for j in range(x_arr.shape[1]):
        i = 0
        res[i, j] = False
        if not x_arr[i, j]:
            queue.append((i, j))
        i = x_arr.shape[0] - 1
        res[i, j] = False
        if not x_arr[i, j]:
            queue.append((i, j))

    for i in range(x_arr.shape[0]):
        for j in range(x_arr.shape[1]):
            if x_arr[i, j]:
                res[i, j] = False

    while len(queue) > 0:
        i0, j0 = queue.popleft()
        i1, j1 = min(i0 + 1, x_arr.shape[0] - 1), j0
        if res[i1, j1]:
            res[i1, j1] = False
            queue.append((i1, j1))
        i1, j1 = max(i0 - 1, 0), j0
        if res[i1, j1]:
            res[i1, j1] = False
            queue.append((i1, j1))
        i1, j1 = i0, min(j0 + 1, x_arr.shape[1] - 1)
        if res[i1, j1]:
            res[i1, j1] = False
            queue.append((i1, j1))
        i1, j1 = i0, max(j0 - 1, 0)
        if res[i1, j1]:
            res[i1, j1] = False
            queue.append((i1, j1))

    return res


if __name__ == "__main__":
    x = np.zeros((5, 5))
    x[1, :] = 1
    x[4, :] = 1
    x[:, 1] = 1
    x[:, 3] = 1
    print(interior_dir4_zero(x))
