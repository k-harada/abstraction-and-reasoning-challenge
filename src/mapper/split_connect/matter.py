from typing import List

from src.data import Matter
from src.mapper.split_connect.array import split_connect


def connect(m: Matter) -> List[Matter]:
    arr_list = split_connect(m.values, m.background_color)

    # avoid meaningless
    assert len(arr_list) >= 2

    return [Matter(arr, background_color=m.background_color) for arr in arr_list]
