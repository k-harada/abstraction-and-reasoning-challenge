import numpy as np
from src.data import Problem, Case, Matter


def fractal_arr(base_arr: np.array, shadow_arr: np.array, background: int):

    r1, c1 = base_arr.shape
    r2, c2 = shadow_arr.shape

    repr_values = np.ones((r1 * r2, c1 * c2), dtype=np.int) * background
    # basic
    if shadow_arr.dtype == 'bool':
        for i in range(r2):
            for j in range(c2):
                if shadow_arr[i, j]:
                    repr_values[(i * r1):((i + 1) * r1), (j * c1):((j + 1) * c1)] = base_arr
    else:
        for i in range(r2):
            for j in range(c2):
                add_arr = shadow_arr[i, j] * (base_arr != background).astype(np.int)
                repr_values[(i * r1):((i + 1) * r1), (j * c1):((j + 1) * c1)] = add_arr

    return repr_values


class Fractal:

    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case) -> Case:
        base_arr = c.repr_values()
        if c.shadow is None:
            shadow_arr = (base_arr != c.background_color).astype(np.bool)
        else:
            shadow_arr = c.shadow

        assert 0 < base_arr.shape[0] * shadow_arr.shape[0] <= 30
        assert 0 < base_arr.shape[1] * shadow_arr.shape[1] <= 30

        res_arr = fractal_arr(base_arr, shadow_arr, c.background_color)

        new_case: Case = c.copy()
        new_case.shape = res_arr.shape
        new_case.matter_list = [Matter(res_arr, background_color=c.background_color, new=True)]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    x = np.array([[0, 2, 3], [3, 0, 0], [1, 0, 3]], dtype=np.int)
    y = (x != 0).astype(np.bool)
    print(fractal_arr(x, y, 0))
    print(fractal_arr(x, x, 0))
