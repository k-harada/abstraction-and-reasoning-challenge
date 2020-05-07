import numpy as np
import numba
from src.data import Problem, Case, Matter


def color_pile_arr(cnt_arr, y_values, background):

    fixed_values = np.ones(y_values.shape, dtype=np.int64)

    color_order = 10 * np.ones(10, dtype=np.int64)

    for order_cur in range(10):
        for color in range(10):
            if color == background:
                continue
            if color_order[color] < 9:
                continue
            if (y_values == color).sum() == 0:
                continue
            if ((y_values == color) * fixed_values == (cnt_arr[:, :, color] > 0) * fixed_values).min():
                color_order[color] = order_cur
        for color in range(10):
            if color_order[color] == order_cur:
                fixed_values *= 1 - (y_values == color)

    # background
    if ((y_values == background) == fixed_values).min():
        color_order[background] = 9

    return color_order


def reduce_rule(x_arr, y_arr):
    z_arr = 10 * np.ones(10, dtype=np.int)
    for color_order in range(10):
        compare_list = []
        for c in range(10):
            if (x_arr[c] != 10 or y_arr[c] != 10) and z_arr[c] == 10:
                compare_list.append(c)
        for c1 in compare_list:
            is_max = True
            for c2 in compare_list:
                if 10 > x_arr[c1] > x_arr[c2]:
                    is_max = False
                if 10 > y_arr[c1] > y_arr[c2]:
                    is_max = False
            if is_max:
                z_arr[c1] = color_order

    return z_arr


def color_pile(p: Problem) -> Problem:

    case_x: Case
    case_y: Case
    case_x_new: Case

    rule_all = 10 * np.ones(10, dtype=np.int64)

    for case_x, case_y in zip(p.train_x_list, p.train_y_list):

        # same shape
        assert case_x.shape == case_y.shape

        # reduce count
        cnt_arr = np.zeros((case_x.shape[0], case_x.shape[1], 10), dtype=np.int64)
        # collect values
        for m in case_x.matter_list:
            if not m.bool_show:
                continue
            for i in range(m.shape[0]):
                for j in range(m.shape[1]):
                    if m.values[i, j] != m.background_color:
                        assert 0 <= m.values[i, j] <= 9
                        cnt_arr[m.x0 + i, m.y0 + j, m.values[i, j]] += 1

        y_values = case_y.repr_values()

        # one rule
        res_arr = color_pile_arr(cnt_arr, y_values, case_x.background_color)
        for color in range(10):
            if (y_values == color).sum():
                assert res_arr[color] < 10

        # reduce rule
        rule_all = reduce_rule(res_arr, rule_all)

    q: Problem
    q = p.copy()
    q.train_x_list = []
    q.test_x_list = []

    # transform
    # test_x first so that find exception faster
    for case_x in p.test_x_list:
        new_values = case_x.background_color * np.ones(case_x.shape, dtype=np.int64)
        cnt_arr = np.zeros((case_x.shape[0], case_x.shape[1], 10), dtype=np.int64)
        # collect values
        for m in case_x.matter_list:
            if not m.bool_show:
                continue
            for i in range(m.shape[0]):
                for j in range(m.shape[1]):
                    if m.values[i, j] != m.background_color:
                        assert 0 <= m.values[i, j] <= 9
                        cnt_arr[m.x0 + i, m.y0 + j, m.values[i, j]] += 1
        # reduce
        for color_order in range(9, -1, -1):
            for color in range(10):
                if rule_all[color] == color_order:
                    new_values[cnt_arr[:, :, color] > 0] = color
        case_x_new = case_x.copy()
        case_x_new.matter_list = [Matter(new_values, background_color=case_x_new.background_color, new=True)]
        q.test_x_list.append(case_x_new)
    # train_x
    for case_x in p.train_x_list:
        new_values = case_x.background_color * np.ones(case_x.shape, dtype=np.int64)
        cnt_arr = np.zeros((case_x.shape[0], case_x.shape[1], 10), dtype=np.int64)
        # collect values
        for m in case_x.matter_list:
            if not m.bool_show:
                continue
            for i in range(m.shape[0]):
                for j in range(m.shape[1]):
                    if m.values[i, j] != m.background_color:
                        assert 0 <= m.values[i, j] <= 9
                        cnt_arr[m.x0 + i, m.y0 + j, m.values[i, j]] += 1
        # reduce
        for color_order in range(9, -1, -1):
            for color in range(10):
                if rule_all[color] == color_order:
                    new_values[cnt_arr[:, :, color] > 0] = color
        case_x_new = case_x.copy()
        case_x_new.matter_list = [Matter(new_values, background_color=case_x_new.background_color, new=True)]
        q.train_x_list.append(case_x_new)

    return q


if __name__ == "__main__":
    import time
    cnt_arr_ = np.zeros((3, 3, 10), dtype=np.int64)
    cnt_arr_[:, 1, 2] = 1
    cnt_arr_[1, :, 3] = 1
    y_values_ = np.array([[0, 2, 0], [3, 3, 3], [0, 2, 0]], dtype=np.int64)
    t0 = time.time()
    print(color_pile_arr(cnt_arr_, y_values_, 0))
    print(time.time() - t0)
    print(reduce_rule(np.array([0, 1, 1, 2, 10, 10, 10, 10, 10, 10]), np.array([0, 1, 2, 3, 4, 10, 10, 10, 10, 10])))
