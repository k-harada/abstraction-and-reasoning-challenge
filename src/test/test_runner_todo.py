from src.runner.runner import Runner


def test_019():
    p = Runner(19)
    # p.run("auto_fill_rot")
    # self.assertEqual(p.eval_distance(), 0)


def test_20():
    p = Runner(20, verbose=True)
    p.run("mesh_split")
    p.run("collect_max")


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


def test_222():
    p = Runner(222, verbose=True)
    p.run("solve_zoom")


def test_261():
    p = Runner(261, verbose=True)


def test_409():
    p = Runner(9, "eval", verbose=True)
    p.run("fusion")
    p.run("auto_fill_line_symmetry_del")


def test_507():
    p = Runner(107, "eval", verbose=True)
    p.run("auto_fill_line_symmetry_del")


def test_551():
    p = Runner(151, "eval", verbose=True)
    # p.run("auto_fill_line_symmetry_full")
    # p.run("connect_row")


def test_558():
    p = Runner(158, "eval", verbose=True)
    p.run("trim_background")


def test_576():
    p = Runner(176, "eval", verbose=True)
    p.run("trim_background")


def test_588():
    p = Runner(188, "eval", verbose=True)
    p.run("trim_background")


def test_598():
    p = Runner(198, "eval", verbose=True)


def test_599():
    p = Runner(199, "eval", verbose=True)


def test_711():
    p = Runner(311, "eval", verbose=True)
    p.run("shadow_ones")
    p.run("fractal")


def test_714():
    p = Runner(314, "eval", verbose=True)
    p.run("drop_duplicates")


def test_719():
    p = Runner(319, "eval", verbose=True)


def test_725():
    p = Runner(325, "eval", verbose=True)
    p.run("n_color")
    p.run("transform_zoom")


def test_727():
    p = Runner(327, "eval", verbose=True)
    p.run("connect")
    p.run("find_symmetry")
    p.run("trim_background")


def test_756():
    p = Runner(356, "eval", verbose=True)
    p.run("color")
    # p.run("rotations_each")


if __name__ == "__main__":
    test_019()
    test_20()
    test_26()
    test_61()
    test_140()
    test_222()
    test_261()
    test_409()
    test_507()
    test_551()
    test_711()
    test_714()
    test_725()
    test_727()
