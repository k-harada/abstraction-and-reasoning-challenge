from src.data import Problem
from src.transformer.interior import Interior
from src.transformer.fill_rectangle import FillRectangle
from src.transformer.diff_color import DiffColor
from src.transformer.connect_line.row import ConnectRow
from src.transformer.connect_line.col import ConnectCol
from src.transformer.connect_line.row_col import ConnectRowCol
from src.transformer.connect_line.diagonal import ConnectDiagonal
from src.reducer.fill_pattern.periodicity_row_col import AutoFillRowColPeriodicity
from src.reducer.fill_pattern.symmetry import AutoFillLineSymmetry
from src.reducer.trim_background import TrimBackground
from src.transformer.paste_color import PasteColor
from src.transformer.arithmetic.n_cell import NCell
from src.transformer.arithmetic.arg_sort import ArgSort


def run_transform(p: Problem, command: str) -> Problem:
    if command == "diff_color":
        return DiffColor.problem(p)
    elif command == "connect_row":
        return ConnectRow.problem(p)
    elif command == "connect_col":
        return ConnectCol.problem(p)
    elif command == "connect_row_col":
        return ConnectRowCol.problem(p)
    elif command == "connect_diagonal":
        return ConnectDiagonal.problem(p)
    elif command == "auto_fill_row_col_periodicity":
        return AutoFillRowColPeriodicity.problem(p)
    elif command == "auto_fill_line_symmetry":
        return AutoFillLineSymmetry.problem(p)
    elif command == "trim_background":
        return TrimBackground.problem(p)
    elif command == "paste_color":
        return PasteColor.problem(p)
    elif command == "arg_sort":
        return ArgSort.problem(p)
    elif command == "n_cell":
        return NCell.problem(p)
    elif command == "fill_rectangle":
        return FillRectangle.problem(p)
    elif command == "interior_dir4_zero":
        return Interior.problem(p)
    else:
        raise NotImplementedError
