from typing import List

from src.data import Matter
from src.mapper.split_color.array import split_color as split_color_arr


def split_color(m: Matter) -> List[Matter]:
    arr_list = split_color_arr(m.values, m.background_color)

    # avoid meaningless
    assert len(arr_list) >= 2

    return [Matter(arr, background_color=m.background_color) for arr in arr_list]
