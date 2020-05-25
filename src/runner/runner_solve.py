from src.data import Problem
from src.operator.solver.static.color import set_problem_color
from src.operator.solver.static.is_pattern import set_is_pattern
from src.operator.solver.static.is_periodic import set_is_periodic_row, set_is_periodic_col
from src.operator.solver.static.is_symmetry import set_is_line_symmetry_row, set_is_line_symmetry_col, set_is_rot_symmetry
from src.operator.solver.dynamic.pattern.fill_pattern import FillPattern
from src.operator.solver.dynamic.replace.point_around import fit_replace_rule_33
from src.operator.solver.dynamic.replace.point_around.fit_replace_rule_33_all import FitRuleOne33All
from src.operator.solver.dynamic.shape.duplicate import duplicate
from src.operator.solver.dynamic.shape.divide import divide
from src.operator.solver.dynamic.shape.extend_shape import extend_shape
from src.operator.solver.dynamic.shape.zoom import ZoomSolver
from src.operator.solver.dynamic.color.color_change import color_change
from src.operator.solver.dynamic.color.color_pile import color_pile
from src.operator.solver.dynamic.reduce.bitwise import reduce_bitwise
from src.operator.solver.dynamic.rotations.solve_rotations import solve_rotations as rotations
from src.operator.solver.dynamic.replace.point_cross.problem import point_cross
from src.operator.solver.dynamic.color.auto_paste import AutoPaste
from src.operator.solver.dynamic.color.auto_paste_a import AutoPasteA
from src.operator.solver.dynamic.color.auto_add_color import AutoAddColor
from src.operator.solver.auto_pick import AutoPick
from src.operator.solver.auto_keep import AutoKeep


# initial solver
def pre_solve(p: Problem, command: str) -> None:
    if command == "set_problem_color":
        set_problem_color(p)
    elif command == "set_is_pattern":
        set_is_pattern(p)
    elif command == "set_is_periodic_row":
        set_is_periodic_row(p)
    elif command == "set_is_periodic_col":
        set_is_periodic_col(p)
    elif command == "set_is_line_symmetry_row":
        set_is_line_symmetry_row(p)
    elif command == "set_is_line_symmetry_col":
        set_is_line_symmetry_col(p)
    elif command == "set_is_rot_symmetry":
        set_is_rot_symmetry(p)
    else:
        raise NotImplementedError

    return None


# normal and final solver
def run_solve(p: Problem, command: str) -> Problem:
    q: Problem
    if command == "fill_pattern":
        q = FillPattern.problem(p)
    elif command == "fit_replace_rule_33":
        q = fit_replace_rule_33(p)
    elif command == "fit_replace_rule_33_all":
        q = FitRuleOne33All.problem(p)
    elif command == "duplicate":
        q = duplicate(p)
    elif command == "divide":
        q = divide(p)
    elif command == "extend_shape":
        q = extend_shape(p)
    elif command == "color_change":
        q = color_change(p)
    elif command == "color_pile":
        q = color_pile(p)
    elif command == "reduce_bitwise":
        q = reduce_bitwise(p)
    elif command == "rotations":
        q = rotations(p)
    elif command == "point_cross":
        q = point_cross(p)
    elif command == "auto_paste":
        q = AutoPaste.problem(p, full=False)
    elif command == "auto_paste_full":
        q = AutoPaste.problem(p, full=True)
    elif command == "auto_paste_a":
        q = AutoPasteA.problem(p)
    elif command == "auto_add_color":
        q = AutoAddColor.problem(p)
    elif command == "solve_zoom":
        q = ZoomSolver.problem(p)
    elif command == "auto_pick":
        q = AutoPick.problem(p)
    elif command == "auto_keep":
        q = AutoKeep.problem(p)
    else:
        raise NotImplementedError

    return q
