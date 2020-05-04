from src.data import Case, Matter


def split_fractal(c: Case) -> Case:

    new_case: Case = c.copy()
    m: Matter = c.matter_list[0]

    new_case.matter_list = [m.copy(), m.copy()]

    return new_case
