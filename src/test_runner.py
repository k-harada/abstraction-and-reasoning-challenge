import os
import json
from heapq import heappush, heappop

from src.data import Problem
from src.runner import Runner, mappers, transformers, reducers, all_operators, static_solvers
from src.evaluator import eval_distance


train_file_list = list(sorted(os.listdir("../input/training/")))


def problem_load(i, file_list="train"):
    if file_list == "train":
        sample_data = json.load(open(f"../input/training/{train_file_list[i]}", "r"))
        # print(sample_data)
        problem = Problem()
        problem.initialize(sample_data)
        return problem


def test_0():
    p = problem_load(0)
    print(eval_distance(p))
    q = Runner.run_map(p, "fractal")
    print(eval_distance(q))


def test_1():
    p = problem_load(1)
    print(eval_distance(p))
    q = Runner.run_solve(p, "set_problem_color")
    print(eval_distance(q))
    r = Runner.run_map(q, "interior_dir4_zero")
    print(eval_distance(r))


def test_5():
    p = problem_load(5)
    print(eval_distance(p))
    # static solvers
    for op in static_solvers:
        try:
            p = Runner.run_solve(p, op)
        except AssertionError:
            pass
    q = Runner.run_map(p, "mesh_align")
    print(eval_distance(q))
    s = Runner.run_reduce(q, "bitwise_and")
    print(eval_distance(s))
    # print(s)


def test_6():
    p = problem_load(6)
    print(eval_distance(p))
    q = Runner.run_solve(p, "set_is_pattern")
    print(eval_distance(q))
    r = Runner.run_solve(q, "fill_pattern")
    print(eval_distance(r))


def test_8():
    p = problem_load(8)
    print(eval_distance(p))
    q = Runner.run_map(p, "mesh_2")
    print(eval_distance(q))
    r = Runner.run_transform(q, "connect_row_col")
    print(eval_distance(r))


def test_16():
    p = problem_load(16)
    print(eval_distance(p))
    q = Runner.run_transform(p, "auto_fill_row_col")
    print(eval_distance(q))


def test_25():
    p = problem_load(25)
    print(eval_distance(p))
    q = Runner.run_map(p, "mesh_split")
    print(eval_distance(q))
    r = Runner.run_solve(q, "set_problem_color")
    print(eval_distance(r))
    s = Runner.run_reduce(r, "bitwise_not_or")
    print(eval_distance(s))


def test_30():
    p = problem_load(30)
    print(eval_distance(p))
    q = Runner.run_transform(p, "trim_background")
    print(eval_distance(q))


if __name__ == "__main__":
    test_0()
    test_1()
    test_5()
    test_6()
    test_8()
    test_16()
    test_25()
    test_30()
