from typing import List

from src.data import Matter
from src.operator.array.map.split_color import split_color


def color(m: Matter) -> List[Matter]:
    arr_list = split_color(m.values, m.background_color)

    # avoid meaningless
    assert len(arr_list) >= 2

    return [Matter(arr, background_color=m.background_color) for arr in arr_list]
