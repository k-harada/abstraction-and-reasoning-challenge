import numpy as np
from src.data import Problem, Case, Matter


class AutoPasteA:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter, color_dict: dict) -> Matter:
        if m.a is not None:
            assert m.a in color_dict.keys()
            new_matter = m.paste_color(color_dict[m.a])
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
