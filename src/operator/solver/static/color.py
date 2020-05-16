from src.data import Problem, Case, Matter
from src.operator.solver.common.color import monotone_color, new_color, deleted_color


def define_color(p: Problem) -> int:
    # only one color
    color_add = monotone_color(p)
    if color_add != -1:
        return color_add
    color_add_list = new_color(p)
    if len(color_add_list) == 1:
        return color_add_list[0]
    else:
        return -1


def set_problem_color(p: Problem) -> None:

    color_add = define_color(p)
    # print(color_add)

    if color_add != -1:
        p.color_add = color_add
        c: Case
        m: Matter
        for c in p.train_x_list:
            c.color_add = color_add
        for c in p.train_y_list:
            c.color_add = color_add
        for c in p.test_x_list:
            c.color_add = color_add

    deleted_colors = deleted_color(p)

    if len(deleted_colors) == 1:
        color_delete = deleted_colors[0]
    elif len(deleted_colors) == 2 and p.background_color in deleted_colors:
        if deleted_colors[0] == p.background_color:
            color_delete = deleted_colors[1]
        else:
            color_delete = deleted_colors[0]
    else:
        color_delete = None

    if color_delete is not None:
        p.color_delete = color_delete
        c: Case
        m: Matter
        for c in p.train_x_list:
            c.color_delete = color_delete
        for c in p.train_y_list:
            c.color_delete = color_delete
        for c in p.test_x_list:
            c.color_delete = color_delete

    return None
