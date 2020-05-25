from src.data import Problem
from src.operator.transformer.interior import Interior
from src.operator.transformer.fill_rectangle import FillRectangle
from src.operator.transformer.diff_color import DiffColor
from src.operator.transformer.align import Align
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
from src.operator.transformer.arithmetic.n_color import NColor
from src.operator.transformer.arithmetic.min_max import MinMax
from src.operator.transformer.arithmetic.mod_2 import Mod2
from src.operator.transformer.arithmetic.arg_sort import ArgSort
from src.operator.transformer.arithmetic.max_color import MaxColor
from src.operator.transformer.arithmetic.count_hole import CountHole
from src.operator.transformer.zoom import ZoomTransformer
from src.operator.transformer.rectangle_hole import RectangleHole
from src.operator.transformer.duplicate import DuplicateTransformer
from src.operator.transformer.shadow import Shadow
from src.operator.transformer.keep_mesh import KeepMesh
from src.operator.transformer.arithmetic.find_rectangle import RectangleFinder
from src.operator.transformer.arithmetic.find_symmetry import SymmetryFinder
from src.operator.transformer.reducer.drop_duplicates import DropDuplicates
from src.operator.transformer.arithmetic.sort import Sort
from src.operator.transformer.arithmetic.hash_count import HashFreq
from src.operator.transformer.arithmetic.frequency import Freq
from src.operator.transformer.keeper.keep_rectangle import RectangleKeeper
from src.operator.transformer.keeper.keep_max import MaxKeeper


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
        return AutoFillRotSymmetry.problem(p, False)
    elif command == "auto_fill_rot_full":
        return AutoFillRotSymmetry.problem(p, True)
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
    elif command == "n_cell_keep_none":
        return NCell.problem(p, True)
    elif command == "n_color":
        return NColor.problem(p)
    elif command == "max_color":
        return MaxColor.problem(p)
    elif command == "min_max":
        return MinMax.problem(p)
    elif command == "mod_2":
        return Mod2.problem(p)
    elif command == "count_hole":
        return CountHole.problem(p)
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
    elif command == "shadow_ones":
        return Shadow.problem(p, "ones")
    elif command == "shadow_problem_max":
        return Shadow.problem(p, "problem_max")
    elif command == "keep_mesh":
        return KeepMesh.problem(p)
    elif command == "find_rectangle":
        return RectangleFinder.problem(p)
    elif command == "find_symmetry":
        return SymmetryFinder.problem(p)
    elif command == "transform_zoom":
        return ZoomTransformer.problem(p)
    elif command == "transform_duplicate":
        return DuplicateTransformer.problem(p)
    elif command == "drop_duplicates":
        return DropDuplicates.problem(p)
    elif command == "sort_ascending":
        return Sort.problem(p, descending=False)
    elif command == "sort_descending":
        return Sort.problem(p, descending=True)
    elif command == "freq":
        return Freq.problem(p)
    elif command == "hash_freq":
        return HashFreq.problem(p)
    elif command == "rectangle_hole_simple":
        return RectangleHole.problem(p, hole_type="simple")
    elif command == "rectangle_hole_mesh":
        return RectangleHole.problem(p, hole_type="mesh")
    elif command == "rectangle_hole_mesh_x":
        return RectangleHole.problem(p, hole_type="mesh_x")
    elif command == "keep_rectangle":
        return RectangleKeeper.problem(p)
    elif command == "keep_max":
        return MaxKeeper.problem(p)
    elif command == "align":
        return Align.problem(p)
    else:
        raise NotImplementedError
