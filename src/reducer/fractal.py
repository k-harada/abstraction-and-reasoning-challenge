import numpy as np
import numba
from src.data import Problem, Case


@numba.jit('i8[:, :](i8[:, :], i8[:, :], i8, i8)', nopython=True)
def fractal_arr(m1_values, m2_values, background_case, background_m2):

    r1, c1 = m1_values.shape
    r2, c2 = m2_values.shape

    repr_values = np.ones((r1 * r2, c1 * c2), dtype=np.int64) * background_case

    if max(r1 * r2, c1 * c2) <= 30:
        for i in range(r2):
            for j in range(c2):
                if m2_values[i, j] != background_m2:
                    repr_values[(i * r1):((i + 1) * r1), (j * c1):((j + 1) * c1)] = m1_values

        return repr_values
    else:
        return np.zeros((30, 30), dtype=np.int64)


def fractal_case_repr(c: Case) -> np.array:
    m1 = c.matter_list[0]
    m2 = c.matter_list[1 % len(c.matter_list)]

    return fractal_arr(m1.values, m2.values, c.background_color, m2.background_color)
