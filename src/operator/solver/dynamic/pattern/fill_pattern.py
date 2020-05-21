import numpy as np
from src.data import Problem, Case, Matter
from src.operator.solver.common.shape import is_same, is_constant


def is_pattern_y(p: Problem) -> bool:
    flag, n_row, n_col = is_constant(p)
    if not flag:
        return False
    pattern_arr = np.zeros((n_row, n_col), dtype=int)
    case_y: Case
    for i, case_y in enumerate(p.train_y_list):
        pattern_arr += (10 ** i) * case_y.repr_values()
    if np.unique(pattern_arr).shape[0] > pattern_arr.shape[0] * pattern_arr.shape[1] // 10:
        return False
    return True


def get_pattern_arr(p: Problem) -> np.array:
    flag, n_row, n_col = is_constant(p)
    assert flag
    assert is_same(p)
    pattern_arr = np.zeros((n_row, n_col), dtype=int)
    case_y: Case
    for i, case_y in enumerate(p.train_y_list):
        pattern_arr += (10 ** i) * case_y.repr_values()
    return pattern_arr


class FillPattern:

    def __init__(self):
        pass

    @classmethod
    def array(cls, x_arr: np.array, pattern_arr: np.array, color_del: int) -> np.array:
        assert x_arr.shape == pattern_arr.shape
        new_x_arr = x_arr.copy()
        # equal or background
        for v in np.unique(pattern_arr):
            v_unique = np.unique(x_arr[pattern_arr == v])
            assert 1 <= v_unique.shape[0] <= 2
            if v_unique.shape[0] == 2:
                if v_unique[0] == color_del:
                    new_color = v_unique[1]
                elif v_unique[1] == color_del:
                    new_color = v_unique[0]
                else:
                    raise AssertionError
                # set values
                new_x_arr[pattern_arr == v] = new_color

        return new_x_arr

    @classmethod
    def case(cls, c_x: Case, pattern_arr: np.array) -> Case:
        x_values = c_x.repr_values()
        if c_x.color_delete is None:
            new_x_values = cls.array(x_values, pattern_arr, c_x.background_color)
        else:
            new_x_values = cls.array(x_values, pattern_arr, c_x.color_delete)
        new_case: Case = c_x.copy()
        new_case.matter_list = [Matter(new_x_values, new=True)]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        assert p.is_pattern
        pattern_arr = get_pattern_arr(p)

        q: Problem = p.copy()
        q.train_x_list = []
        q.test_x_list = []

        q.train_x_list = [cls.case(c_x, pattern_arr) for c_x in p.train_x_list]
        q.test_x_list = [cls.case(c_x, pattern_arr) for c_x in p.test_x_list]
        return q


if __name__ == "__main__":
    import time
    pp = Problem.load(111, "eval")
    pp.is_pattern = True
    t0 = time.time()
    qq = FillPattern.problem(pp)
    print(time.time() - t0)
    print(qq)

