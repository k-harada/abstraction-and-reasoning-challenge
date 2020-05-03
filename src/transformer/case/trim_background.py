from src.transformer.matter.trim_background import trim_background as tbm
from src.data import Case


def trim_background(c: Case) -> Case:
    new_case = c.copy()
    new_case.matter_list = [tbm(c.matter_list[0])]
    new_case.shape = new_case.matter_list[0].shape
    return new_case
