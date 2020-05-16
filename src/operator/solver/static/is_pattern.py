import numpy as np
from src.data import Problem, Case


def set_is_pattern(p: Problem) -> None:
    
    case_y: Case
    y_values_new_list = []
    for case_y in p.train_y_list:
        y_values = case_y.repr_values()
        y_values_new = y_values * 0 - 1
        c = 0
        for i in range(y_values_new.shape[0]):
            for j in range(y_values_new.shape[1]):
                if y_values_new[i, j] == -1:
                    y_values_new[y_values == y_values[i, j]] = c
                    c += 1
        y_values_new_list.append(y_values_new)
    for k in range(1, len(y_values_new_list)):
        if y_values_new_list[0].shape != y_values_new_list[k].shape:
            return None
        if np.abs(y_values_new_list[0] - y_values_new_list[k]).sum() != 0:
            return None

    p.is_pattern = True
    return None
