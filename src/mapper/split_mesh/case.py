from src.data import Case
import src.mapper.split_mesh.matter as matter_map


def mesh_split(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.mesh_split(c.matter_list[0])
    return new_case


def mesh_2(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.mesh_2(c.matter_list[0])
    return new_case


def mesh_align(c: Case) -> Case:
    assert len(c.matter_list) == 1
    new_case = c.copy()
    new_case.matter_list = matter_map.mesh_align(c.matter_list[0])
    new_case.shape = new_case.matter_list[0].shape
    return new_case
