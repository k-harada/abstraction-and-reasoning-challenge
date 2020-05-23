import numpy as np
import numba
from src.data import Problem, Case, Matter


@numba.jit('i8[:, :](i8[:, :], i8)', nopython=True)
def is_rot_symmetry_point(x_arr: np.array, background: np.int) -> np.array:

    res_arr = np.zeros(x_arr.shape, dtype=np.int64)

    # center point
    for i0 in range(x_arr.shape[0]):
        for j0 in range(x_arr.shape[1]):

            # right-down
            x_arr_1 = x_arr[i0:, j0:]
            # right-up
            x_arr_2 = x_arr[i0::-1, j0:].transpose()
            # left-up
            x_arr_3 = x_arr[i0::-1, j0::-1]
            # left-down
            x_arr_4 = x_arr[i0:, j0::-1].transpose()

            new_shape_0 = max([x_arr_1.shape[0], x_arr_2.shape[0], x_arr_3.shape[0], x_arr_4.shape[0]])
            new_shape_1 = max([x_arr_1.shape[1], x_arr_2.shape[1], x_arr_3.shape[1], x_arr_4.shape[1]])

            x_arr_1_exp = background * np.ones((new_shape_0, new_shape_1), dtype=np.int64)
            x_arr_1_exp[:x_arr_1.shape[0], :x_arr_1.shape[1]] = x_arr_1
            x_arr_2_exp = background * np.ones((new_shape_0, new_shape_1), dtype=np.int64)
            x_arr_2_exp[:x_arr_2.shape[0], :x_arr_2.shape[1]] = x_arr_2
            x_arr_3_exp = background * np.ones((new_shape_0, new_shape_1), dtype=np.int64)
            x_arr_3_exp[:x_arr_3.shape[0], :x_arr_3.shape[1]] = x_arr_3
            x_arr_4_exp = background * np.ones((new_shape_0, new_shape_1), dtype=np.int64)
            x_arr_4_exp[:x_arr_4.shape[0], :x_arr_4.shape[1]] = x_arr_4

            # break if gap
            if ((x_arr_1_exp != x_arr_2_exp) * (x_arr_1_exp != background) * (x_arr_2_exp != background)).sum():
                res_arr[i0, j0] = -2
                continue
            # break if gap
            if ((x_arr_1_exp != x_arr_3_exp) * (x_arr_1_exp != background) * (x_arr_3_exp != background)).sum():
                res_arr[i0, j0] = -2
                continue
            # break if gap
            if ((x_arr_1_exp != x_arr_4_exp) * (x_arr_1_exp != background) * (x_arr_4_exp != background)).sum():
                res_arr[i0, j0] = -2
                continue
            # break if gap
            if ((x_arr_2_exp != x_arr_3_exp) * (x_arr_2_exp != background) * (x_arr_3_exp != background)).sum():
                res_arr[i0, j0] = -2
                continue
            # break if gap
            if ((x_arr_2_exp != x_arr_4_exp) * (x_arr_2_exp != background) * (x_arr_4_exp != background)).sum():
                res_arr[i0, j0] = -2
                continue
            # break if gap
            if ((x_arr_3_exp != x_arr_4_exp) * (x_arr_3_exp != background) * (x_arr_4_exp != background)).sum():
                res_arr[i0, j0] = -2
                continue

            score_arr = (x_arr_1_exp != background).astype(np.int64) + (x_arr_2_exp != background).astype(np.int64) + \
                        (x_arr_3_exp != background).astype(np.int64) + (x_arr_4_exp != background).astype(np.int64)

            res_arr[i0, j0] = (score_arr * (score_arr - 1)).sum()

            # center should be same
            if 1 <= score_arr[0, 1] <= 2:
                flag_todo = 1
            elif 1 <= score_arr[1, 1] <= 2:
                flag_todo = 1
            else:
                flag_todo = 0
            if flag_todo == 1:
                # unless it is the center
                if i0 == j0 == x_arr.shape[0] // 2 and x_arr.shape[0] == x_arr.shape[1] and x_arr.shape[0] % 2 == 1:
                    pass
                else:
                    res_arr[i0, j0] = -2

    return res_arr // 2


