from typing import List

from src.data import Matter


def fractal(m1: Matter, m2: Matter) -> List[Matter]:
    """
    function to expand a matter in fractal way
    :param m1: matter to be expanded
    :param m2: matter that represent expansion
    :return: List[Matter]
    """
    r1, c1 = m1.shape
    r2, c2 = m2.shape
    assert max(r1 * r2, c1 * c2) <= 30
    res_list = []

    for i in range(r2):
        for j in range(c2):
            new_matter = Matter(m1.values, i * r1, j * c1, m1.background_color)
            if not m2.bool_represents()[i, j]:
                new_matter.set_attr("bool_show", False)
            res_list.append(new_matter)

    return res_list
