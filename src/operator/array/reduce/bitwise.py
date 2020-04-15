def bitwise_or(a, b):
    """
    :param a: np.array(np.bool)
    :param b: np.array(np.bool)
    :return: np.array(np.bool), bitwise_or
    """
    assert a.shape == b.shape
    return a | b


def bitwise_and(a, b):
    """
    :param a: np.array(np.bool)
    :param b: np.array(np.bool)
    :return: np.array(np.bool), bitwise_and
    """
    assert a.shape == b.shape
    return a & b


def bitwise_xor(a, b):
    """
    :param a: np.array(np.bool)
    :param b: np.array(np.bool)
    :return: np.array(np.bool), bitwise_xor
    """
    assert a.shape == b.shape
    return a ^ b


def bitwise_not_xor(a, b):
    """
    :param a: np.array(np.bool)
    :param b: np.array(np.bool)
    :return: np.array(np.bool), negation of bitwise_xor
    """
    assert a.shape == b.shape
    return ~ bitwise_xor(a, b)


def bitwise_not_or(a, b):
    """
    :param a: np.array(np.bool)
    :param b: np.array(np.bool)
    :return: np.array(np.bool), negation of bitwise_or
    """
    assert a.shape == b.shape
    return ~ bitwise_or(a, b)


def bitwise_not_and(a, b):
    """
    :param a: np.array(np.bool)
    :param b: np.array(np.bool)
    :return: np.array(np.bool), negation of bitwise_and
    """
    assert a.shape == b.shape
    return ~ bitwise_and(a, b)
