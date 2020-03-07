import os
import json
from src.data import Problem
from src.runner import Operator

train_names = list(sorted(os.listdir("../../input/training/")))


def read_problem(i):
    sample_data = json.load(open(f"../../input/training/{train_names[i]}", "r"))
    # print(sample_data)
    problem = Problem()
    problem.initialize(sample_data)
    return problem


def test_226():
    p = read_problem(226)
    print(p)
    q = Operator.run(p, "split_row_2")
    print(q)
    r = Operator.run(q, "bitwise_operators")
    print(r)
    s = Operator.run(r, "set_problem_color")
    print(s)


def test_0():
    p = read_problem(0)
    print(p)
    q = Operator.run(p, "fractal")
    print(q)


def test_13():
    p = read_problem(13)
    print(p)
    q = Operator.run(p, "split_color")
    print(q)
    r = Operator.run(q, "pick_min_color")
    print(r)
    s = Operator.run(r, "trim_background")
    print(s)


if __name__ == "__main__":
    p = read_problem(6)
    print(p)
    q = Operator.run(p, "auto_fill_row_col")
    print(q)
