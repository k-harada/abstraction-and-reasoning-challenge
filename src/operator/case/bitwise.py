import numpy as np
from src.data import MatterFactory, CaseFactory

# case -> case


def bitwise_operators(c):

    assert len(set([m.shape[0] for m in c.matter_list])) == 1
    assert len(set([m.shape[1] for m in c.matter_list])) == 1

    for m in c.matter_list:
        assert m.bool_repr is not None
    new_shape = c.matter_list[0].shape

    bool_repr_list = [m.bool_repr for m in c.matter_list]

    calculated_list = [
        bitwise_or(bool_repr_list), bitwise_and(bool_repr_list), bitwise_xor(bool_repr_list),
        bitwise_not_xor(bool_repr_list), bitwise_not_or(bool_repr_list), bitwise_not_and(bool_repr_list)
    ]
    matter_list = [MatterFactory.new(v) for v in calculated_list]
    print(calculated_list)
    print(calculated_list[0])
    return CaseFactory.from_matter_list(matter_list, new_shape, 0)


def bitwise_or(bool_repr_list):
    new_m_value = np.array(bool_repr_list).sum(axis=0)
    new_m_value = (new_m_value > 0).astype(np.int)
    return new_m_value


def bitwise_and(bool_repr_list):
    new_m_value = np.array(bool_repr_list).sum(axis=0)
    new_m_value = (new_m_value == len(bool_repr_list)).astype(np.int)
    return new_m_value


def bitwise_xor(bool_repr_list):
    new_m_value = np.array(bool_repr_list).sum(axis=0)
    new_m_value = (new_m_value % 2 == 1).astype(np.int)
    return new_m_value


def bitwise_not_xor(bool_repr_list):
    new_m_value = np.array(bool_repr_list).sum(axis=0)
    new_m_value = (new_m_value % 2 == 0).astype(np.int)
    return new_m_value


def bitwise_not_or(bool_repr_list):
    new_m_value = np.array(bool_repr_list).sum(axis=0)
    new_m_value = (new_m_value == 0).astype(np.int)
    return new_m_value


def bitwise_not_and(bool_repr_list):
    new_m_value = np.array(bool_repr_list).sum(axis=0)
    new_m_value = (new_m_value < len(bool_repr_list)).astype(np.int)
    return new_m_value
