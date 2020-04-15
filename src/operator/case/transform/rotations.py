from src.operator.matter.transform import rotations as rot_mat
from src.data import Case


def transpose(c: Case) -> Case:
    new_case = c.copy()
    new_case.shape = c.shape[1], c.shape[0]
    new_case.matter_list = [rot_mat.transpose(m) for m in c.matter_list]
    return new_case


def rev_row(c: Case) -> Case:
    new_case = c.copy()
    new_case.matter_list = [rot_mat.rev_row(m) for m in c.matter_list]
    return new_case


def rev_col(c: Case) -> Case:
    new_case = c.copy()
    new_case.matter_list = [rot_mat.rev_col(m) for m in c.matter_list]
    return new_case


def rot_180(c: Case) -> Case:
    new_case = c.copy()
    new_case.matter_list = [rot_mat.rot_180(m) for m in c.matter_list]
    return new_case


def rot_rev_180(c: Case) -> Case:
    new_case = c.copy()
    new_case.shape = c.shape[1], c.shape[0]
    new_case.matter_list = [rot_mat.rot_rev_180(m) for m in c.matter_list]
    return new_case


def rot_90(c: Case) -> Case:
    new_case = c.copy()
    new_case.shape = c.shape[1], c.shape[0]
    new_case.matter_list = [rot_mat.rot_90(m) for m in c.matter_list]
    return new_case


def rot_270(c: Case) -> Case:
    new_case = c.copy()
    new_case.shape = c.shape[1], c.shape[0]
    new_case.matter_list = [rot_mat.rot_270(m) for m in c.matter_list]
    return new_case
