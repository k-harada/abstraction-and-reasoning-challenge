import numpy as np
import numba
from src.data import Problem, Case, Matter


@numba.jit('i8[:, :](i8[:, :], i8)', nopython=True)
def is_rot_symmetry_point(x_arr: np.array, background: np.int) -> np.array:

    res_arr = np.zeros(x_arr.shape, dtype=np.int64)

    # center point
    for i0 in range(x_arr.shape[0]):
        for j0 in range(x_arr.shape[1]):

            # pre-find
            fail = False
            for i in range(1, min(i0, x_arr.shape[0] - i0)):
                if background != x_arr[i0 - i, j0] != x_arr[i0 + i, j0] != background:
                    fail = True
                    break
            if fail:
                continue

            for i in range(max(x_arr.shape)):
                for j in range(max(x_arr.shape)):
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
                    # print(i0, j0, [v1, v2, v3, v4])
                    # score
                    vs_uni = np.unique(np.array([v1, v2, v3, v4]))
                    if vs_uni.shape[0] >= 3:
                        res_arr[i0, j0] = -2
                    elif vs_uni.shape[0] == 2 and background not in [v1, v2, v3, v4]:
                        res_arr[i0, j0] = -2
                    else:
                        c = [v1, v2, v3, v4].count(background)
                        # print(i0, j0, c, [v1, v2, v3, v4])
                        res_arr[i0, j0] += (4 - c) * (3 - c)

                    # break if -1
                    if res_arr[i0, j0] == -2:
                        break
                # break if -1
                if res_arr[i0, j0] == -2:
                    break

    return res_arr // 2


@numba.jit('i8[:, :](i8[:, :], i8)', nopython=True)
def is_rot_symmetry_valley(x_arr: np.array, background: np.int) -> np.array:

    res_arr = np.zeros(x_arr.shape, dtype=np.int64)
    res_arr[-1, :] = -1
    res_arr[:, -1] = -1

    # center point
    for i0 in range(x_arr.shape[0] - 1):
        for j0 in range(x_arr.shape[1] - 1):
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
                    # print(i0, j0, [v1, v2, v3, v4])
                    # score
                    vs_uni = np.unique(np.array([v1, v2, v3, v4]))
                    if vs_uni.shape[0] >= 3:
                        res_arr[i0, j0] = -1
                    elif vs_uni.shape[0] == 2 and background not in [v1, v2, v3, v4]:
                        res_arr[i0, j0] = -1
                    else:
                        c = [v1, v2, v3, v4].count(background)
                        res_arr[i0, j0] += (4 - c) * (3 - c)

                    # break if -1
                    if res_arr[i0, j0] == -1:
                        break
                # break if -1
                if res_arr[i0, j0] == -1:
                    break

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
    def array(cls, x_arr: np.array, background: np.int) -> np.array:
        res_arr_1 = is_rot_symmetry_point(x_arr, background)
        res_arr_2 = is_rot_symmetry_valley(x_arr, background)
        # print(res_arr_1, res_arr_2)
        assert res_arr_1.max() > 0 or res_arr_2.max() > 0

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
    def case(cls, c: Case) -> Case:
        assert c.shape[0] > 2 and c.shape[1] > 2
        new_case = c.copy()
        new_values = cls.array(c.repr_values(), c.background_color)
        new_case.matter_list = [Matter(new_values, background_color=c.background_color, new=True)]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        assert p.is_rot_symmetry
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    import time
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    t0 = time.time()
    print(is_rot_symmetry_point(x, 0))
    print(time.time() - t0)
    x = np.array([[3, 2, 3], [0, 6, 0], [3, 0, 3]])
    t0 = time.time()
    print(is_rot_symmetry_point(x, 0))
    print(time.time() - t0)
    x = np.array([[1, 2, 1], [2, 5, 2], [1, 2, 1]])
    t0 = time.time()
    print(is_rot_symmetry_point(x, 0))
    print(time.time() - t0)
    x = np.array([[1, 2, 1], [2, 5, 2], [1, 2, 1]])
    t0 = time.time()
    print(is_rot_symmetry_valley(x, 0))
    print(time.time() - t0)
    x = np.array([[1, 2, 3], [3, 4, 4], [2, 4, 4]])
    t0 = time.time()
    print(is_rot_symmetry_valley(x, 0))
    print(time.time() - t0)

    x = np.array([[3, 2, 3], [0, 6, 0], [3, 0, 3]])
    t0 = time.time()
    print(fill_rot_symmetry_point(x, 0, 1, 1))
    print(time.time() - t0)
    x = np.array([[1, 2, 0], [3, 4, 0], [0, 0, 0]])
    t0 = time.time()
    print(fill_rot_symmetry_valley(x, 0, 1, 1))
    print(time.time() - t0)

    x = np.array([[3, 2, 3], [0, 6, 0], [3, 0, 3]])
    t0 = time.time()
    print(AutoFillRotSymmetry.array(x, 0))
    print(time.time() - t0)
    x = np.array([
        [0, 0, 0, 2, 2, 0, 0, 0], [0, 0, 0, 2, 2, 0, 0, 0], [0, 0, 0, 2, 2, 0, 0, 0], [2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    ])
    t0 = time.time()
    print(AutoFillRotSymmetry.array(x, 0))
    print(time.time() - t0)