@numba.jit('i8[:, :](i8[:, :], i8)', nopython=True)
def is_rot_symmetry_valley(x_arr: np.array, background: np.int) -> np.array:

    res_arr = np.zeros(x_arr.shape, dtype=np.int64)
    res_arr[-1, :] = -1
    res_arr[:, -1] = -1

    # center point
    for i0 in range(x_arr.shape[0] - 1):
        for j0 in range(x_arr.shape[1] - 1):

            # right-down
            x_arr_1 = x_arr[i0 + 1:, j0 + 1:]
            # right-up
            x_arr_2 = x_arr[i0::-1, j0 + 1:].transpose()
            # left-up
            x_arr_3 = x_arr[i0::-1, j0::-1]
            # left-down
            x_arr_4 = x_arr[i0 + 1:, j0::-1].transpose()

            new_shape_0 = max([x_arr_1.shape[0], x_arr_2.shape[0], x_arr_3.shape[0], x_arr_4.shape[0]])
            new_shape_1 = max([x_arr_1.shape[1], x_arr_2.shape[1], x_arr_3.shape[1], x_arr_4.shape[1]])

            x_arr_1_exp = background * np.ones((new_shape_0, new_shape_1), dtype=np.int64)
            x_arr_1_exp[:x_arr_1.shape[0], :x_arr_1.shape[1]] = x_arr_1
            x_arr_2_exp = background * np.ones((new_shape_0, new_shape_1), dtype=np.int64)
            x_arr_2_exp[:x_arr_2.shape[0], :x_arr_2.shape[1]] = x_arr_2
            x_arr_3_exp = background * np.ones((new_shape_0, new_shape_1), dtype=np.int64)
            x_arr_3_exp[:x_arr_3.shape[0], :x_arr_3.shape[1]] = x_arr_3
            x_arr_4_exp = background * np.ones((new_shape_0, new_shape_1), dtype=np.int64)
            x_arr_4_exp[:x_arr_4.shape[0], :x_arr_4.shape[1]] = x_arr_4

            # break if gap
            if ((x_arr_1_exp != x_arr_2_exp) * (x_arr_1_exp != background) * (x_arr_2_exp != background)).sum():
                res_arr[i0, j0] = -1
                continue
            # break if gap
            if ((x_arr_1_exp != x_arr_3_exp) * (x_arr_1_exp != background) * (x_arr_3_exp != background)).sum():
                res_arr[i0, j0] = -1
                continue
            # break if gap
            if ((x_arr_1_exp != x_arr_4_exp) * (x_arr_1_exp != background) * (x_arr_4_exp != background)).sum():
                res_arr[i0, j0] = -1
                continue
            # break if gap
            if ((x_arr_2_exp != x_arr_3_exp) * (x_arr_2_exp != background) * (x_arr_3_exp != background)).sum():
                res_arr[i0, j0] = -1
                continue
            # break if gap
            if ((x_arr_2_exp != x_arr_4_exp) * (x_arr_2_exp != background) * (x_arr_4_exp != background)).sum():
                res_arr[i0, j0] = -1
                continue
            # break if gap
            if ((x_arr_3_exp != x_arr_4_exp) * (x_arr_3_exp != background) * (x_arr_4_exp != background)).sum():
                res_arr[i0, j0] = -1
                continue

            score_arr = (x_arr_1_exp != background).astype(np.int64) + (x_arr_2_exp != background).astype(np.int64) + \
                        (x_arr_3_exp != background).astype(np.int64) + (x_arr_4_exp != background).astype(np.int64)

            res_arr[i0, j0] = (score_arr * (score_arr - 1)).sum()
            # center should be same
            if 1 <= score_arr[0, 0] <= 2:
                # unless it is the center
                if i0 == j0 == x_arr.shape[0] // 2 - 1 and x_arr.shape[0] == x_arr.shape[1] and x_arr.shape[0] % 2 == 0:
                    pass
                else:
                    res_arr[i0, j0] = -1

    return res_arr


