from src.data import Problem
from .map_color import MapColor
from .map_connect import MapConnect
from .map_divide import Divide
from .map_multiple import Multiple
from .split_mesh_normal import SplitMesh
from .split_mesh_2 import SplitMeshTwo
from .split_mesh_align import SplitMeshAlign
from .map_fractal import MapFractal


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
        q = SplitMeshTwo.problem(p)
        q.mapper = command
    elif command == "mesh_align":
        q = SplitMeshAlign.problem(p)
        q.mapper = command
    elif command == "mesh_split":
        q = SplitMesh.problem(p)
        q.mapper = command
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
