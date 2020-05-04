from typing import List
from src.data import Matter
from src.mapper.split_connect.array import split_connect as split_connect_arr


def split_connect(m: Matter, allow_diagonal: bool) -> List[Matter]:

    arr_list = split_connect_arr(m.values, allow_diagonal, m.background_color)
    # avoid meaningless
    assert len(arr_list) >= 2

    res_list = []

    for x_arr in arr_list:
        # trim
        x_sum = (x_arr != m.background_color).sum(axis=1)
        y_sum = (x_arr != m.background_color).sum(axis=0)

        min_x = min([i for i in range(x_arr.shape[0]) if x_sum[i]])
        max_x = max([i for i in range(x_arr.shape[0]) if x_sum[i]])
        min_y = min([i for i in range(x_arr.shape[1]) if y_sum[i]])
        max_y = max([i for i in range(x_arr.shape[1]) if y_sum[i]])

        new_values = x_arr[min_x:max_x + 1, min_y:max_y + 1].copy()

        res_list.append(Matter(new_values, min_x, min_y, background_color=m.background_color))

    return res_list
