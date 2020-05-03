from src.data import Case, Matter


def paste_color(c: Case) -> Case:
    m: Matter
    new_case = c.copy()
    new_case.matter_list = [m.paste_color() for m in c.matter_list]
    return new_case
