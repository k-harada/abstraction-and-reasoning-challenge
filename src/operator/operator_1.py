import numpy as np
from src.data import Matter, TrainCase, TestCase, Problem


def split_color(problem):

    new_problem = problem.copy()
    new_problem.train_case_list = []
    new_problem.test_case_list = []

    for case in problem.train_case_list:
        new_case = case.copy()
        new_case.matter_list = []
        for m in case.matter_list:
            for c in range(10):
                if c == m.background_color:
                    continue
                if (m.value == c).sum() == 0:
                    continue
                new_m_value = np.ones(m.shape, dtype=np.int) * m.background_color
                new_m_value[m.value == c] = c
                matter_c = Matter(new_m_value)
                matter_c.color = c
                new_case.matter_list.append(matter_c)
        new_problem.train_case_list.append(new_case)

    for case in problem.test_case_list:
        new_case = case.copy()
        new_case.matter_list = []
        for m in case.matter_list:
            for c in range(10):
                if c == m.background_color:
                    continue
                if (m.value == c).sum() == 0:
                    continue
                new_m_value = np.ones(m.shape, dtype=np.int) * m.background_color
                new_m_value[m.value == c] = c
                matter_c = Matter(new_m_value)
                matter_c.color = c
                new_case.matter_list.append(matter_c)
        new_problem.test_case_list.append(new_case)

    return new_problem


def pick_one_color(problem, c):

    new_problem = problem.copy()
    new_problem.train_case_list = []
    new_problem.test_case_list = []

    for case in problem.train_case_list:
        new_case = case.copy()
        new_case.matter_list = []
        for m in case.matter_list:
            if c == m.background_color:
                continue
            new_m_value = np.ones(m.shape, dtype=np.int) * m.background_color
            new_m_value[m.value == c] = c
            matter_c = Matter(new_m_value)
            matter_c.color = c
            new_case.matter_list.append(matter_c)
        new_problem.train_case_list.append(new_case)

    for case in problem.test_case_list:
        new_case = case.copy()
        new_case.matter_list = []
        for m in case.matter_list:
            if c == m.background_color:
                continue
            new_m_value = np.ones(m.shape, dtype=np.int) * m.background_color
            new_m_value[m.value == c] = c
            matter_c = Matter(new_m_value)
            matter_c.color = c
            new_case.matter_list.append(matter_c)
        new_problem.test_case_list.append(new_case)

    return new_problem


def trim_background(problem):

    new_problem = problem.copy()
    new_problem.train_case_list = []
    new_problem.test_case_list = []

    for case in problem.train_case_list:
        new_case = case.copy()
        new_case.matter_list = []
        for m in case.matter_list:
            x_sum = (m.value != m.background_color).sum(axis=1)
            y_sum = (m.value != m.background_color).sum(axis=0)
            min_x = min([i for i in range(m.shape[0]) if x_sum[i]])
            max_x = max([i for i in range(m.shape[0]) if x_sum[i]])
            min_y = min([i for i in range(m.shape[1]) if y_sum[i]])
            max_y = max([i for i in range(m.shape[1]) if y_sum[i]])
            new_m_value = m.value[min_x:max_x + 1, min_y:max_y + 1]
            matter_c = Matter(new_m_value)
            matter_c.placement = [min_x, min_y]
            new_case.matter_list.append(matter_c)
        new_problem.train_case_list.append(new_case)

    for case in problem.test_case_list:
        new_case = case.copy()
        new_case.matter_list = []
        for m in case.matter_list:
            x_sum = (m.value != m.background_color).sum(axis=1)
            y_sum = (m.value != m.background_color).sum(axis=0)
            min_x = min([i for i in range(m.shape[0]) if x_sum[i]])
            max_x = max([i for i in range(m.shape[0]) if x_sum[i]])
            min_y = min([i for i in range(m.shape[1]) if y_sum[i]])
            max_y = max([i for i in range(m.shape[1]) if y_sum[i]])
            new_m_value = m.value[min_x:max_x + 1, min_y:max_y + 1]
            matter_c = Matter(new_m_value)
            matter_c.placement = [min_x, min_y]
            new_case.matter_list.append(matter_c)
        new_problem.test_case_list.append(new_case)

    return_flg = True

    for case in new_problem.train_case_list:
        y = case.output_matter_list[0]
        for x in case.matter_list:
            if x.shape != y.shape:
                return_flg = False
    if return_flg:
        return new_problem
    else:
        return None
