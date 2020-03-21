from src.data import Case


def simple_reduce(c: Case) -> Case:
    assert len(c.matter_list) >= 2
    new_values = c.repr_values()
    new_case = Case()
    new_case.initialize(new_values, c.background_color)
    return new_case
