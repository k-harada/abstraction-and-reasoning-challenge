import os
import json
import unittest
from src.data import Problem
from src.runner import Runner, static_solvers
from src.evaluator import eval_distance


train_file_list = list(sorted(os.listdir("../input/training/")))
eval_file_list = list(sorted(os.listdir("../input/evaluation/")))


def problem_load(i, file_list="train"):
    if file_list == "train":
        with open(f"../input/training/{train_file_list[i]}", "r") as f:
            sample_data = json.load(f)
            problem = Problem()
            problem.initialize(sample_data)
    else:
        with open(f"../input/evaluation/{eval_file_list[i]}", "r") as f:
            sample_data = json.load(f)
            problem = Problem()
            problem.initialize(sample_data)
    # static solvers
    for op in static_solvers:
        Runner.pre_solve(problem, op)
    return problem


class TestSolve(unittest.TestCase):

    def test_000(self):
        p = problem_load(0)
        p = Runner.run_transform(p, "fractal")
        self.assertEqual(eval_distance(p), 0)

    def test_001(self):
        p = problem_load(1)
        p = Runner.run_transform(p, "interior_dir4_zero")
        self.assertEqual(eval_distance(p), 0)

    def test_002(self):
        p = problem_load(2)
        p = Runner.run_solve(p, "extend_shape")
        p = Runner.run_transform(p, "auto_fill_row_col_periodicity")
        p = Runner.run_solve(p, "color_change")
        self.assertEqual(eval_distance(p), 0)

    def test_005(self):
        p = problem_load(5)
        p = Runner.run_map(p, "mesh_align")
        p = Runner.run_solve(p, "reduce_bitwise")
        p = Runner.run_solve(p, "color_change")
        self.assertEqual(eval_distance(p), 0)

    def test_006(self):
        p = problem_load(6)
        p = Runner.run_solve(p, "fill_pattern")
        self.assertEqual(eval_distance(p), 0)

    def test_008(self):
        p = problem_load(8)
        p = Runner.run_map(p, "mesh_2")
        p = Runner.run_transform(p, "connect_row_col")
        self.assertEqual(eval_distance(p), 0)

    def test_013(self):
        p = problem_load(13)
        p = Runner.run_map(p, "color")
        p = Runner.run_transform(p, "trim_background")
        self.assertEqual(eval_distance(p), 0)

    def test_014(self):
        p = problem_load(14)
        p = Runner.run_solve(p, "fit_replace_rule_33")
        self.assertEqual(eval_distance(p), 0)

    def test_015(self):
        p = problem_load(15)
        p = Runner.run_solve(p, "color_change")
        self.assertEqual(eval_distance(p), 0)

    def test_016(self):
        p = problem_load(16)
        p = Runner.run_transform(p, "auto_fill_row_col_periodicity")
        self.assertEqual(eval_distance(p), 0)

    def test_018(self):
        p = problem_load(18)
        p = Runner.run_solve(p, "duplicate")
        p = Runner.run_solve(p, "fit_replace_rule_33_all")
        self.assertEqual(eval_distance(p), 0)

    def test_019(self):
        p = problem_load(19)
        p = Runner.run_transform(p, "auto_fill_rot")
        self.assertEqual(eval_distance(p), 0)

    def test_020(self):
        p = problem_load(20)
        p = Runner.run_map(p, "mesh_split")
        p = Runner.run_transform(p, "collect_max")
        self.assertEqual(eval_distance(p), 0)

    def test_023(self):
        p = problem_load(23)
        p = Runner.run_map(p, "color")
        p = Runner.run_solve(p, "point_cross")
        p = Runner.run_solve(p, "color_pile")
        self.assertEqual(eval_distance(p), 0)

    def test_025(self):
        p = problem_load(25)
        p = Runner.run_map(p, "mesh_align")
        p = Runner.run_solve(p, "reduce_bitwise")
        p = Runner.run_solve(p, "color_change")
        self.assertEqual(eval_distance(p), 0)

    def test_026(self):
        p = problem_load(26)
        p = Runner.run_transform(p, "auto_fill_rot")
        p = Runner.run_transform(p, "diff_color")
        self.assertEqual(eval_distance(p), 0)

    def test_030(self):
        p = problem_load(30)
        p = Runner.run_transform(p, "trim_background")
        self.assertEqual(eval_distance(p), 0)

    def test_035(self):
        p = problem_load(35)
        p = Runner.run_map(p, "color")
        p = Runner.run_transform(p, "trim_background")
        self.assertEqual(eval_distance(p), 0)

    def test_044(self):
        p = problem_load(44)
        p = Runner.run_transform(p, "connect_row")
        self.assertEqual(eval_distance(p), 0)

    def test_049(self):
        p = problem_load(49)
        p = Runner.run_transform(p, "connect_row_col")
        p = Runner.run_transform(p, "diff_color")
        self.assertEqual(eval_distance(p), 0)

    def test_070(self):
        p = problem_load(70)
        p = Runner.run_transform(p, "auto_fill_line_symmetry_del")
        self.assertEqual(eval_distance(p), 0)

    def test_073(self):
        p = problem_load(73)
        p = Runner.run_transform(p, "auto_fill_line_symmetry_del")
        self.assertEqual(eval_distance(p), 0)

    def test_080(self):
        p = problem_load(80)
        p = Runner.run_map(p, "connect")
        p = Runner.run_transform(p, "fill_rectangle")
        self.assertEqual(eval_distance(p), 0)

    def test_091(self):
        p = problem_load(91)
        p = Runner.run_transform(p, "connect_row")
        p = Runner.run_transform(p, "connect_col")
        self.assertEqual(eval_distance(p), 0)

    def test_111(self):
        p = problem_load(111)
        p = Runner.run_transform(p, "auto_fill_line_symmetry_add")
        self.assertEqual(eval_distance(p), 0)

    def test_112(self):
        p = problem_load(112)
        p = Runner.run_transform(p, "auto_fill_line_symmetry_full")
        self.assertEqual(eval_distance(p), 0)

    def test_116(self):
        p = problem_load(116)
        p = Runner.run_transform(p, "auto_fill_line_symmetry_add")
        self.assertEqual(eval_distance(p), 0)

    def test_126(self):
        p = problem_load(126)
        p = Runner.run_solve(p, "fit_replace_rule_33")
        self.assertEqual(eval_distance(p), 0)

    def test_128(self):
        p = problem_load(128)
        p = Runner.run_transform(p, "max_color")
        p = Runner.run_transform(p, "paste_color_full")
        self.assertEqual(eval_distance(p), 0)

    def test_176(self):
        p = problem_load(176)
        p = Runner.run_transform(p, "trim_background")
        p = Runner.run_solve(p, "rotations")
        self.assertEqual(eval_distance(p), 0)

    def test_210(self):
        p = problem_load(210)
        p = Runner.run_map(p, "multiple_row_col")
        p = Runner.run_solve(p, "rotations")
        self.assertEqual(eval_distance(p), 0)

    def test_216(self):
        p = problem_load(216)
        p = Runner.run_transform(p, "trim_background")
        p = Runner.run_transform(p, "fractal")
        self.assertEqual(eval_distance(p), 0)

    def test_226(self):
        p = problem_load(226)
        p = Runner.run_map(p, "divide_row_col")
        p = Runner.run_solve(p, "reduce_bitwise")
        p = Runner.run_solve(p, "color_change")
        self.assertEqual(eval_distance(p), 0)

    def test_256(self):
        p = problem_load(256)
        p = Runner.run_map(p, "mesh_align")
        p = Runner.run_solve(p, "color_pile")
        self.assertEqual(eval_distance(p), 0)

    def test_266(self):
        p = problem_load(266)
        p = Runner.run_transform(p, "switch_color")
        p = Runner.run_transform(p, "keep_max_color")
        self.assertEqual(eval_distance(p), 0)

    def test_329(self):
        p = problem_load(329)
        p = Runner.run_map(p, "connect")
        p = Runner.run_transform(p, "paste_color")
        p = Runner.run_solve(p, "color_change")
        self.assertEqual(eval_distance(p), 0)


if __name__ == "__main__":
    unittest.main()
