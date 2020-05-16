import numpy as np
from src.data import Problem, Case, Matter


def keep_mesh_array(x_arr: np.array) -> np.array:
    y_arr = np.zeros(x_arr.shape, dtype=np.bool)
    for i in range(x_arr.shape[0]):
        if np.unique(x_arr[i, :]).shape[0] == 1:
            y_arr[i, :] = True
    for j in range(x_arr.shape[1]):
        if np.unique(x_arr[:, j]).shape[0] == 1:
            y_arr[:, j] = True
    return y_arr


class KeepMesh:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter, color_add=None) -> Matter:
        res_arr = keep_mesh_array(m.values)
        assert res_arr.sum()
        new_matter: Matter = m.copy()
        if color_add is not None:
            new_values = m.background_color * np.ones(m.shape, dtype=np.int)
            new_values[res_arr] = color_add
        else:
            new_values = m.values.copy()
            new_values[res_arr == False] = m.background_color
        new_matter.set_values(new_values)
        return new_matter

    @classmethod
    def case(cls, c: Case) -> Case:
        new_case: Case = c.copy()
        m: Matter
        new_case.matter_list = [cls.matter(m, color_add=c.color_add) for m in c.matter_list]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
