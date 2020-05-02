import numpy as np


def find_periodicity_row(x_arr, background=0):
    """
    :param x_arr: np.array(int)
    :param background: int
    :return: int, minimum period
    """
    for p in range(1, x_arr.shape[0]):

        res = True

        i = 0
        while i < p and res:
            for j in range(x_arr.shape[1]):
                colors = np.unique(x_arr[i::p, j])
                if colors.shape[0] >= 3:
                    res = False
                    break
                elif colors.shape[0] == 2 and background not in colors:
                    res = False
                    break
            i += 1
        if res:
            return p
    return x_arr.shape[0]


def find_periodicity_col(x_arr, background=0):
    """
    :param x_arr: np.array(int)
    :param background: int
    :return: int, minimum period
    """
    return find_periodicity_row(x_arr.transpose(), background)


def fill_periodicity_row(x_arr, p, background=0):
    """
    :param x_arr: np.array(int)
    :param p: period
    :param background: int
    :return: np.array(int), filled array
    """
    # assertion
    assert x_arr.shape[0] > 0 and x_arr.shape[1] > 0

    # trivial case
    if p == x_arr.shape[0]:
        return x_arr.copy()

    y_arr = x_arr.copy()
    y_arr[x_arr == background] = -1

    for i in range(p):
        for j in range(x_arr.shape[1]):
            v = x_arr[i::p, j].max()
            if v >= 0:
                y_arr[i::p, j] = v
            else:
                y_arr[i::p, j] = background

    return y_arr


def fill_periodicity_col(x_arr, p, background=0):
    """
    :param x_arr: np.array(int), must be >= 0 otherwise returns x_arr.copy()
    :param p: period
    :param background: int
    :return: np.array(int), filled array
    """
    return fill_periodicity_row(x_arr.transpose(), p, background).transpose()


def auto_fill_row(x_arr, background=0):
    """
    :param x_arr: np.array(int), must be >= 0 otherwise returns x_arr.copy()
    :param background: int
    :return: np.array(int), filled array in row_wise
    """
    p_row = find_periodicity_row(x_arr, background)
    return fill_periodicity_row(x_arr, p_row, background)


def auto_fill_col(x_arr, background=0):
    """
    :param x_arr: np.array(int), must be >= 0 otherwise returns x_arr.copy()
    :param background: int
    :return: np.array(int), filled array in col_wise
    """
    p_col = find_periodicity_col(x_arr, background)
    return fill_periodicity_col(x_arr, p_col, background)


def auto_fill_row_col(x_arr, background=0):
    """
    :param x_arr: np.array(int), must be >= 0 otherwise returns x_arr.copy()
    :param background: int
    :return: np.array(int), filled array in row_wise and col_wise, row first
    """
    y_arr = x_arr.copy()

    iter_times = 0
    while iter_times < 10000:
        z_arr, y_arr = y_arr, auto_fill_row(y_arr, background)
        z_arr, y_arr = y_arr, auto_fill_col(y_arr, background)
        if np.abs(z_arr - y_arr).sum() == 0:
            return z_arr
        iter_times += 1
    assert iter_times == -1
    return None


if __name__ == "__main__":
    x = np.ones((5, 3), dtype=np.int)
    print(find_periodicity_row(x))
    x[1, :] = 2
    print(find_periodicity_row(x))
    x[3, :] = 2
    print(find_periodicity_row(x))
    print(find_periodicity_col(x))
    x = np.zeros((5, 3), dtype=np.int)
    print(find_periodicity_row(x))
    print(find_periodicity_row(x, -1))
    x[1, :] = 2
    print(find_periodicity_row(x))
    print(find_periodicity_row(x, -1))
    x[3, :] = 2
    print(find_periodicity_row(x))
    print(find_periodicity_row(x, -1))
    print(find_periodicity_col(x))
    print(find_periodicity_col(x, -1))

    x = np.zeros((5, 3), dtype=np.int)
    x[1, :] = 2
    print(fill_periodicity_row(x, 2))
    print(fill_periodicity_row(x, 3))
    print(fill_periodicity_col(x, 2))
    x[3, 0] = 2
    print(fill_periodicity_col(x, 2))
    x = np.zeros((5, 3), dtype=np.int)
    x[:2, :2] = 1
    x[1, 1] = 2
    print(find_periodicity_row(x))
    print(fill_periodicity_row(x, 2))
    print(auto_fill_row(x))
    print(auto_fill_row_col(x))

    x = np.ones((5, 3), dtype=np.int)
    x[1, :] = 3
    x[3:, :] = -1
    print(x)
    print(auto_fill_row_col(x, -1))
