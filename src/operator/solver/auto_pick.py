from typing import List
import numpy as np
from src.data import Problem, Case, Matter
from src.operator.mapper.map_connect import MapConnect


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


class AutoPick:

    def __init__(self):
        pass

    @classmethod
    def case_assert(cls, c_x: Case, c_y: Case):
        assert len(c_x.matter_list) > 1
        res_values = c_y.repr_values()
        for m in c_x.matter_list:
            if m.shape == res_values.shape:
                if (m.values == res_values).min():
                    return True
        return False

    @classmethod
    def case_create_flag(cls, c_x: Case, c_y: Case):
        res_list = []
        res_values = c_y.repr_values()
        for m in c_x.matter_list:
            if m.shape == res_values.shape:
                if (m.values == res_values).min():
                    res_list.append(True)
                else:
                    res_list.append(False)
            else:
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
    def eval_min(cls, train_list):
        for ca in train_list:
            min_a = min([ma.a for ma in ca.matter_list])
            if [min_a == ma.a for ma in ca.matter_list] == ca.y_list:
                pass
            else:
                return False
        return True

    @classmethod
    def eval_max(cls, train_list):
        for ca in train_list:
            max_a = max([ma.a for ma in ca.matter_list])
            if [max_a == ma.a for ma in ca.matter_list] == ca.y_list:
                pass
            else:
                return False
        return True

    @classmethod
    def fit_min(cls, test_list):
        for ca in test_list:
            min_a = min([ma.a for ma in ca.matter_list])
            ca.y_list = [min_a == ma.a for ma in ca.matter_list]
        return None

    @classmethod
    def fit_max(cls, test_list):
        for ca in test_list:
            max_a = max([ma.a for ma in ca.matter_list])
            ca.y_list = [max_a == ma.a for ma in ca.matter_list]
        return None

    @classmethod
    def auto_solve(cls, train_list, test_list):
        ca: AbstractCase
        ma: AbstractMatter

        # n_color
        cls.set_a(train_list, test_list, 'n_color')
        if cls.eval_min(train_list):
            return cls.fit_min(test_list)
        if cls.eval_max(train_list):
            return cls.fit_max(test_list)
        # n_cell
        cls.set_a(train_list, test_list, 'n_cell')
        if cls.eval_min(train_list):
            return cls.fit_min(test_list)
        if cls.eval_max(train_list):
            return cls.fit_max(test_list)
        # size
        cls.set_a(train_list, test_list, 'size')
        if cls.eval_min(train_list):
            return cls.fit_min(test_list)
        if cls.eval_max(train_list):
            return cls.fit_max(test_list)
        # is_filled_rectangle
        cls.set_a(train_list, test_list, 'is_filled_rectangle')
        if cls.eval_min(train_list):
            return cls.fit_min(test_list)
        if cls.eval_max(train_list):
            return cls.fit_max(test_list)
        # ind
        cls.set_a(train_list, test_list, 'ind')
        if cls.eval_min(train_list):
            return cls.fit_min(test_list)
        if cls.eval_max(train_list):
            return cls.fit_max(test_list)
        # hash
        cls.set_a(train_list, test_list, 'hash')
        if cls.eval_min(train_list):
            return cls.fit_min(test_list)
        if cls.eval_max(train_list):
            return cls.fit_max(test_list)
        # is_symmetry
        cls.set_a(train_list, test_list, 'is_symmetry')
        if cls.eval_min(train_list):
            return cls.fit_min(test_list)
        if cls.eval_max(train_list):
            return cls.fit_max(test_list)
        # is_symmetry
        cls.set_a(train_list, test_list, 'n_noise')
        if cls.eval_min(train_list):
            return cls.fit_min(test_list)
        if cls.eval_max(train_list):
            return cls.fit_max(test_list)
        raise ValueError

    @classmethod
    def case_fit(cls, c: Case, ca: AbstractCase):
        for m, y in zip(c.matter_list, ca.y_list):
            if y:
                new_case: Case = c.copy()
                new_matter: Matter = m.deepcopy()
                new_matter.x0 = 0
                new_matter.y0 = 0
                new_case.matter_list = [new_matter]
                new_case.shape = new_matter.shape
                return new_case
        raise AssertionError

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        # fast check
        for c_x, c_y in zip(p.train_x_list, p.train_y_list):
            assert cls.case_assert(c_x, c_y)
        # assign flag
        train_list = []
        test_list = []
        for c_x, c_y in zip(p.train_x_list, p.train_y_list):
            y_list = cls.case_create_flag(c_x, c_y)
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


def hand_pick_case(c: Case, ind: int) -> Case:
    new_case: Case = c.copy()
    new_matter: Matter = c.matter_list[ind % len(c.matter_list)].deepcopy()
    new_matter.x0 = 0
    new_matter.y0 = 0
    new_case.matter_list = [new_matter]
    new_case.shape = new_matter.shape
    return new_case


def hand_pick(p: Problem) -> List[Problem]:
    q0: Problem = p.copy()
    q0.train_x_list = [hand_pick_case(c, 0) for c in p.train_x_list]
    q0.test_x_list = [hand_pick_case(c, 0) for c in p.test_x_list]
    q1: Problem = p.copy()
    q1.train_x_list = [hand_pick_case(c, 1) for c in p.train_x_list]
    q1.test_x_list = [hand_pick_case(c, 1) for c in p.test_x_list]
    q2: Problem = p.copy()
    q2.train_x_list = [hand_pick_case(c, 2) for c in p.train_x_list]
    q2.test_x_list = [hand_pick_case(c, 2) for c in p.test_x_list]

    return [q0, q1, q2]


if __name__ == "__main__":
    pp = Problem.load(178, "eval")
    qq = MapConnect.problem(pp, allow_diagonal=True)
    rr = AutoPick.problem(qq)
    print(rr)
    pp = Problem.load(235, "eval")
    qq = MapConnect.problem(pp, allow_diagonal=True)
    rr = AutoPick.problem(qq)
    print(rr)
    pp = Problem.load(312, "eval")
    qq = MapConnect.problem(pp, allow_diagonal=True)
    rr = AutoPick.problem(qq)
    print(rr)
    pp = Problem.load(327, "eval")
    qq = MapConnect.problem(pp, allow_diagonal=True)
    rr = AutoPick.problem(qq)
    print(rr)
