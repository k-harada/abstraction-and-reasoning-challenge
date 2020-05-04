from src.data import Case, Matter


def diff_color(c: Case, compare_c: Case):

    assert c.color_add is not None

    new_values = c.repr_values()
    compare_values = compare_c.repr_values()

    assert new_values.shape == compare_values.shape
    new_values[new_values != compare_values] = c.color_add

    new_case: Case = c.copy()
    new_case.matter_list = [Matter(new_values, background_color=c.background_color)]

    return new_case
