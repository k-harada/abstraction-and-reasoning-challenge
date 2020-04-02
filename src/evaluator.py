import numpy as np

from src.data import Case, Problem


N_DIFF = 100000
ROW_DIFF = 1000
CNT_DIFF = 10
VAL_DIFF = 1


def eval_distance(problem: Problem) -> np.int:

    res = 0
    case_x: Case
    case_y: Case

    for case_x, case_y in zip(problem.train_x_list, problem.train_y_list):

        if len(case_x.repr_values()) == 0:  # assume len(case.repr_y) == 1 now
            res += N_DIFF
        else:
            s = case_x.__repr__()
            t = case_y.__repr__()

            # ROWS
            res += abs(s.count("|") != t.count("|")) * ROW_DIFF

            # CNT
            res += abs(len(s) - len(t)) * CNT_DIFF

            # VALUE
            for i in range(min(len(s), len(t))):
                res += (s[i] != t[i]) * VAL_DIFF

    return res
