from src.operator.transform import *
from src.operator.split import *
from src.operator.reduce import *


transformers = ["trim_background"]
splitters = ["split_color", "split_row_2", "split_col_2"]
reducers = ["bitwise_or", "bitwise_and", "bitwise_xor", "bitwise_not_xor", "bitwise_not_or", "bitwise_not_and"]
all_operators = transformers + splitters + reducers


class Operator:

    def __init__(self):
        pass

    @classmethod
    def run(cls, problem, command):  # problem -> problem
        if command in transformers:
            return cls.run_transform(problem, command)
        elif command in splitters:
            return cls.run_split(problem, command)
        elif command in reducers:
            return cls.run_reduce(problem, command)
        else:
            raise NotImplementedError

    @classmethod
    def run_transform(cls, problem, command):  # problem -> problem

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
    def run_split(cls, problem, command):  # problem -> List[problem]

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
    def run_reduce(cls, problem, command):  # List[problem] -> problem

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
