import numpy as np
from src.data import Problem, Case
from src.operator.transformer.keep_mesh import keep_mesh_array
from src.common.trivial_reducer import trivial_reducer


class Shadow:

    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case, shadow_type: str) -> Case:
        new_case: Case = c.copy()
        new_case.matter_list = c.matter_list[:]
        repr_values = trivial_reducer(c)
        if shadow_type == "bool":
            new_case.shadow = (repr_values != c.background_color).astype(np.bool)
        elif shadow_type == "same":
            new_case.shadow = repr_values.copy()
        elif shadow_type == "max":
            new_case.shadow = (repr_values == new_case.max_color()).astype(np.bool)
        elif shadow_type == "min":
            new_case.shadow = (repr_values == new_case.min_color()).astype(np.bool)
        elif shadow_type == "mesh":
            new_case.shadow = keep_mesh_array(repr_values)
        elif shadow_type == "ones":
            new_case.shadow = np.ones(repr_values.shape, dtype=np.bool)
        return new_case

    @classmethod
    def problem(cls, p: Problem, shadow_type: str) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c, shadow_type) for c in p.train_x_list]
        q.test_x_list = [cls.case(c, shadow_type) for c in p.test_x_list]
        return q
