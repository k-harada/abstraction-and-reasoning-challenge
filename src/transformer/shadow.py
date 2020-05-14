import numpy as np
from src.data import Problem, Case, Matter


class Shadow:

    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case, shadow_type: str) -> Case:
        new_case: Case = c.copy()
        new_case.matter_list = c.matter_list[:]
        if shadow_type == "bool":
            new_case.shadow = (new_case.repr_values() != c.background_color).astype(np.bool)
        elif shadow_type == "same":
            new_case.shadow = new_case.repr_values().copy()
        elif shadow_type == "max":
            new_case.shadow = (new_case.repr_values() != new_case.max_color()).astype(np.bool)

        return new_case

    @classmethod
    def problem(cls, p: Problem, shadow_type: str) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, shadow_type) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, shadow_type) for c in p.test_x_list]
        return q