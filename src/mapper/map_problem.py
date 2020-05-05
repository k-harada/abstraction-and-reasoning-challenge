from src.data import Problem
from .color import MapColor
from .connect import MapConnect
from .divide import Divide
from .multiple import Multiple
from .split_mesh.case import mesh_2, mesh_align, mesh_split
from src.solver.common.shape import is_division
from .fractal import MapFractal


# initial map
def run_map(p: Problem, command: str) -> Problem:
    # set
    q: Problem
    q = p.copy()
    q.mapper = command
    # run
    if command == "identity":
        q = p.copy()
        q.mapper = command
        raise DeprecationWarning
    elif command == "color":
        q = MapColor.problem(p)
        q.mapper = command
    elif command == "connect":
        q = MapConnect.problem(p, True)
        q.mapper = command
    elif command == "connect4":
        q = MapConnect.problem(p, False)
        q.mapper = command
    elif command == "divide_row_col":
        q = Divide.problem(p)
        q.mapper = command
    elif command == "multiple_row_col":
        q = Multiple.problem(p)
        q.mapper = command
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
        q = MapFractal.problem(p)
        q.mapper = command
    else:
        raise NotImplementedError

    # set mapper for cases
    for case in q.train_x_list:
        case.mapper = command
    for case in q.test_x_list:
        case.mapper = command

    return q
