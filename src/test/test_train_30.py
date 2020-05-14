import os
import json

from src.data import Problem
from src.runner import Runner, static_solvers
from src.runner.evaluator import eval_distance


train_file_list = list(sorted(os.listdir("../../input/training/")))


def problem_load(i, file_list="train"):
    if file_list == "train":
        sample_data = json.load(open(f"../../input/training/{train_file_list[i]}", "r"))
        # print(sample_data)
        print(file_list, i)
        problem = Problem()
        problem.initialize(sample_data)
        # static solvers
        for op in static_solvers:
            Runner.pre_solve(problem, op)
        # print("|" + "|".join(["".join(map(str, x)) for x in sample_data["test"][0]["output"]]) + "|")
        return problem


def test_0():
    p = problem_load(0)
    print(eval_distance(p))
    q = Runner.run_map(p, "fractal")
    print(eval_distance(q))


def test_1():
    p = problem_load(1)
    print(eval_distance(p))
    q = Runner.run_transform(p, "interior_dir4_zero")
    print(eval_distance(q))


def test_2():
    p = problem_load(2)
    print(eval_distance(p))
    q = Runner.run_solve(p, "extend_shape")
    print(eval_distance(q))
    r = Runner.run_transform(q, "auto_fill_row_col_periodicity")
    print(eval_distance(r))
    s = Runner.run_solve(r, "color_change")
    print(eval_distance(s))


def test_5():
    p = problem_load(5)
    print(eval_distance(p))
    q = Runner.run_map(p, "mesh_align")
    print(eval_distance(q))
    r = Runner.run_solve(q, "reduce_bitwise")
    print(eval_distance(r))


def test_6():
    p = problem_load(6)
    print(eval_distance(p))
    q = Runner.run_solve(p, "fill_pattern")
    print(eval_distance(q))


def test_8():
    p = problem_load(8)
    print(eval_distance(p))
    q = Runner.run_map(p, "mesh_2")
    print(eval_distance(q))
    r = Runner.run_transform(q, "connect_row_col")
    print(eval_distance(r))


def test_9():
    p = problem_load(9)
    print(eval_distance(p))
    q = Runner.run_map(p, "connect")
    print(eval_distance(q))
    r = Runner.run_transform(q, "arg_sort")
    print(eval_distance(r))
    s = Runner.run_transform(r, "paste_color")
    print(eval_distance(s))
    # t = Runner.run_solve(s, "color_change")
    # print(eval_distance(t))


def test_13():
    p = problem_load(13)
    print(eval_distance(p))
    q = Runner.run_map(p, "color")
    print(eval_distance(q))
    r = Runner.run_transform(q, "trim_background")
    print(eval_distance(r))


def test_14():
    p = problem_load(14)
    print(eval_distance(p))
    q = Runner.run_solve(p, "fit_replace_rule_33")
    print(eval_distance(q))


def test_15():
    p = problem_load(15)
    print(eval_distance(p))
    q = Runner.run_solve(p, "color_change")
    print(eval_distance(q))


def test_16():
    p = problem_load(16)
    print(eval_distance(p))
    q = Runner.run_transform(p, "auto_fill_row_col_periodicity")
    print(eval_distance(q))


def test_18():
    p = problem_load(18)
    print(eval_distance(p))
    q = Runner.run_solve(p, "duplicate")
    print(eval_distance(q))
    r = Runner.run_solve(q, "fit_replace_rule_33_all")
    print(eval_distance(r))


def test_23():
    p = problem_load(23)
    print(eval_distance(p))
    q = Runner.run_map(p, "color")
    print(eval_distance(q))
    r = Runner.run_solve(q, "point_cross")
    print(eval_distance(r))


def test_25():
    p = problem_load(25)
    print(eval_distance(p))
    q = Runner.run_map(p, "mesh_align")
    print(eval_distance(q))
    r = Runner.run_solve(q, "reduce_bitwise")
    print(eval_distance(r))


def test_30():
    p = problem_load(30)
    print(eval_distance(p))
    q = Runner.run_transform(p, "trim_background")
    print(eval_distance(q))


if __name__ == "__main__":
    test_0()
    test_1()
    test_2()
    test_5()
    test_6()
    test_8()
    test_9()
    test_13()
    test_14()
    test_15()
    test_16()
    test_18()
    test_23()
    test_25()
    test_30()