from src.runner.runner import Runner


def test_019():
    p = Runner(19)
    # p.run("auto_fill_rot")
    # self.assertEqual(p.eval_distance(), 0)


def test_26():
    p = Runner(26, verbose=True)
    # p.run("auto_fill_rot")
    # p.run("diff_color")


def test_61():
    p = Runner(61, verbose=True)


def test_64():
    p = Runner(64, verbose=True)


def test_134():
    p = Runner(134, verbose=True)


def test_140():
    p = Runner(140, verbose=True)


def test_217():
    p = Runner(217, verbose=True)


def test_221():
    p = Runner(221, verbose=True)


def test_261():
    p = Runner(261, verbose=True)


def test_336():
    p = Runner(336, verbose=True)
    p.run("color_change")


def test_406():
    p = Runner(6, "eval", verbose=True)
    p.run("shadow_bool")
    p.run("switch_color")
    p.run("fractal")


def test_411():
    p = Runner(11, "eval", verbose=True)
    p.run("color_connect4")
    p.run("pick_rectangle")
    p.run("collect_max")


def test_412():
    p = Runner(12, "eval", verbose=True)
    p.run("connect")
    p.run("count_hole")
    p.run("auto_paste")


def test_446():
    p = Runner(46, "eval", verbose=True)
    p.run("mesh_split")
    p.run("switch_color")
    p.run("color_change")


def test_458():
    p = Runner(58, "eval", verbose=True)
    p.run("point_cross")
    p.run("interior_dir4_zero")


def test_507():
    p = Runner(107, "eval", verbose=True)
    p.run("auto_fill_line_symmetry_del")


def test_508():
    p = Runner(108, "eval", verbose=True)
    p.run("duplicate")
    p.run("switch_color")


if __name__ == "__main__":
    test_019()
    test_26()
    test_61()
    test_140()
    test_261()
    test_336()
    test_406()
    test_411()
    test_412()
    test_446()
    test_458()
    test_507()
    test_508()
