import os
import json
import unittest
from src.data import Problem
from src.runner import Runner, static_solvers
from src.evaluator import eval_distance


train_file_list = list(sorted(os.listdir("../input/training/")))


def problem_load(i, file_list="train"):
    if file_list == "train":
        with open(f"../input/training/{train_file_list[i]}", "r") as f:
            sample_data = json.load(f)
            # print(sample_data)
            # print(file_list, i)
            problem = Problem()
            problem.initialize(sample_data)
        # static solvers
        for op in static_solvers:
            Runner.pre_solve(problem, op)
        # print("|" + "|".join(["".join(map(str, x)) for x in sample_data["test"][0]["output"]]) + "|")
        return problem


class TestSolve(unittest.TestCase):

    def test_000(self):
        p = problem_load(0)
        d = eval_distance(p)
        q = Runner.run_map(p, "fractal")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_001(self):
        p = problem_load(1)
        d = eval_distance(p)
        q = Runner.run_transform(p, "interior_dir4_zero")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_002(self):
        p = problem_load(2)
        d = eval_distance(p)
        q = Runner.run_solve(p, "extend_shape")
        d = eval_distance(q)
        r = Runner.run_transform(q, "auto_fill_row_col_periodicity")
        d = eval_distance(r)
        s = Runner.run_solve(r, "color_change")
        d = eval_distance(s)
        self.assertEqual(d, 0)

    def test_005(self):
        p = problem_load(5)
        d = eval_distance(p)
        q = Runner.run_map(p, "mesh_align")
        d = eval_distance(q)
        r = Runner.run_solve(q, "reduce_bitwise")
        d = eval_distance(r)
        s = Runner.run_solve(r, "color_change")
        d = eval_distance(s)
        self.assertEqual(d, 0)

    def test_006(self):
        p = problem_load(6)
        d = eval_distance(p)
        q = Runner.run_solve(p, "fill_pattern")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_008(self):
        p = problem_load(8)
        d = eval_distance(p)
        q = Runner.run_map(p, "mesh_2")
        d = eval_distance(q)
        r = Runner.run_transform(q, "connect_row_col")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_013(self):
        p = problem_load(13)
        d = eval_distance(p)
        q = Runner.run_map(p, "color")
        d = eval_distance(q)
        r = Runner.run_transform(q, "trim_background")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_014(self):
        p = problem_load(14)
        d = eval_distance(p)
        q = Runner.run_solve(p, "fit_replace_rule_33")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_015(self):
        p = problem_load(15)
        d = eval_distance(p)
        q = Runner.run_solve(p, "color_change")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_016(self):
        p = problem_load(16)
        d = eval_distance(p)
        q = Runner.run_transform(p, "auto_fill_row_col_periodicity")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_018(self):
        p = problem_load(18)
        d = eval_distance(p)
        q = Runner.run_solve(p, "duplicate")
        d = eval_distance(q)
        r = Runner.run_solve(q, "fit_replace_rule_33_all")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_020(self):
        p = problem_load(20)
        d = eval_distance(p)
        q = Runner.run_map(p, "mesh_split")
        d = eval_distance(q)
        r = Runner.run_transform(q, "collect_max")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_023(self):
        p = problem_load(23)
        d = eval_distance(p)
        q = Runner.run_map(p, "color")
        d = eval_distance(q)
        r = Runner.run_solve(q, "point_cross")
        d = eval_distance(r)
        s = Runner.run_solve(r, "color_pile")
        d = eval_distance(s)
        self.assertEqual(d, 0)

    def test_025(self):
        p = problem_load(25)
        d = eval_distance(p)
        q = Runner.run_map(p, "mesh_align")
        d = eval_distance(q)
        r = Runner.run_solve(q, "reduce_bitwise")
        d = eval_distance(r)
        s = Runner.run_solve(r, "color_change")
        d = eval_distance(s)
        self.assertEqual(d, 0)

    def test_030(self):
        p = problem_load(30)
        d = eval_distance(p)
        q = Runner.run_transform(p, "trim_background")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_035(self):
        p = problem_load(35)
        d = eval_distance(p)
        q = Runner.run_map(p, "color")
        d = eval_distance(q)
        r = Runner.run_transform(q, "trim_background")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_044(self):
        p = problem_load(44)
        d = eval_distance(p)
        q = Runner.run_transform(p, "connect_row")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_049(self):
        p = problem_load(49)
        d = eval_distance(p)
        q = Runner.run_transform(p, "connect_row_col")
        d = eval_distance(q)
        r = Runner.run_transform(q, "diff_color")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_070(self):
        p = problem_load(70)
        d = eval_distance(p)
        q = Runner.run_transform(p, "auto_fill_line_symmetry_del")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_073(self):
        p = problem_load(73)
        d = eval_distance(p)
        q = Runner.run_transform(p, "auto_fill_line_symmetry_del")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_080(self):
        p = problem_load(80)
        d = eval_distance(p)
        q = Runner.run_map(p, "connect")
        d = eval_distance(q)
        r = Runner.run_transform(q, "fill_rectangle")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_091(self):
        p = problem_load(91)
        d = eval_distance(p)
        q = Runner.run_transform(p, "connect_row")
        d = eval_distance(q)
        r = Runner.run_transform(q, "connect_col")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_111(self):
        p = problem_load(111)
        d = eval_distance(p)
        q = Runner.run_transform(p, "auto_fill_line_symmetry_add")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_112(self):
        p = problem_load(112)
        d = eval_distance(p)
        q = Runner.run_transform(p, "auto_fill_line_symmetry_full")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_116(self):
        p = problem_load(116)
        d = eval_distance(p)
        q = Runner.run_transform(p, "auto_fill_line_symmetry_add")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_126(self):
        p = problem_load(126)
        d = eval_distance(p)
        q = Runner.run_solve(p, "fit_replace_rule_33")
        d = eval_distance(q)
        self.assertEqual(d, 0)

    def test_128(self):
        p = problem_load(128)
        d = eval_distance(p)
        q = Runner.run_transform(p, "max_color")
        d = eval_distance(q)
        r = Runner.run_transform(q, "paste_color_full")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_176(self):
        p = problem_load(176)
        d = eval_distance(p)
        q = Runner.run_transform(p, "trim_background")
        d = eval_distance(q)
        r = Runner.run_solve(q, "rotations")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_210(self):
        p = problem_load(210)
        d = eval_distance(p)
        q = Runner.run_map(p, "multiple_row_col")
        d = eval_distance(q)
        r = Runner.run_solve(q, "rotations")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_216(self):
        p = problem_load(216)
        d = eval_distance(p)
        q = Runner.run_map(p, "fractal")
        d = eval_distance(q)
        r = Runner.run_transform(q, "trim_background")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_226(self):
        p = problem_load(226)
        d = eval_distance(p)
        q = Runner.run_map(p, "divide_row_col")
        d = eval_distance(q)
        r = Runner.run_solve(q, "reduce_bitwise")
        d = eval_distance(r)
        s = Runner.run_solve(r, "color_change")
        d = eval_distance(s)
        self.assertEqual(d, 0)

    def test_256(self):
        p = problem_load(256)
        d = eval_distance(p)
        q = Runner.run_map(p, "mesh_align")
        d = eval_distance(q)
        r = Runner.run_solve(q, "color_pile")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_266(self):
        p = problem_load(266)
        d = eval_distance(p)
        q = Runner.run_transform(p, "switch_color")
        d = eval_distance(q)
        r = Runner.run_transform(q, "keep_max_color")
        d = eval_distance(r)
        self.assertEqual(d, 0)

    def test_329(self):
        p = problem_load(329)
        d = eval_distance(p)
        q = Runner.run_map(p, "connect")
        d = eval_distance(q)
        r = Runner.run_transform(q, "paste_color")
        d = eval_distance(r)
        s = Runner.run_solve(r, "color_change")
        d = eval_distance(s)
        self.assertEqual(d, 0)


if __name__ == "__main__":
    unittest.main()
