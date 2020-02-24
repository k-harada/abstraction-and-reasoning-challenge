import numpy as np


def set_problem_color(problem):

    # get color from output
    color_count = np.zeros(10, dtype=np.int)
    for case in problem.train_case_list:
        for m in case.output_matter_list:
            for c in range(10):
                if c != problem.metadata.background_color:
                    color_count[c] += (m.values == c).sum()

    # only color other than background
    assert (color_count > 0).sum() == 1

    new_color = color_count.argmax()
    assert problem.metadata.color != new_color

    new_problem = problem.deep_copy()
    new_problem.metadata.color = new_color
    for case in new_problem.train_case_list:
        case.metadata.color = new_color
        for m in case.matter_list:
            m.color = new_color
    for case in new_problem.test_case_list:
        case.metadata.color = new_color
        for m in case.matter_list:
            m.color = new_color

    return new_problem
