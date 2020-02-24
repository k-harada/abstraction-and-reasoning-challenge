import numpy as np
from src.data import Matter

# List[matter] -> matter


def bitwise_or(m_list):

    assert len(set([m.shape[0] for m in m_list])) == 1
    assert len(set([m.shape[1] for m in m_list])) == 1

    new_m_value = np.array([(m.values != m.background_color).astype(np.int) for m in m_list]).sum(axis=0)
    new_m_value = (new_m_value > 0).astype(np.int)
    return Matter(new_m_value)


def bitwise_and(m_list):

    assert len(set([m.shape[0] for m in m_list])) == 1
    assert len(set([m.shape[1] for m in m_list])) == 1

    new_m_value = np.array([(m.values != m.background_color).astype(np.int) for m in m_list]).sum(axis=0)
    new_m_value = (new_m_value == len(m_list)).astype(np.int)
    return Matter(new_m_value)


def bitwise_xor(m_list):

    assert len(set([m.shape[0] for m in m_list])) == 1
    assert len(set([m.shape[1] for m in m_list])) == 1

    new_m_value = np.array([(m.values != m.background_color).astype(np.int) for m in m_list]).sum(axis=0)
    new_m_value = (new_m_value % 2 == 1).astype(np.int)
    return Matter(new_m_value)


def bitwise_not_xor(m_list):

    assert len(set([m.shape[0] for m in m_list])) == 1
    assert len(set([m.shape[1] for m in m_list])) == 1

    new_m_value = np.array([(m.values != m.background_color).astype(np.int) for m in m_list]).sum(axis=0)
    new_m_value = (new_m_value % 2 == 0).astype(np.int)
    return Matter(new_m_value)


def bitwise_not_or(m_list):

    assert len(set([m.shape[0] for m in m_list])) == 1
    assert len(set([m.shape[1] for m in m_list])) == 1

    new_m_value = np.array([(m.values != m.background_color).astype(np.int) for m in m_list]).sum(axis=0)
    new_m_value = (new_m_value == 0).astype(np.int)
    return Matter(new_m_value)


def bitwise_not_and(m_list):

    assert len(set([m.shape[0] for m in m_list])) == 1
    assert len(set([m.shape[1] for m in m_list])) == 1

    new_m_value = np.array([(m.values != m.background_color).astype(np.int) for m in m_list]).sum(axis=0)
    new_m_value = (new_m_value < len(m_list)).astype(np.int)
    return Matter(new_m_value)
