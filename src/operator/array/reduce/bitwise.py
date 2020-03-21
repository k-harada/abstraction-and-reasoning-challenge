def bitwise_or(a, b):
    """
    :param a: np.array(np.bool)
    :param b: np.array(np.bool)
    :return: np.array(np.bool), bitwise_or
    """
    return a | b


def bitwise_and(a, b):
    """
    :param a: np.array(np.bool)
    :param b: np.array(np.bool)
    :return: np.array(np.bool), bitwise_and
    """
    return a & b


def bitwise_xor(a, b):
    """
    :param a: np.array(np.bool)
    :param b: np.array(np.bool)
    :return: np.array(np.bool), bitwise_xor
    """
    return a ^ b


def bitwise_not_xor(a, b):
    """
    :param a: np.array(np.bool)
    :param b: np.array(np.bool)
    :return: np.array(np.bool), negation of bitwise_xor
    """
    return ~ bitwise_xor(a, b)


def bitwise_not_or(a, b):
    """
    :param a: np.array(np.bool)
    :param b: np.array(np.bool)
    :return: np.array(np.bool), negation of bitwise_or
    """
    return ~ bitwise_or(a, b)


def bitwise_not_and(a, b):
    """
    :param a: np.array(np.bool)
    :param b: np.array(np.bool)
    :return: np.array(np.bool), negation of bitwise_and
    """
    return ~ bitwise_and(a, b)
