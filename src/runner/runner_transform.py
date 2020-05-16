from src.data import Problem
from src.operator.transformer.interior import Interior
from src.operator.transformer.fill_rectangle import FillRectangle
from src.operator.transformer.diff_color import DiffColor
from src.operator.transformer.connect_line.row import ConnectRow
from src.operator.transformer.connect_line.col import ConnectCol
from src.operator.transformer.connect_line.row_col import ConnectRowCol
from src.operator.transformer.connect_line.diagonal import ConnectDiagonal
from src.operator.transformer.reducer.fill_pattern.periodicity_row_col import AutoFillRowColPeriodicity
from src.operator.transformer.reducer.fill_pattern.symmetry_delete import AutoFillLineSymmetryDelete
from src.operator.transformer.reducer.fill_pattern.symmetry_add import AutoFillLineSymmetryAdd
from src.operator.transformer.reducer.fill_pattern.symmetry_full import AutoFillLineSymmetryFull
from src.operator.transformer.reducer.fill_pattern.symmetry_rot import AutoFillRotSymmetry
from src.operator.transformer.reducer.trim_background import TrimBackground
from src.operator.transformer.reducer.collect_mesh import CollectMax
from src.operator.transformer.reducer.fractal import Fractal
from src.operator.transformer.paste_color import PasteColor
from src.operator.transformer.switch_color import SwitchColor
from src.operator.transformer.keep_max_color import KeepMaxColor
from src.operator.transformer.change_background import ChangeBackground
from src.operator.transformer.arithmetic.n_cell import NCell
from src.operator.transformer.arithmetic.arg_sort import ArgSort
from src.operator.transformer.arithmetic.max_color import MaxColor
from src.operator.transformer.shadow import Shadow
from src.operator.transformer.keep_mesh import KeepMesh
from src.operator.transformer.picker.pick_rectangle import RectanglePicker


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
    elif command == "pick_rectangle":
        return RectanglePicker.problem(p)
    else:
        raise NotImplementedError
