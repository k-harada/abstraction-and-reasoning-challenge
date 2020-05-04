from src.data import Case


def identity(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = [c.matter_list[0]]
    return new_case
