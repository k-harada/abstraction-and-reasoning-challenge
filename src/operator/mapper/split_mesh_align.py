from typing import List
import numpy as np
from src.data import Problem, Case, Matter
from .split_mesh_normal import find_mesh, split_by_mesh


class SplitMeshAlign:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter) -> List[Matter]:
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

    @classmethod
    def case(cls, c: Case) -> Case:
        assert len(c.matter_list) == 1
        new_case = c.copy()
        new_case.matter_list = cls.matter(c.matter_list[0])
        new_case.shape = new_case.matter_list[0].shape
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