def fill_rot_symmetry_point(x_arr: np.array, background: np.int, i0: np.int, j0: np.int) -> np.array:

    y_arr = x_arr.copy()

    # center point
    for i in range(max(x_arr.shape) - 1):
        for j in range(max(x_arr.shape) - 1):
            if i0 - i >= 0 and j0 - j >= 0:
                v1 = x_arr[i0 - i, j0 - j]
            else:
                v1 = background
            if i0 - j >= 0 and j0 + i < x_arr.shape[1]:
                v2 = x_arr[i0 - j, j0 + i]
            else:
                v2 = background
            if i0 + i < x_arr.shape[0] and j0 + j < x_arr.shape[1]:
                v3 = x_arr[i0 + i, j0 + j]
            else:
                v3 = background
            if i0 + j < x_arr.shape[0] and j0 - i >= 0:
                v4 = x_arr[i0 + j, j0 - i]
            else:
                v4 = background

            # print(i, j, [v1, v2, v3, v4])
            vs_uni = np.unique(np.array([v1, v2, v3, v4]))
            assert vs_uni.shape[0] <= 2
            if vs_uni.shape[0] == 2:
                assert background in [v1, v2, v3, v4]
                new_c = [c for c in [v1, v2, v3, v4] if c != background][0]
                if i0 - i >= 0 and j0 - j >= 0:
                    y_arr[i0 - i, j0 - j] = new_c
                if i0 - j >= 0 and j0 + i < x_arr.shape[1]:
                    y_arr[i0 - j, j0 + i] = new_c
                if i0 + i < x_arr.shape[0] and j0 + j < x_arr.shape[1]:
                    y_arr[i0 + i, j0 + j] = new_c
                if i0 + j < x_arr.shape[0] and j0 - i >= 0:
                    y_arr[i0 + j, j0 - i] = new_c

    return y_arr


def fill_rot_symmetry_valley(x_arr: np.array, background: np.int, i0: np.int, j0: np.int) -> np.array:

    y_arr = x_arr.copy()

    # center point
    for i in range(max(x_arr.shape) - 1):
        for j in range(max(x_arr.shape) - 1):
            if i0 - i >= 0 and j0 - j >= 0:
                v1 = x_arr[i0 - i, j0 - j]
            else:
                v1 = background
            if i0 - j >= 0 and j0 + 1 + i < x_arr.shape[1]:
                v2 = x_arr[i0 - j, j0 + 1 + i]
            else:
                v2 = background
            if i0 + 1 + i < x_arr.shape[0] and j0 + 1 + j < x_arr.shape[1]:
                v3 = x_arr[i0 + 1 + i, j0 + 1 + j]
            else:
                v3 = background
            if i0 + 1 + j < x_arr.shape[0] and j0 - i >= 0:
                v4 = x_arr[i0 + 1 + j, j0 - i]
            else:
                v4 = background

            # print(i, j, [v1, v2, v3, v4])
            vs_uni = np.unique(np.array([v1, v2, v3, v4]))
            assert vs_uni.shape[0] <= 2
            if vs_uni.shape[0] == 2:
                assert background in [v1, v2, v3, v4]
                new_c = [c for c in [v1, v2, v3, v4] if c != background][0]
                if i0 - i >= 0 and j0 - j >= 0:
                    y_arr[i0 - i, j0 - j] = new_c
                if i0 - j >= 0 and j0 + 1 + i < x_arr.shape[1]:
                    y_arr[i0 - j, j0 + 1 + i] = new_c
                if i0 + 1 + i < x_arr.shape[0] and j0 + 1 + j < x_arr.shape[1]:
                    y_arr[i0 + 1 + i, j0 + 1 + j] = new_c
                if i0 + 1 + j < x_arr.shape[0] and j0 - i >= 0:
                    y_arr[i0 + 1 + j, j0 - i] = new_c

    return y_arr


