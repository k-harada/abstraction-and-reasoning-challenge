import os
import json

from src.data import Problem
from src.runner import Runner, static_solvers
from src.evaluator import eval_distance


train_file_list = list(sorted(os.listdir("../input/training/")))
eval_file_list = list(sorted(os.listdir("../input/evaluation/")))


def problem_load(i, file_list="train"):
    if file_list == "train":
        with open(f"../input/training/{train_file_list[i]}", "r") as f:
            sample_data = json.load(f)
            print("train", i)
            problem = Problem()
            problem.initialize(sample_data)
    else:
        with open(f"../input/evaluation/{eval_file_list[i]}", "r") as f:
            sample_data = json.load(f)
            print("eval", i)
            problem = Problem()
            problem.initialize(sample_data)
    # static solvers
    for op in static_solvers:
        Runner.pre_solve(problem, op)
    return problem


def test_9():
    p = problem_load(9)
    print(eval_distance(p))
    q = Runner.run_map(p, "connect")
    print(eval_distance(q))
    r = Runner.run_transform(q, "arg_sort")
    print(eval_distance(r))
    s = Runner.run_transform(r, "paste_color")
    print(eval_distance(s))
    t = Runner.run_solve(s, "color_change")
    print(eval_distance(t))


def test_46():
    p = problem_load(46)
    print(eval_distance(p))
    q = Runner.run_map(p, "color")
    print(eval_distance(q))
    r = Runner.run_solve(q, "point_cross")
    print(eval_distance(r))


def test_61():
    p = problem_load(61)
    print(eval_distance(p))
    # q = Runner.run_transform(p, "auto_fill_line_symmetry")
    # print(eval_distance(q))
    # r = Runner.run_solve(q, "color_change")
    # print(eval_distance(r))


def test_64():
    p = problem_load(64)
    print(eval_distance(p))


def test_134():
    p = problem_load(134)
    print(eval_distance(p))


def test_140():
    p = problem_load(140)
    print(eval_distance(p))


def test_221():
    p = problem_load(221)
    print(eval_distance(p))


def test_243():
    p = problem_load(243)
    print(eval_distance(p))


def test_258():
    p = problem_load(258)
    d = eval_distance(p)
    q = Runner.run_transform(p, "change_background")
    d = eval_distance(q)
    r = Runner.run_transform(q, "trim_background")
    d = eval_distance(r)
    s = Runner.run_solve(r, "color_change")
    d = eval_distance(s)
    print(d)


def test_261():
    p = problem_load(261)
    print(eval_distance(p))


def test_406():
    p = problem_load(6, "eval")
    p = Runner.run_transform(p, "shadow_bool")
    p = Runner.run_transform(p, "switch_color")
    p = Runner.run_transform(p, "fractal")
    print(eval_distance(p), 0)


if __name__ == "__main__":
    test_9()
    test_46()
    test_61()
    test_140()
    test_258()
    test_261()
    test_406()
