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


def test_440():
    p = Runner(40, "eval", verbose=True)
    p.run("connect")


def test_507():
    p = Runner(107, "eval", verbose=True)
    p.run("auto_fill_line_symmetry_del")


def test_551():
    p = Runner(151, "eval", verbose=True)
    # p.run("auto_fill_line_symmetry_full")
    # p.run("connect_row")


def test_555():
    p = Runner(155, "eval", verbose=True)
    p.run("trim_background")


def test_558():
    p = Runner(158, "eval", verbose=True)
    p.run("trim_background")


def test_561():
    p = Runner(161, "eval", verbose=True)
    p.run("trim_background")


def test_576():
    p = Runner(176, "eval", verbose=True)
    p.run("trim_background")


def test_578():
    p = Runner(178, "eval", verbose=True)
    p.run("trim_background")


def test_586():
    p = Runner(186, "eval", verbose=True)
    p.run("trim_background")


def test_588():
    p = Runner(188, "eval", verbose=True)
    p.run("trim_background")


def test_598():
    p = Runner(198, "eval", verbose=True)


def test_599():
    p = Runner(199, "eval", verbose=True)


def test_652():
    p = Runner(252, "eval", verbose=True)


def test_719():
    p = Runner(319, "eval", verbose=True)


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
    test_507()
    test_551()
