from typing import List

from src.data import Matter


def fractal(m: Matter) -> List[Matter]:
    """
    function to expand a matter in fractal way
    :param m: matter to be expanded
    :return: List[Matter]
    """
    r1, c1 = m.shape
    r2, c2 = m.bool_copy.shape
    assert max(r1 * r2, c1 * c2) <= 30
    res_list = []

    for i in range(r2):
        for j in range(c2):
            new_matter = Matter(m.values, i * r1, j * c1, m.background_color)
            if not m.bool_copy[i, j]:
                new_matter.set_attr("bool_show", False)
            res_list.append(new_matter)

    return res_list
