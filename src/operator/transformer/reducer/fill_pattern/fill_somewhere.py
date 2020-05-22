import numpy as np
from src.data import Problem, Case, Matter


def fill_somewhere(x_arr: np.array, del_color: int) -> np.array:

    assert min(x_arr.shape) >= 15
    assert x_arr.min() >= 0

    if (x_arr == del_color).sum() == 0:
        return x_arr

    x_arr_copy = x_arr.copy()
    x_arr_copy[x_arr == del_color] = -1

    x_sum = (x_arr == del_color).sum(axis=1)
    y_sum = (x_arr == del_color).sum(axis=0)

    x0 = min([i for i in range(x_arr.shape[0]) if x_sum[i]])
    x1 = max([i for i in range(x_arr.shape[0]) if x_sum[i]]) + 1
    y0 = min([i for i in range(x_arr.shape[1]) if y_sum[i]])
    y1 = max([i for i in range(x_arr.shape[1]) if y_sum[i]]) + 1

    x0_ = max(x0 - 1, 0)
    x1_ = min(x1 + 1, x_arr.shape[0])
    y0_ = max(y0 - 1, 0)
    y1_ = min(y1 + 1, x_arr.shape[1])

    search_arr = x_arr_copy[x0_:x1_, y0_:y1_].copy()

    for t in range(4):
        for i in range(x_arr_copy.shape[0] - search_arr.shape[0] + 1):
            for j in range(x_arr_copy.shape[1] - search_arr.shape[1] + 1):
                # perfect on >= 0
                match_arr = (x_arr_copy[i:i+search_arr.shape[0], j:j+search_arr.shape[1]] == search_arr).astype(int)
                match_arr[x_arr_copy[i:i+search_arr.shape[0], j:j+search_arr.shape[1]] < 0] = 1
                match_arr[search_arr < 0] = 1
                if match_arr.min() == 0:
                    continue
                # no match on negative
                if x_arr_copy[i:i+search_arr.shape[0], j:j+search_arr.shape[1]].min() < 0:
                    continue

                new_v = x_arr_copy[i:i+search_arr.shape[0], j:j+search_arr.shape[1]].copy()
                if t % 2 == 0:
                    new_v = new_v.reshape((x1_ - x0_, y1_ - y0_))
                else:
                    new_v = new_v.reshape((y1_ - y0_, x1_ - x0_))
                x_arr_copy[x0_:x1_, y0_:y1_] = np.rot90(new_v, 4 - t)
                return x_arr_copy

        search_arr = np.rot90(search_arr)

    raise AssertionError


class FillSomewhere:

    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case) -> Case:
        if c.color_delete is not None:
            new_case = c.copy()
            new_values = fill_somewhere(c.repr_values(), c.color_delete)
            new_case.matter_list = [Matter(new_values, background_color=c.background_color, new=True)]
            return new_case
        else:
            return c

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    xx_arr = np.array([[9, 9, 3, 1, 2], [9, 9, 3, 1, 2], [3, 3, 3, 3, 3]])
    xxx_arr = np.zeros((15, 15), dtype=int)
    xxx_arr[:3, :5] = xx_arr
    yyy_arr = fill_somewhere(xxx_arr, 9)
    print(xxx_arr)
    print(yyy_arr)
