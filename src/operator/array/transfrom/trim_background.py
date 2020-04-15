import numpy as np


def trim_background(x_arr, background=0):
    """
    :param x_arr: np.array(int8), array to trim
    :param background: int8, must be one of 0-9
    :return: List[np.array(np.int8)]
    """

    x_sum = (x_arr != background).sum(axis=1)
    y_sum = (x_arr != background).sum(axis=0)

    if x_sum.sum() == 0:
        return x_arr.copy(), (0, 0)

    min_x = min([i for i in range(x_arr.shape[0]) if x_sum[i]])
    max_x = max([i for i in range(x_arr.shape[0]) if x_sum[i]])
    min_y = min([i for i in range(x_arr.shape[1]) if y_sum[i]])
    max_y = max([i for i in range(x_arr.shape[1]) if y_sum[i]])

    new_values = x_arr[min_x:max_x + 1, min_y:max_y + 1].copy()
    return new_values, (0, 0)


if __name__ == "__main__":
    x = np.array([[3, 2, 0], [0, 1, 0], [0, 0, 0]])
    print(trim_background(x))
