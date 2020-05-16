from src.data import Problem
from src.transformer.interior import Interior
from src.transformer.fill_rectangle import FillRectangle
from src.transformer.diff_color import DiffColor
from src.transformer.connect_line.row import ConnectRow
from src.transformer.connect_line.col import ConnectCol
from src.transformer.connect_line.row_col import ConnectRowCol
from src.transformer.connect_line.diagonal import ConnectDiagonal
from src.reducer.fill_pattern.periodicity_row_col import AutoFillRowColPeriodicity
from src.reducer.fill_pattern.symmetry_delete import AutoFillLineSymmetryDelete
from src.reducer.fill_pattern.symmetry_add import AutoFillLineSymmetryAdd
from src.reducer.fill_pattern.symmetry_full import AutoFillLineSymmetryFull
from src.reducer.fill_pattern.symmetry_rot import AutoFillRotSymmetry
from src.reducer.trim_background import TrimBackground
from src.reducer.collect_mesh import CollectMax
from src.reducer.fractal import Fractal
from src.transformer.paste_color import PasteColor
from src.transformer.switch_color import SwitchColor
from src.transformer.keep_max_color import KeepMaxColor
from src.transformer.change_background import ChangeBackground
from src.transformer.arithmetic.n_cell import NCell
from src.transformer.arithmetic.arg_sort import ArgSort
from src.transformer.arithmetic.max_color import MaxColor
from src.transformer.shadow import Shadow
from src.transformer.keep_mesh import KeepMesh


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
    elif command == "auto_fill_line_symmetry_del":
        return AutoFillLineSymmetryDelete.problem(p)
    elif command == "auto_fill_line_symmetry_add":
        return AutoFillLineSymmetryAdd.problem(p)
    elif command == "auto_fill_line_symmetry_full":
        return AutoFillLineSymmetryFull.problem(p)
    elif command == "auto_fill_rot":
        return AutoFillRotSymmetry.problem(p)
    elif command == "trim_background":
        return TrimBackground.problem(p)
    elif command == "collect_max":
        return CollectMax.problem(p)
    elif command == "fractal":
        return Fractal.problem(p)
    elif command == "paste_color":
        return PasteColor.problem(p, False)
    elif command == "paste_color_full":
        return PasteColor.problem(p, True)
    elif command == "switch_color":
        return SwitchColor.problem(p)
    elif command == "keep_max_color":
        return KeepMaxColor.problem(p)
    elif command == "change_background":
        return ChangeBackground.problem(p)
    elif command == "arg_sort":
        return ArgSort.problem(p)
    elif command == "n_cell":
        return NCell.problem(p)
    elif command == "max_color":
        return MaxColor.problem(p)
    elif command == "fill_rectangle":
        return FillRectangle.problem(p)
    elif command == "interior_dir4_zero":
        return Interior.problem(p)
    elif command == "shadow_bool":
        return Shadow.problem(p, "bool")
    elif command == "shadow_same":
        return Shadow.problem(p, "same")
    elif command == "shadow_max":
        return Shadow.problem(p, "max")
    elif command == "shadow_min":
        return Shadow.problem(p, "min")
    elif command == "shadow_mesh":
        return Shadow.problem(p, "mesh")
    elif command == "keep_mesh":
        return KeepMesh.problem(p)
    else:
        raise NotImplementedError
