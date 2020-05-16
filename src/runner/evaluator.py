import numpy as np
from src.data import Case, Problem


SHAPE_DIFF_FLAG = 10000
VAL_ILLEGAL = 100
VAL_DIFF = 1


def eval_distance(problem: Problem) -> np.int:
    res_base = 0
    res_fractal = 1
    case_x: Case
    case_y: Case

    # normal
    for case_x, case_y in zip(problem.train_x_list, problem.train_y_list):

        x_values = case_x.repr_values()
        y_values = case_y.repr_values()

        # normal reducer
        # shape
        if x_values.shape != y_values.shape:
            shape_0 = min(x_values.shape[0], y_values.shape[0])
            shape_1 = min(x_values.shape[1], y_values.shape[1])
            res_base += SHAPE_DIFF_FLAG * abs(
                x_values.shape[0] * x_values.shape[1] + y_values.shape[0] * y_values.shape[1] - 2 * shape_0 * shape_1
            )
        else:
            # values
            res_base += VAL_DIFF * (x_values != y_values).sum()
            res_base += VAL_ILLEGAL * (x_values < 0).sum()
            res_base += VAL_ILLEGAL * (x_values >= 10).sum()

    # fractal reducer
    for case_x, case_y in zip(problem.train_x_list, problem.train_y_list):

        r1, c1 = case_x.shape
        if case_x.shadow is None:
            r2, c2 = case_x.shape
        else:
            r2, c2 = case_x.shadow.shape

        if (r1 * r2, c1 * c2) == case_y.shape:
            x_values = case_x.repr_fractal_values()
            y_values = case_y.repr_values()

            # normal reducer
            # shape
            if x_values.shape != y_values.shape:
                shape_0 = min(x_values.shape[0], y_values.shape[0])
                shape_1 = min(x_values.shape[1], y_values.shape[1])
                res_fractal += SHAPE_DIFF_FLAG * abs(
                    x_values.shape[0] * x_values.shape[1] + y_values.shape[0] * y_values.shape[1] - 2 * shape_0 * shape_1
                )
            else:
                # values
                res_fractal += VAL_DIFF * (x_values != y_values).sum()
                res_fractal += VAL_ILLEGAL * (x_values < 0).sum()
                res_fractal += VAL_ILLEGAL * (x_values >= 10).sum()
        else:
            res_fractal += SHAPE_DIFF_FLAG * abs(
                r1 * r2 * c1 * c2 - y_values.shape[0] * y_values.shape[1]
            )

    res = min(res_base, res_fractal)
    return res
