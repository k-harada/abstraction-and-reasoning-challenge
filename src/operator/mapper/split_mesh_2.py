from typing import List
import numpy as np
from src.data import Problem, Case, Matter
from .split_mesh_normal import find_mesh, split_by_mesh


class SplitMeshTwo:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter) -> List[Matter]:
        """
        function to split a matter by mesh
        others in one and mesh
        :param m: matter to split
        :return: List[Matter]
        """
        c = find_mesh(m.values)
        assert c != -1

        arr_list, mesh_arr = split_by_mesh(m.values, m.background_color)

        # reduce
        main_values = m.background_color * np.ones(m.shape, dtype=np.int)
        for arr, xy0 in arr_list:
            x0, y0 = xy0
            main_values[x0: x0 + arr.shape[0], y0: y0 + arr.shape[1]] = arr

        # main
        matter_main = Matter(main_values, background_color=m.background_color, new=True)

        # mesh
        matter_mesh = Matter(mesh_arr, background_color=m.background_color, new=True)
        matter_mesh.is_mesh = True

        return [matter_main, matter_mesh]

    @classmethod
    def case(cls, c: Case) -> Case:
        assert len(c.matter_list) == 1
        new_case = c.copy()
        new_case.matter_list = cls.matter(c.matter_list[0])
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
