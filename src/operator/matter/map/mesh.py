from typing import List

from src.data import Matter
from src.operator.array.map.mesh import split_by_mesh, find_mesh


def mesh(m: Matter) -> List[Matter]:
    """
    function to split a matter by mesh
    :param m: matter to split
    :return: List[Matter]
    """
    assert find_mesh(m.values) != -1
    arr_list, mesh_arr = split_by_mesh(m.values, m.background_color)
    res_list = []

    # split
    for arr, xy0 in arr_list:
        x0, y0 = xy0
        new_matter = Matter(arr, x0, y0, m.background_color)
        res_list.append(new_matter)

    # mesh
    matter_mesh = Matter(mesh_arr, background_color=m.background_color)
    matter_mesh.is_mesh = True
    res_list.append(matter_mesh)

    return res_list
