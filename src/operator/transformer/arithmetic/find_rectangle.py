from src.data import Problem, Case, Matter


class RectangleFinder:

    def __init__(self):
        pass

    @classmethod
    def matter(cls, m: Matter) -> Matter:
        new_matter = m.deepcopy()
        if new_matter.is_filled_rectangle() and min(new_matter.shape[0], new_matter.shape[1]) >= 3:
            if new_matter.is_square():
                new_matter.a = 2
            else:
                new_matter.a = 1
        else:
            new_matter.a = 0
        return new_matter

    @classmethod
    def case(cls, c: Case) -> Case:
        assert len(c.matter_list) > 1
        new_case: Case = c.copy()
        new_case.matter_list = [cls.matter(m) for m in c.matter_list]
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
