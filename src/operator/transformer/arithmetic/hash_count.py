import numpy as np
from src.data import Problem, Case, Matter


class HashFreq:
    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case) -> Case:
        m: Matter
        new_case = c.copy()
        counter = dict()
        for m in c.matter_list:
            k = str(m.values)
            if k not in counter.keys():
                counter[k] = 1
            else:
                counter[k] += 1
        new_case.matter_list = []
        for m in c.matter_list:
            new_m = m.deepcopy()
            new_m.a = counter[str(m.values)]
            new_case.matter_list.append(new_m)

        new_case.matter_list = list(sorted(new_case.matter_list, key=lambda x: -x.a))

        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q
