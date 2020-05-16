from src.data import Problem, Case, Matter
from src.operator.solver.common.color import only_color


class AutoAddColor:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter, op: str, const: int, color_add: int) -> Matter:
        assert m.a is not None
        if op == "<=":
            if m.a <= const:
                return m.paste_color(color_add)
            else:
                return m
        elif op == "==":
            if m.a == const:
                return m.paste_color(color_add)
            else:
                return m
        elif op == ">=":
            if m.a >= const:
                return m.paste_color(color_add)
            else:
                return m
        else:
            raise NotImplementedError

    @classmethod
    def case(cls, c: Case, op: str, const: int) -> Case:
        assert c.color_add is not None
        new_case: Case = c.copy()
        m: Matter
        new_case.matter_list = [cls.matter(m, op, const, c.color_add) for m in c.matter_list]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        assert only_color(p)
        # assert non_background coincide
        q: Problem = p.copy()
        for op in ["<=", "==", ">="]:
            for const in range(1, 10):
                q.train_x_list = [cls.case(c, op, const) for c in p.train_x_list]
                q.test_x_list = [cls.case(c, op, const) for c in p.test_x_list]
                ac, n_train = q.judge()
                if ac == n_train:
                    return q

        raise AssertionError
