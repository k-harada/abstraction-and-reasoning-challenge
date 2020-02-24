from src.operator.matter.transform import *
from src.operator.matter.split import *
from src.operator.matter.reduce import *
from src.operator.arithmetic.color import *
from src.operator.case.color_operation import *


transformers = ["trim_background", "resize", "fractal", "paint"]
splitters = ["split_color", "split_row_2", "split_col_2"]
reducers = ["bitwise_or", "bitwise_and", "bitwise_xor", "bitwise_not_xor", "bitwise_not_or", "bitwise_not_and"]
problem_operators = ["set_problem_color"]
case_operators = ["pick_color", "max_color", "min_color", "count_color"]
all_operators = transformers + splitters + reducers + problem_operators + case_operators


class Operator:

    def __init__(self):
        pass

    @classmethod
    def run(cls, problem, command):  # problem -> problem
        if command in transformers:
            return cls.run_matter_transform(problem, command)
        elif command in splitters:
            return cls.run_matter_split(problem, command)
        elif command in reducers:
            return cls.run_matter_reduce(problem, command)
        elif command in problem_operators:
            return eval(f'{command}(problem)')
        elif command in case_operators:
            return cls.run_case_operators(problem, command)
        else:
            raise NotImplementedError

    @classmethod
    def run_matter_transform(cls, problem, command):  # matter -> matter

        new_problem = problem.copy()
        new_problem.train_case_list = []
        new_problem.test_case_list = []

        for case in problem.train_case_list:
            new_case = case.copy()
            new_case.matter_list = []
            for m in case.matter_list:
                new_case.matter_list.append(eval(f'{command}(m)'))
            new_problem.train_case_list.append(new_case)

        for case in problem.test_case_list:
            new_case = case.copy()
            new_case.matter_list = []
            for m in case.matter_list:
                new_case.matter_list.append(eval(f'{command}(m)'))
            new_problem.test_case_list.append(new_case)

        return new_problem

    @classmethod
    def run_matter_split(cls, problem, command):  # matter -> List[matter]

        new_problem = problem.copy()
        new_problem.train_case_list = []
        new_problem.test_case_list = []

        for case in problem.train_case_list:
            new_case = case.copy()
            new_case.matter_list = []
            for m in case.matter_list:
                res_list = eval(f'{command}(m)')
                for r in res_list:
                    new_case.matter_list.append(r)
            new_problem.train_case_list.append(new_case)

        for case in problem.test_case_list:
            new_case = case.copy()
            new_case.matter_list = []
            for m in case.matter_list:
                res_list = eval(f'{command}(m)')
                for r in res_list:
                    new_case.matter_list.append(r)
            new_problem.test_case_list.append(new_case)

        return new_problem

    @classmethod
    def run_matter_reduce(cls, problem, command):  # List[matter] -> matter

        new_problem = problem.copy()
        new_problem.train_case_list = []
        new_problem.test_case_list = []

        for case in problem.train_case_list:
            new_case = case.copy()
            new_case.matter_list = [eval(f'{command}(case.matter_list)')]
            new_problem.train_case_list.append(new_case)

        for case in problem.test_case_list:
            new_case = case.copy()
            new_case.matter_list = [eval(f'{command}(case.matter_list)')]
            new_problem.test_case_list.append(new_case)

        return new_problem

    @classmethod
    def run_case_operators(cls, problem, command):  # case -> case

        new_problem = problem.copy()
        new_problem.train_case_list = [eval(f'{command}(case)') for case in problem.train_case_list]
        new_problem.test_case_list = [eval(f'{command}(case)') for case in problem.test_case_list]

        return new_problem
