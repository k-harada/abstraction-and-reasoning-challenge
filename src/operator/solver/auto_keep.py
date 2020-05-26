from typing import List
import numpy as np
from src.data import Problem, Case, Matter
from src.operator.mapper.map_connect import MapConnect
from src.operator.mapper.map_color import MapColor


class AbstractMatter:

    def __init__(self, m: Matter, ind: int, hash_count: int):
        self.a_init = m.a
        self.n_color = m.n_color()
        self.n_cell = m.n_cell()
        self.size = m.shape[0] * m.shape[1]
        self.is_filled_rectangle = m.is_filled_rectangle()
        if m.is_filled_rectangle():
            if m.is_square():
                self.is_rectangle = 2
            else:
                self.is_rectangle = 1
        else:
            if m.a is not None:
                self.is_rectangle = 0
            else:
                self.is_rectangle = None
        # assume trimmed
        x_arr = m.values
        # row
        res_row = 0
        for i in range(x_arr.shape[0] // 2):
            res_row += (x_arr[i, :] != x_arr[x_arr.shape[0] - 1 - i, :]).sum()
        # col
        res_col = 0
        for j in range(x_arr.shape[1] // 2):
            res_col += (x_arr[:, j] != x_arr[:, x_arr.shape[1] - 1 - j]).sum()
        res = 0
        if res_row == 0:
            res += 1
        if res_col == 0:
            res += 2
        self.is_symmetry = res
        self.ind = ind
        self.hash = hash_count
        self.n_noise = (m.values != m.max_color()).sum()
        self.a = None
        self.y = None


class AbstractCase:

    def __init__(self, c: Case):
        m: Matter
        counter = dict()
        for m in c.matter_list:
            k = str(m.values)
            if k not in counter.keys():
                counter[k] = 1
            else:
                counter[k] += 1
        hash_list = [counter[str(m.values)] for m in c.matter_list]
        self.matter_list = []
        for i in range(len(hash_list)):
            ma = AbstractMatter(c.matter_list[i], i, hash_list[i])
            self.matter_list.append(ma)
        self.y_list = None


class AutoKeep:

    def __init__(self):
        pass

    @classmethod
    def case_assert(cls, c_x: Case, c_y: Case, color=False):
        # color
        if color:
            color_x = c_x.color_count()
            color_y = c_y.color_count()
            flag_color = True
            for color_ in range(10):
                if color_ == c_x.background_color:
                    continue
                if color_x[color_] != color_y[color_] != 0:
                    flag_color = False
            if flag_color:
                return True, True
        # simply keep
        y_values = c_y.repr_values()
        if c_x.shape == c_y.shape:
            for m in c_x.matter_list:
                if (m.values == y_values[m.x0:m.x0 + m.shape[0], m.y0:m.y0 + m.shape[1]]).min():
                    pass
                elif (c_x.background_color == y_values[m.x0:m.x0 + m.shape[0], m.y0:m.y0 + m.shape[1]]).min():
                    pass
                else:
                    return False, False
            return True, False
        return False, False

    @classmethod
    def case_create_flag(cls, c_x: Case, c_y: Case, color=False):
        res_list = []
        # color
        if color:
            color_y = c_y.color_count()
            for m in c_x.matter_list:
                if color_y[m.max_color()] > 0:
                    res_list.append(True)
                else:
                    res_list.append(False)
            return res_list
        # normal
        else:
            y_values = c_y.repr_values()
            for m in c_x.matter_list:
                if (m.values == y_values[m.x0:m.x0 + m.shape[0], m.y0:m.y0 + m.shape[1]]).min():
                    res_list.append(True)
                elif (c_x.background_color == y_values[m.x0:m.x0 + m.shape[0], m.y0:m.y0 + m.shape[1]]).min():
                    res_list.append(False)
            return res_list

    @classmethod
    def set_a(cls, train_list, test_list, command):
        for ca in train_list:
            for ma in ca.matter_list:
                ma.a = eval('ma.' + command)
        for ca in test_list:
            for ma in ca.matter_list:
                ma.a = eval('ma.' + command)
        return None

    @classmethod
    def eval_eq_c(cls, train_list, c):
        for ca in train_list:
            if [ma.a == c for ma in ca.matter_list] == ca.y_list:
                pass
            else:
                return False
        return True

    @classmethod
    def eval_leq_c(cls, train_list, c):
        for ca in train_list:
            if [ma.a <= c for ma in ca.matter_list] == ca.y_list:
                pass
            else:
                return False
        return True

    @classmethod
    def eval_geq_c(cls, train_list, c):
        for ca in train_list:
            if [ma.a >= c for ma in ca.matter_list] == ca.y_list:
                pass
            else:
                return False
        return True

    @classmethod
    def fit_eq_c(cls, test_list, c):
        for ca in test_list:
            ca.y_list = [ma.a == c for ma in ca.matter_list]
        return None

    @classmethod
    def fit_leq_c(cls, test_list, c):
        for ca in test_list:
            ca.y_list = [ma.a <= c for ma in ca.matter_list]
        return None

    @classmethod
    def fit_geq_c(cls, test_list, c):
        for ca in test_list:
            ca.y_list = [ma.a >= c for ma in ca.matter_list]
        return None

    @classmethod
    def auto_solve(cls, train_list, test_list):
        ca: AbstractCase
        ma: AbstractMatter

        # n_color
        cls.set_a(train_list, test_list, 'n_color')
        for c_int in range(10):
            if cls.eval_leq_c(train_list, c_int):
                return cls.fit_leq_c(test_list, c_int)
            if cls.eval_geq_c(train_list, c_int):
                return cls.fit_geq_c(test_list, c_int)
            if cls.eval_eq_c(train_list, c_int):
                return cls.fit_eq_c(test_list, c_int)
        # n_cell
        cls.set_a(train_list, test_list, 'n_cell')
        for c_int in range(10):
            if cls.eval_leq_c(train_list, c_int):
                return cls.fit_leq_c(test_list, c_int)
            if cls.eval_geq_c(train_list, c_int):
                return cls.fit_geq_c(test_list, c_int)
            if cls.eval_eq_c(train_list, c_int):
                return cls.fit_eq_c(test_list, c_int)
        # size
        cls.set_a(train_list, test_list, 'size')
        for c_int in range(10):
            if cls.eval_leq_c(train_list, c_int):
                return cls.fit_leq_c(test_list, c_int)
            if cls.eval_geq_c(train_list, c_int):
                return cls.fit_geq_c(test_list, c_int)
            if cls.eval_eq_c(train_list, c_int):
                return cls.fit_eq_c(test_list, c_int)
        # is_filled_rectangle
        cls.set_a(train_list, test_list, 'is_filled_rectangle')
        for c_int in range(10):
            if cls.eval_leq_c(train_list, c_int):
                return cls.fit_leq_c(test_list, c_int)
            if cls.eval_geq_c(train_list, c_int):
                return cls.fit_geq_c(test_list, c_int)
            if cls.eval_eq_c(train_list, c_int):
                return cls.fit_eq_c(test_list, c_int)
        # ind
        cls.set_a(train_list, test_list, 'ind')
        for c_int in range(10):
            if cls.eval_leq_c(train_list, c_int):
                return cls.fit_leq_c(test_list, c_int)
            if cls.eval_geq_c(train_list, c_int):
                return cls.fit_geq_c(test_list, c_int)
            if cls.eval_eq_c(train_list, c_int):
                return cls.fit_eq_c(test_list, c_int)
        # hash
        cls.set_a(train_list, test_list, 'hash')
        for c_int in range(10):
            if cls.eval_leq_c(train_list, c_int):
                return cls.fit_leq_c(test_list, c_int)
            if cls.eval_geq_c(train_list, c_int):
                return cls.fit_geq_c(test_list, c_int)
            if cls.eval_eq_c(train_list, c_int):
                return cls.fit_eq_c(test_list, c_int)
        # is_symmetry
        cls.set_a(train_list, test_list, 'is_symmetry')
        for c_int in range(10):
            if cls.eval_leq_c(train_list, c_int):
                return cls.fit_leq_c(test_list, c_int)
            if cls.eval_geq_c(train_list, c_int):
                return cls.fit_geq_c(test_list, c_int)
            if cls.eval_eq_c(train_list, c_int):
                return cls.fit_eq_c(test_list, c_int)
        # n_noise
        cls.set_a(train_list, test_list, 'n_noise')
        for c_int in range(10):
            if cls.eval_leq_c(train_list, c_int):
                return cls.fit_leq_c(test_list, c_int)
            if cls.eval_geq_c(train_list, c_int):
                return cls.fit_geq_c(test_list, c_int)
            if cls.eval_eq_c(train_list, c_int):
                return cls.fit_eq_c(test_list, c_int)
        raise AssertionError

    @classmethod
    def case_fit(cls, c: Case, ca: AbstractCase):
        new_case: Case = c.copy()
        new_case.matter_list = []
        for m, y in zip(c.matter_list, ca.y_list):
            if y:
                new_case.matter_list.append(m.deepcopy())
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        # fast check
        if p.history == ["color"]:
            color = True
        else:
            color = False
        for c_x, c_y in zip(p.train_x_list, p.train_y_list):
            flag_keep, flag_color = cls.case_assert(c_x, c_y, color)
            assert flag_keep
        # assign flag
        train_list = []
        test_list = []
        for c_x, c_y in zip(p.train_x_list, p.train_y_list):
            y_list = cls.case_create_flag(c_x, c_y, flag_color)
            c_ax: AbstractCase = AbstractCase(c_x)
            c_ax.y_list = y_list
            train_list.append(c_ax)
        for c_x in p.test_x_list:
            c_ax: AbstractCase = AbstractCase(c_x)
            test_list.append(c_ax)

        cls.auto_solve(train_list, test_list)

        q: Problem = p.copy()
        q.train_x_list = [cls.case_fit(c, ca) for c, ca in zip(p.train_x_list, train_list)]
        q.test_x_list = [cls.case_fit(c, ca) for c, ca in zip(p.test_x_list, test_list)]
        return q


if __name__ == "__main__":
    pp = Problem.load(254, "eval")
    qq = MapConnect.problem(pp, allow_diagonal=True)
    rr = AutoKeep.problem(qq)
    print(rr.eval_distance())
    pp = Problem.load(252, "eval")
    qq = MapColor.problem(pp)
    qq.history.append("color")
    rr = AutoKeep.problem(qq)
    print(rr)
