import numpy as np

from src.data import Case, Problem


SHAPE_DIFF_FLAG = 10000
VAL_ILLEGAL = 100
VAL_DIFF = 1


def case_repr_values(c: Case) -> np.array:

    try:
        if c.mapper == "fractal":

            m1 = c.matter_list[0]
            m2 = c.matter_list[1 % len(c.matter_list)]

            r1, c1 = m1.shape
            r2, c2 = m2.shape
            if max(r1 * r2, c1 * c2) <= 30:
                c.shape = (r1 * r2, c1 * c2)
                repr_values = np.ones(c.shape, dtype=np.int) * c.background_color
                for i in range(r2):
                    for j in range(c2):
                        if m2.values[i, j] != m2.background_color:
                            repr_values[(i * r1):((i + 1) * r1), (j * c1):((j + 1) * c1)] = m1.values
                return repr_values
            else:
                c.shape = (30, 30)
                return np.zeros((30, 30), dtype=np.int)
        else:
            # pile up from 0
            # paste background
            repr_values = np.ones(c.shape, dtype=np.int) * c.background_color
            # collect values
            for m in c.matter_list:
                if not m.bool_show:
                    continue
                for i in range(m.shape[0]):
                    for j in range(m.shape[1]):
                        if m.values[i, j] != m.background_color:
                            repr_values[m.x0 + i, m.y0 + j] = m.values[i, j]

            return repr_values
    except IndexError:
        print([(m.values, m.x0, m.y0, m.background_color) for m in c.matter_list])
        print(c.shape)
        raise


def eval_distance(problem: Problem) -> np.int:

    res = 0
    case_x: Case
    case_y: Case

    for case_x, case_y in zip(problem.train_x_list, problem.train_y_list):

        x_values = case_repr_values(case_x)
        y_values = case_repr_values(case_y)
        case_x.repr_values_eval = x_values
        case_y.repr_values_eval = y_values
        # print(x_values, y_values)

        # shape
        if x_values.shape != y_values.shape:
            res += SHAPE_DIFF_FLAG * abs(x_values.shape[0] * x_values.shape[1] - y_values.shape[0] * y_values.shape[1])

        # values
        for i in range(min(x_values.shape[0], y_values.shape[0])):
            for j in range(min(x_values.shape[1], y_values.shape[1])):
                if x_values[i, j] != y_values[i, j]:
                    res += VAL_DIFF
                if x_values[i, j] < 0 or x_values[i, j] >= 10:
                    res += VAL_ILLEGAL
                if y_values[i, j] < 0 or y_values[i, j] >= 10:
                    res += VAL_ILLEGAL

    # set
    for case_x in problem.test_x_list:
        case_x.repr_values_eval = case_repr_values(case_x)
    # print(res)
    return res
