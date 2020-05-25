from src.runner.runner import Runner


def test_124():
    p = Runner(124, verbose=True)
    p.run("change_background")
    # p.run("map_interior_exterior")
    # p.run("auto_paste_a")


# mesh
def test_607():
    p = Runner(207, "eval", verbose=True)
    p.run("mesh_split")
    p.run("collect_max")

    # print(p.problem_hand)


def test_58():
    p = Runner(58, verbose=True)
    p.run("mesh_split")
    p.run("n_cell")
    p.run("keep_max")
    p.run("max_color")
    p.run("paste_color_full")


def test_61():
    p = Runner(61, verbose=True)
    # symmetry


def test_64():
    p = Runner(64, verbose=True)


def test_85():
    p = Runner(85, verbose=True)


def test_134():
    p = Runner(134, verbose=True)
    p.run("divide")


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


def test_488():
    p = Runner(88, "eval", verbose=True)
    p.run("connect")
    p.run("count_hole")
    p.run("freq")
    p.run("sort_ascending")
    p.run("trim_background")


def test_551():
    p = Runner(151, "eval", verbose=True)
    # p.run("auto_fill_line_symmetry_full")
    # p.run("connect_row")


def test_555():
    p = Runner(155, "eval", verbose=True)
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


def test_652():
    p = Runner(252, "eval", verbose=True)
    p.run("color")
    p.run("auto_keep")
    p.run("align")


def test_654():
    p = Runner(254, "eval", verbose=True)
    p.run("connect")
    p.run("auto_keep")


def test_719():
    p = Runner(319, "eval", verbose=True)


def test_738():
    p = Runner(338, "eval", verbose=True)
    p.run("change_background")
    p.run("connect4")
    p.run("auto_paste_a")


def test_756():
    p = Runner(356, "eval", verbose=True)
    p.run("color")
    # p.run("rotations_each")


if __name__ == "__main__":
    test_124()
    test_607()
    test_58()
    test_61()
    test_134()
    test_140()
    test_261()
    test_488()
    test_551()
    test_652()
    test_654()
    test_738()
