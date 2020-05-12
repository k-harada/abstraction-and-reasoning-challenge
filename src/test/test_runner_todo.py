from src.runner.runner import Runner


def test_5():
    p = Runner(5, verbose=True)
    print(p.problem_hand)
    for op in ['mesh_align', 'switch_color', 'fit_replace_rule_33']:
        p.run(op)
        print(p.problem_hand)


def test_9():
    p = Runner(9, verbose=True)
    p.run("connect")
    p.run("arg_sort")
    p.run("paste_color")
    p.run("color_change")


def test_26():
    p = Runner(26, verbose=True)
    p.run("auto_fill_rot")
    p.run("diff_color")


def test_46():
    p = Runner(46, verbose=True)
    p.run("color")
    p.run("point_cross")


def test_61():
    p = Runner(61, verbose=True)
    # p.run("auto_fill_line_symmetry")
    # p.run("color_change")


def test_64():
    p = Runner(64, verbose=True)


def test_134():
    p = Runner(134, verbose=True)


def test_140():
    p = Runner(140, verbose=True)


def test_221():
    p = Runner(221, verbose=True)


def test_243():
    p = Runner(243, verbose=True)


def test_258():
    p = Runner(258, verbose=True)
    p.run("change_background")
    p.run("trim_background")
    p.run("color_change")


def test_261():
    p = Runner(261, verbose=True)


def test_406():
    p = Runner(6, "eval", verbose=True)
    p.run("shadow_bool")
    p.run("switch_color")
    p.run("fractal")


if __name__ == "__main__":
    test_5()
    test_9()
    test_26()
    test_46()
    test_61()
    test_140()
    test_258()
    test_261()
    test_406()
