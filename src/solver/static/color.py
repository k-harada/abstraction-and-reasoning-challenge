import numpy as np
from src.data import Problem


def set_problem_color(p: Problem) -> Problem:
    # only one color in
    # get color from output
    color_count = np.array([case.color_count for case in p.train_y_list]).sum(axis=0)
    # only color other than background
    color_count[p.background_color] = 0
    if (color_count > 0).sum() == 1:
        new_color = color_count.argmax()

        new_problem = p.copy()
        transform_rule = {i: new_color for i in range(10)}
        transform_rule[problem.metadata.background_color] = problem.metadata.background_color

        new_problem.train_x_list = [CaseFactory.color_transform(c, transform_rule) for c in problem.train_x_list]
        new_problem.test_x_list = [CaseFactory.color_transform(c, transform_rule) for c in problem.test_x_list]

        return new_problem
    else:
        return p
