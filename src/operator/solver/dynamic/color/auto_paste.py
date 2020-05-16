from src.data import Problem
from src.operator.transformer.paste_color import PasteColor
from src.operator.solver.dynamic.color.color_change import color_change


class AutoPaste:

    def __init__(self):
        pass

    @classmethod
    def problem(cls, p: Problem, full: bool) -> Problem:
        q = PasteColor.problem(p, full)
        # print(q)
        return color_change(q)
