import numpy as np
from src.data import CaseFactory


def set_problem_color(problem):
    # TODO: extend general case, color table
    # only one color
    # get color from output
    color_count = np.array([case.color_count for case in problem.train_y_list]).sum(axis=0)
    # only color other than background
    color_count[problem.metadata.background_color] = 0
    assert (color_count > 0).sum() == 1
    new_color = color_count.argmax()

    new_problem = problem.copy()
    transform_rule = {i: new_color for i in range(10)}
    transform_rule[problem.metadata.background_color] = problem.metadata.background_color

    new_problem.train_x_list = [CaseFactory.color_transform(c, transform_rule) for c in problem.train_x_list]
    new_problem.test_x_list = [CaseFactory.color_transform(c, transform_rule) for c in problem.test_x_list]

    return new_problem
