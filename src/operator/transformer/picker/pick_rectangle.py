from src.data import Problem, Case, Matter


class RectanglePicker:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter) -> bool:
        if m.is_filled_rectangle() and min(m.shape[0], m.shape[1]) >= 3:
            return True
        else:
            return False

    @classmethod
    def case(cls, c: Case) -> Case:
        assert len(c.matter_list) > 1
        new_case: Case = c.copy()
        new_case.matter_list = [m for m in c.matter_list if cls.matter(m)]
        assert len(new_case.matter_list) > 0
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
