from src.operator.matter.transform.trim_background import trim_background as tbm
from src.data import Case


def trim_background(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = [tbm(m) for m in c.matter_list]
    new_case.shape = max([m.shape[0] for m in new_case.matter_list]), max([m.shape[1] for m in new_case.matter_list])
    return new_case
