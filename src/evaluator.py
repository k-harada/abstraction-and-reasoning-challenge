N_DIFF = 100000
ROW_DIFF = 1000
CNT_DIFF = 10
VAL_DIFF = 1


def eval_distance(problem):

    res = 0

    for case in problem.train_case_list:

        if len(case.repr_x()) == 0:  # assume len(case.repr_y) == 1 now
            res += N_DIFF
        else:
            s = case.repr_x()[0]
            t = case.repr_y()[0]

            # ROWS
            res += abs(s.count("|") != t.count("|")) * ROW_DIFF

            # CNT
            res += abs(len(s) - len(t)) * ROW_DIFF

            # VALUE
            for i in range(min(len(s), len(t))):
                res += (s[i] != t[i])

    return res
