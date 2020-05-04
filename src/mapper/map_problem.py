from src.data import Problem
from .identity.case import identity
from .split_color.case import split_color
from .split_connect.case import split_connect, split_connect_4
from .split_row_col.case import split_row_col
from .spread_duplicate.case import spread_row_col
from .split_mesh.case import mesh_2, mesh_align, mesh_split
from src.solver.common.shape import is_multiple, is_division
from .fractal.case import split_fractal


# initial map
def run_map(p: Problem, command: str) -> Problem:
    # set
    q: Problem
    q = p.copy()
    q.mapper = command
    # run
    if command == "identity":
        q.train_x_list = [identity(c) for c in p.train_x_list]
        q.test_x_list = [identity(c) for c in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    elif command == "color":
        q.train_x_list = [split_color(c) for c in p.train_x_list]
        q.test_x_list = [split_color(c) for c in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    elif command == "connect":
        q.train_x_list = [split_connect(c) for c in p.train_x_list]
        q.test_x_list = [split_connect(c) for c in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    elif command == "connect4":
        q.train_x_list = [split_connect_4(c) for c in p.train_x_list]
        q.test_x_list = [split_connect_4(c) for c in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    elif command == "divide_row_col":
        flag, d_row, d_col = is_division(p)
        assert flag
        q.train_x_list = [split_row_col(c, d_row, d_col) for c in p.train_x_list]
        q.test_x_list = [split_row_col(c, d_row, d_col) for c in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    elif command == "spread_row_col":
        flag, m_row, m_col = is_multiple(p)
        assert flag
        q.train_x_list = [spread_row_col(c, m_row, m_col) for c in p.train_x_list]
        q.test_x_list = [spread_row_col(c, m_row, m_col) for c in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    elif command == "mesh_2":
        q.train_x_list = [mesh_2(c) for c in p.train_x_list]
        q.test_x_list = [mesh_2(c) for c in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    elif command == "mesh_align":
        q.train_x_list = [mesh_align(c) for c in p.train_x_list]
        q.test_x_list = [mesh_align(c) for c in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    elif command == "mesh_split":
        q.train_x_list = [mesh_split(c) for c in p.train_x_list]
        q.test_x_list = [mesh_split(c) for c in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    elif command == "fractal":
        q.train_x_list = [split_fractal(c) for c in p.train_x_list]
        q.test_x_list = [split_fractal(c) for c in p.test_x_list]
        q.train_y_list = [x for x in p.train_y_list]
    else:
        raise NotImplementedError

    # set mapper for cases
    for case in q.train_x_list:
        case.mapper = command
    for case in q.test_x_list:
        case.mapper = command

    return q
