from heapq import heappop, heappush
import numpy as np
from src.data import Problem, Case, Matter


def align_xy(x0_arr: np.array, y0_arr: np.array, x1_arr: np.array, y1_arr: np.array, c_arr: np.array) -> np.array:

    n = x0_arr.shape[0]

    # x
    heap_x = []
    for i in range(n):
        heappush(heap_x, (x0_arr[i], x1_arr[i], i))

    x1_temp = 0
    x_list_all = []
    x_list_now = []
    while len(heap_x):
        x0, x1, i = heappop(heap_x)
        if x0 >= x1_temp:
            # new group
            x1_temp = x1
            if len(x_list_now) > 0:
                x_list_all.append(x_list_now)
            x_list_now = [i]
        else:
            x1_temp = max(x1_temp, x1)
            x_list_now.append(i)
    x_list_all.append(x_list_now)

    # y
    heap_y = []
    for i in range(n):
        heappush(heap_y, (y0_arr[i], y1_arr[i], i))

    y1_temp = 0
    y_list_all = []
    y_list_now = []
    while len(heap_y):
        y0, y1, i = heappop(heap_y)
        if y0 >= y1_temp:
            # new group
            y1_temp = y1
            if len(y_list_now) > 0:
                y_list_all.append(y_list_now)
            y_list_now = [i]
        else:
            y1_temp = max(y1_temp, y1)
            y_list_now.append(i)
    y_list_all.append(y_list_now)

    # find size
    len_x_max = max([len(x) for x in x_list_all])
    len_y_max = max([len(y) for y in y_list_all])

    assert 0 < len_x_max * len_y_max <= n
    # eval 158 is a good example
    # try
    xl, yl = 0, 0
    for xl in range(len_x_max, n + 1):
        if n % xl != 0:
            continue
        yl = n // xl
        assert yl >= len_y_max  # you must break before yl < len_y_max
        # bind until xl
        xl_temp = 0
        for x in x_list_all:
            xl_temp += len(x)
            if xl_temp == xl:
                xl_temp = 0
            elif xl_temp > xl:
                break
        if xl_temp > 0:
            continue
        # success for x, bind until yl
        yl_temp = 0
        for y in y_list_all:
            yl_temp += len(y)
            if yl_temp == yl:
                yl_temp = 0
            elif yl_temp > yl:
                break
        if yl_temp > 0:
            continue
        # success for y
        break

    assert xl * yl > 0
    # assign i, j
    # bind until xl
    i_arr = np.zeros(n, dtype=np.int)
    row_id = 0
    xl_temp = 0
    for x_list in x_list_all:
        xl_temp += len(x_list)
        for i in x_list:
            i_arr[i] = row_id
        if xl_temp == xl:
            xl_temp = 0
            row_id += 1

    # bind until yl
    j_arr = np.zeros(n, dtype=np.int)
    col_id = 0
    yl_temp = 0
    for y_list in y_list_all:
        yl_temp += len(y_list)
        for i in y_list:
            j_arr[i] = col_id
        if yl_temp == yl:
            yl_temp = 0
            col_id += 1

    res_arr = -1 * np.ones((yl, xl), dtype=np.int)
    for i in range(n):
        assert res_arr[i_arr[i], j_arr[i]] == -1
        res_arr[i_arr[i], j_arr[i]] = c_arr[i]

    return res_arr


class CollectMax:

    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case) -> Case:
        m: Matter
        x0_arr = np.array([m.x0 for m in c.matter_list if not m.is_mesh])
        y0_arr = np.array([m.y0 for m in c.matter_list if not m.is_mesh])
        x1_arr = np.array([m.x0 + m.shape[0] for m in c.matter_list if not m.is_mesh])
        y1_arr = np.array([m.y0 + m.shape[1] for m in c.matter_list if not m.is_mesh])
        c_arr = np.array([m.max_color() for m in c.matter_list if not m.is_mesh])

        res_arr = align_xy(x0_arr, y0_arr, x1_arr, y1_arr, c_arr)

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
    x0_ = np.array([0, 0])
    x1_ = np.array([1, 1])
    y0_ = np.array([0, 2])
    y1_ = np.array([1, 3])
    c_ = np.array([4, 5])
    res_arr_ = align_xy(x0_, y0_, x1_, y1_, c_)
    print(res_arr_)
