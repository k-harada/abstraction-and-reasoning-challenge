import numpy as np
from src.data import Problem, Case, Matter


def is_monotone(color_dict):
    a = -1000
    b = -1000
    v = -1000
    for k in sorted(color_dict.keys()):
        if color_dict[k] != v:
            v = color_dict[k]
            if a == -1000:
                a = k
            elif b == -1000:
                b = k
            else:
                return False, -1
    if b == -1000:
        return True, a
    else:
        return True, b


class AutoPasteA:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter, color_dict: dict) -> Matter:
        if m.a is not None:
            if m.a in color_dict.keys():
                new_matter = m.paste_color(color_dict[m.a])
            else:
                flag, bar = is_monotone(color_dict)
                if flag:
                    if m.a >= flag:
                        new_matter = m.paste_color(color_dict[max(color_dict.keys())])
                    else:
                        new_matter = m.paste_color(color_dict[min(color_dict.keys())])
                else:
                    raise AssertionError
            return new_matter
        else:
            return m

    @classmethod
    def matter_temp(cls, m: Matter) -> Matter:
        if m.a is not None:
            new_matter = m.paste_color(m.a + 10)
            return new_matter
        else:
            return m

    @classmethod
    def case(cls, c: Case, color_dict: dict) -> Case:
        new_case: Case = c.copy()
        new_case.matter_list = [cls.matter(m, color_dict) for m in c.matter_list]
        return new_case

    @classmethod
    def case_xy(cls, c_x: Case, c_y: Case) -> dict:
        temp_c_x = c_x.copy()
        temp_c_x.matter_list = [cls.matter_temp(m) for m in c_x.matter_list]
        x_repr = temp_c_x.repr_values()
        y_repr = c_y.repr_values()
        assert x_repr.shape == y_repr.shape
        res_dict = dict()
        for v in np.unique(x_repr):
            if v >= 10:
                new_w = np.unique(y_repr[x_repr == v])
                # print(x_repr, y_repr, new_w)
                assert new_w.shape[0] == 1
                res_dict[v - 10] = new_w[0]
        return res_dict

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        # color_dict
        color_dict = dict()
        for c_x, c_y in zip(p.train_x_list, p.train_y_list):
            new_dict = cls.case_xy(c_x, c_y)
            # print(new_dict)
            for k in new_dict.keys():
                if k in color_dict.keys():
                    assert color_dict[k] == new_dict[k]
                else:
                    color_dict[k] = new_dict[k]
        # fit
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, color_dict) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, color_dict) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    d = dict()
    d[0] = 1
    d[4] = 1
    d[10] = 1
    print(is_monotone(d))
    d = dict()
    d[0] = 1
    d[4] = 1
    d[10] = 5
    d[12] = 5
    print(is_monotone(d))
    d = dict()
    d[0] = 1
    d[4] = 5
    d[10] = 5
    d[12] = 1
    print(is_monotone(d))
    d[0] = 1
    d[4] = 5
    d[10] = 15
    d[12] = 21
    print(is_monotone(d))
