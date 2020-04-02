import os
import json

import numpy as np

from src.data import Case
from src.operator.case.map import fractal, color, interior_dir4_zero, mesh
from src.operator.case.reduce import bitwise_or
from src.operator.case.transform import connect_row, connect_col, auto_fill_row_col, trim_background


train_names = list(sorted(os.listdir("../../input/training/")))


def read_problem_and_case_train_0(i):
    sample_data = json.load(open(f"../../input/training/{train_names[i]}", "r"))
    c = Case()
    c.initialize(np.array(sample_data["train"][0]["input"]))
    return c


if __name__ == "__main__":
    c0 = read_problem_and_case_train_0(0)
    print(c0)
    c1 = fractal(c0)
    print(c1)
    c2 = read_problem_and_case_train_0(16)
    print(c2)
    c3 = color(c2)
    print(c3)
    c4 = read_problem_and_case_train_0(1)
    print(c4)
    c5 = interior_dir4_zero(c4)
    print(c5)
    c6 = read_problem_and_case_train_0(5)
    print(c6)
    c7 = bitwise_or(mesh(c6))
    print(c7)
    c8 = read_problem_and_case_train_0(40)
    print(c8)
    c9 = connect_row(c8)
    print(c9)
    c10 = read_problem_and_case_train_0(16)
    print(c10)
    c11 = auto_fill_row_col(c10)
    print(c11)
    c12 = read_problem_and_case_train_0(30)
    print(c12)
    c13 = trim_background(c12)
    print(c13)

