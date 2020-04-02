import os
import json
from src.data import Problem
from src.operator.problem import run_map, run_reduce, run_transform
from src.solver.static.periodicity import is_periodic_row, is_periodic_col


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
    q = run_map(p, "split_row_2")
    print(q)
    r = run_reduce(q, "bitwise_and")
    print(r)
    # s = Operator.run(r, "set_problem_color")
    # print(s)
    # print(s.judge())


def test_0():
    p = read_problem(0)
    print(p)
    q = run_map(p, "fractal")
    print(q)
    print(q.judge())


def test_13():
    p = read_problem(13)
    print(p)
    q = run_map(p, "split_color")
    print(q)
    r = run_reduce(q, "pick_min_color")
    print(r)
    s = run_reduce(r, "trim_background")
    print(s)
    print(s.judge())


def test_6():
    p = read_problem(6)
    print(p)
    q = run_transform(p, "auto_fill_row_col")
    print(q)
    print(q.judge())


def test_109():
    p = read_problem(109)
    print(p)
    print(is_periodic_row(p))
    print(is_periodic_col(p))
    q = run_transform(p, "auto_fill_row_col")
    print(q)
    print(q.judge())


if __name__ == "__main__":
    test_109()
