import unittest
from src.runner.runner import Runner


class TestSolve(unittest.TestCase):

    def test_000(self):
        p = Runner(0)
        p.run("fractal")
        self.assertEqual(p.eval_distance(), 0)

    def test_001(self):
        p = Runner(1)
        p.run("interior_dir4_zero")
        self.assertEqual(p.eval_distance(), 0)

    def test_002(self):
        p = Runner(2)
        p.run("extend_shape")
        p.run("auto_fill_row_col_periodicity")
        p.run("color_change")
        self.assertEqual(p.eval_distance(), 0)

    def test_005(self):
        p = Runner(5)
        p.run("mesh_align")
        p.run("reduce_bitwise")
        p.run("color_change")
        self.assertEqual(p.eval_distance(), 0)

    def test_006(self):
        p = Runner(6)
        p.run("fill_pattern")
        self.assertEqual(p.eval_distance(), 0)

    def test_008(self):
        p = Runner(8)
        p.run("mesh_2")
        p.run("connect_row_col")
        self.assertEqual(p.eval_distance(), 0)

    def test_013(self):
        p = Runner(13)
        p.run("color")
        p.run("trim_background")
        self.assertEqual(p.eval_distance(), 0)

    def test_014(self):
        p = Runner(14)
        p.run("fit_replace_rule_33")
        self.assertEqual(p.eval_distance(), 0)

    def test_015(self):
        p = Runner(15)
        p.run("color_change")
        self.assertEqual(p.eval_distance(), 0)

    def test_016(self):
        p = Runner(16)
        p.run("auto_fill_row_col_periodicity")
        self.assertEqual(p.eval_distance(), 0)

    def test_018(self):
        p = Runner(18)
        p.run("duplicate")
        p.run("fit_replace_rule_33_all")
        self.assertEqual(p.eval_distance(), 0)

    def test_019(self):
        p = Runner(19)
        p.run("auto_fill_rot")
        self.assertEqual(p.eval_distance(), 0)

    def test_020(self):
        p = Runner(20)
        p.run("mesh_split")
        p.run("collect_max")
        self.assertEqual(p.eval_distance(), 0)

    def test_023(self):
        p = Runner(23)
        p.run("color")
        p.run("point_cross")
        p.run("color_pile")
        self.assertEqual(p.eval_distance(), 0)

    def test_025(self):
        p = Runner(25)
        p.run("mesh_align")
        p.run("reduce_bitwise")
        p.run("color_change")
        self.assertEqual(p.eval_distance(), 0)

    def test_030(self):
        p = Runner(30)
        p.run("trim_background")
        self.assertEqual(p.eval_distance(), 0)

    def test_035(self):
        p = Runner(35)
        p.run("color")
        p.run("trim_background")
        self.assertEqual(p.eval_distance(), 0)

    def test_044(self):
        p = Runner(44)
        p.run("connect_row")
        self.assertEqual(p.eval_distance(), 0)

    def test_049(self):
        p = Runner(49)
        p.run("connect_row_col")
        p.run("diff_color")
        self.assertEqual(p.eval_distance(), 0)

    def test_070(self):
        p = Runner(70)
        p.run("auto_fill_line_symmetry_del")
        self.assertEqual(p.eval_distance(), 0)

    def test_073(self):
        p = Runner(73)
        p.run("auto_fill_line_symmetry_del")
        self.assertEqual(p.eval_distance(), 0)

    def test_080(self):
        p = Runner(80)
        p.run("connect")
        p.run("fill_rectangle")
        self.assertEqual(p.eval_distance(), 0)

    def test_091(self):
        p = Runner(91)
        p.run("connect_row")
        p.run("connect_col")
        self.assertEqual(p.eval_distance(), 0)

    def test_111(self):
        p = Runner(111)
        p.run("auto_fill_line_symmetry_add")
        self.assertEqual(p.eval_distance(), 0)

    def test_112(self):
        p = Runner(112)
        p.run("auto_fill_line_symmetry_full")
        self.assertEqual(p.eval_distance(), 0)

    def test_116(self):
        p = Runner(116)
        p.run("auto_fill_line_symmetry_add")
        self.assertEqual(p.eval_distance(), 0)

    def test_126(self):
        p = Runner(126)
        p.run("fit_replace_rule_33")
        self.assertEqual(p.eval_distance(), 0)

    def test_128(self):
        p = Runner(128)
        p.run("max_color")
        p.run("paste_color_full")
        self.assertEqual(p.eval_distance(), 0)

    def test_176(self):
        p = Runner(176)
        p.run("trim_background")
        p.run("rotations")
        self.assertEqual(p.eval_distance(), 0)

    def test_210(self):
        p = Runner(210)
        p.run("multiple_row_col")
        p.run("rotations")
        self.assertEqual(p.eval_distance(), 0)

    def test_216(self):
        p = Runner(216)
        p.run("trim_background")
        p.run("fractal")
        self.assertEqual(p.eval_distance(), 0)

    def test_226(self):
        p = Runner(226)
        p.run("divide_row_col")
        p.run("reduce_bitwise")
        p.run("color_change")
        self.assertEqual(p.eval_distance(), 0)

    def test_256(self):
        p = Runner(256)
        p.run("mesh_align")
        p.run("color_pile")
        self.assertEqual(p.eval_distance(), 0)

    def test_266(self):
        p = Runner(266)
        p.run("switch_color")
        p.run("keep_max_color")
        self.assertEqual(p.eval_distance(), 0)

    def test_329(self):
        p = Runner(329)
        p.run("connect")
        p.run("paste_color")
        p.run("color_change")
        self.assertEqual(p.eval_distance(), 0)


if __name__ == "__main__":
    unittest.main()
