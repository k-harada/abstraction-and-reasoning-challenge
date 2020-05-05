from typing import List
import numpy as np

from src.data import Matter
from src.mapper.split_mesh.array import split_by_mesh, find_mesh


def mesh_split(m: Matter) -> List[Matter]:
    """
    function to split a matter by mesh
    split others by mesh, and mesh
    :param m: matter to split
    :return: List[Matter]
    """
    assert find_mesh(m.values) != -1
    arr_list, mesh_arr = split_by_mesh(m.values, m.background_color)
    res_list = []

    # split
    for arr, xy0 in arr_list:
        x0, y0 = xy0
        new_matter = Matter(arr, x0, y0, m.background_color, new=True)
        res_list.append(new_matter)

    # mesh
    matter_mesh = Matter(mesh_arr, background_color=m.background_color, new=True)
    matter_mesh.is_mesh = True
    res_list.append(matter_mesh)

    return res_list


def mesh_2(m: Matter) -> List[Matter]:
    """
    function to split a matter by mesh
    others in one and mesh
    :param m: matter to split
    :return: List[Matter]
    """
    c = find_mesh(m.values)
    assert c != -1

    main_values = m.values.copy()
    mesh_values = m.values.copy()

    main_values[main_values == c] = m.background_color
    mesh_values[mesh_values != c] = m.background_color

    # main
    matter_main = Matter(main_values, background_color=m.background_color, new=True)

    # mesh
    matter_mesh = Matter(mesh_values, background_color=m.background_color, new=True)
    matter_mesh.is_mesh = True

    return [matter_main, matter_mesh]


def mesh_align(m: Matter) -> List[Matter]:
    """
    function to split a matter by mesh
    others aligned and drop mesh
    :param m: matter to split
    :return: List[Matter]
    """
    assert find_mesh(m.values) != -1
    arr_list, mesh_arr = split_by_mesh(m.values, m.background_color)
    res_list = []

    # split and align
    arr_0 = arr_list[0][0]
    for arr, _ in arr_list:  # drop position
        assert arr.shape == arr_0.shape
        new_matter = Matter(arr, np.int(0), np.int(0), m.background_color, new=True)
        res_list.append(new_matter)

    return res_list