class AutoFillRotSymmetry:

    def __init__(self):
        pass

    @classmethod
    def array(cls, x_arr: np.array, background: np.int, full: bool) -> np.array:
        res_arr_1 = is_rot_symmetry_point(x_arr, background)
        res_arr_2 = is_rot_symmetry_valley(x_arr, background)
        # print(res_arr_1, res_arr_2)
        assert res_arr_1.max() > 0 or res_arr_2.max() > 0

        if full:
            assert x_arr.shape[0] == x_arr.shape[1]
            if x_arr.shape[0] % 2 == 1:
                m = x_arr.shape[0] // 2
                assert res_arr_1[m, m] > 0
                return fill_rot_symmetry_point(x_arr, background, m, m)
            else:
                m = x_arr.shape[0] // 2 - 1
                assert res_arr_2[m, m] > 0
                return fill_rot_symmetry_valley(x_arr, background, m, m)

        if res_arr_1.max() >= res_arr_2.max():
            m = -1
            i0, j0 = -1, -1
            for i in range(res_arr_1.shape[0]):
                for j in range(res_arr_1.shape[1]):
                    if res_arr_1[i, j] > m:
                        m = res_arr_1[i, j]
                        i0, j0 = i, j
            return fill_rot_symmetry_point(x_arr, background, i0, j0)
        else:
            m = -1
            i0, j0 = -1, -1
            for i in range(res_arr_2.shape[0]):
                for j in range(res_arr_2.shape[1]):
                    if res_arr_2[i, j] > m:
                        m = res_arr_2[i, j]
                        i0, j0 = i, j
            return fill_rot_symmetry_valley(x_arr, background, i0, j0)

    @classmethod
    def case(cls, c: Case, full) -> Case:
        assert c.shape[0] > 2 and c.shape[1] > 2
        new_case = c.copy()
        if c.color_delete is None:
            new_values = cls.array(c.repr_values(), c.background_color, full)
        else:
            new_values = cls.array(c.repr_values(), c.color_delete, full)
        new_case.matter_list = [Matter(new_values, background_color=c.background_color, new=True)]
        return new_case

    @classmethod
    def problem(cls, p: Problem, full: bool = False) -> Problem:
        assert p.is_rot_symmetry
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, full) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, full) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    import time
    pp = Problem.load(19)
    pp.is_rot_symmetry = True
    t0 = time.time()
    qq = AutoFillRotSymmetry.problem(pp)
    print(time.time() - t0)
    print(qq)
    pp = Problem.load(26)
    pp.is_rot_symmetry = True
    t0 = time.time()
    qq = AutoFillRotSymmetry.problem(pp)
    print(time.time() - t0)
    print(qq)
    pp = Problem.load(360)
    pp.is_rot_symmetry = True
    t0 = time.time()
    qq = AutoFillRotSymmetry.problem(pp)
    print(time.time() - t0)
    print(qq)
    pp = Problem.load(107, "eval")
    print(pp)
    pp.is_rot_symmetry = True
    pp.color_delete = 6
    for cc in pp.train_x_list:
        cc.color_delete = 6
    for cc in pp.test_x_list:
        cc.color_delete = 6
    t0 = time.time()
    qq = AutoFillRotSymmetry.problem(pp)
    print(time.time() - t0)
    print(qq)
    pp = Problem.load(243, "eval")
    print(pp)
    pp.is_rot_symmetry = True
    t0 = time.time()
    qq = AutoFillRotSymmetry.problem(pp, True)
    print(time.time() - t0)
    print(qq)
