def eval_distance(problem):

    res = 0

    for case in problem.train_case_list:
        # length 1
        if len(case.matter_list) == 1 and len(case.output_matter_list) == 1:
            if case.matter_list[0].__repr__() == case.output_matter_list[0].__repr__():
                res += 0
            else:
                res += 1
        else:
            res += 1

    return res
