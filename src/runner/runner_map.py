from src.data import Problem
from src.operator.mapper.map_color import MapColor
from src.operator.mapper.map_connect import MapConnect
from src.operator.mapper.map_color_connect import MapColorConnect
from src.operator.mapper.map_divide import Divide
from src.operator.mapper.map_multiple import Multiple
from src.operator.mapper.split_mesh_normal import SplitMesh
from src.operator.mapper.split_mesh_2 import SplitMeshTwo
from src.operator.mapper.split_mesh_align import SplitMeshAlign
from src.operator.mapper.fusion import Fusion
from src.operator.mapper.map_interior import MapInterior
from src.operator.mapper.map_interior_pierce import MapInteriorPierce


# initial map
def run_map(p: Problem, command: str) -> Problem:
    q: Problem
    # run
    if command == "identity":
        q = p.copy()
        raise DeprecationWarning
    elif command == "color":
        q = MapColor.problem(p)
    elif command == "connect":
        q = MapConnect.problem(p, True)
    elif command == "connect4":
        q = MapConnect.problem(p, False)
    elif command == "color_connect":
        q = MapColorConnect.problem(p, True)
    elif command == "color_connect4":
        q = MapColorConnect.problem(p, False)
    elif command == "divide_row_col":
        q = Divide.problem(p)
    elif command == "multiple_row_col":
        q = Multiple.problem(p)
    elif command == "mesh_2":
        q = SplitMeshTwo.problem(p)
    elif command == "mesh_align":
        q = SplitMeshAlign.problem(p)
    elif command == "mesh_split":
        q = SplitMesh.problem(p)
    elif command == "fusion":
        q = Fusion.problem(p)
    elif command == "map_interior":
        q = MapInterior.problem(p, boundary_none=False)
    elif command == "map_interior_in":
        q = MapInterior.problem(p, boundary_none=True)
    elif command == "map_interior_pierce":
        q = MapInteriorPierce.problem(p, allow_diagonal=False, boundary_none=True)
    else:
        raise NotImplementedError

    return q
