from src.operator.matter.transform import *
from src.operator.matter.split import *
from src.operator.matter.map import *
from src.operator.problem.color import *
from src.operator.case import *
from src.data import CaseFactory

transformers = []
splitters = ["split_color", "split_row_2", "split_col_2", "split_rotations"]
mappers = []
reducers = []
problem_operators = ["set_problem_color"]
case_operators = [
    "bitwise_operators", "pick_max_color", "pick_min_color", "trim_background", "resize", "fractal",
    "auto_fill_row_col"
]
all_operators = transformers + splitters + mappers + reducers + problem_operators + case_operators


class Operator:

    def __init__(self):
        pass

    @classmethod
    def run(cls, problem, command):  # problem -> problem
        if command in transformers:
            return cls.run_matter_transform(problem, command)
        elif command in splitters:
            return cls.run_matter_split(problem, command)
        elif command in mappers:
            return cls.run_matter_map(problem, command)
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
        new_problem.train_x_list = []
        new_problem.test_x_list = []

        for case in problem.train_x_list:
            new_case = case.copy()
            new_case.matter_list = []
            for m in case.matter_list:
                new_case.matter_list.append(eval(f'{command}(m)'))
            new_problem.train_x_list.append(new_case)

        for case in problem.test_x_list:
            new_case = case.copy()
            new_case.matter_list = []
            for m in case.matter_list:
                new_case.matter_list.append(eval(f'{command}(m)'))
            new_problem.test_x_list.append(new_case)

        return new_problem

    @classmethod
    def run_matter_split(cls, problem, command):  # matter -> List[matter]
        new_problem = problem.copy()
        new_problem.train_x_list = []
        new_problem.test_x_list = []

        for case in problem.train_x_list:
            assert len(case.matter_list) <= 10
            new_case_matter_list = []
            for m in case.matter_list:
                res_list = eval(f'{command}(m)')
                for r in res_list:
                    new_case_matter_list.append(r)
            new_case = CaseFactory.from_matter_list(new_case_matter_list, case.shape, case.background_color)
            new_problem.train_x_list.append(new_case)

        for case in problem.test_x_list:
            assert len(case.matter_list) <= 10
            new_case_matter_list = []
            for m in case.matter_list:
                res_list = eval(f'{command}(m)')
                for r in res_list:
                    new_case_matter_list.append(r)
            new_case = CaseFactory.from_matter_list(new_case_matter_list, case.shape, case.background_color)

            new_problem.test_x_list.append(new_case)

        return new_problem

    @classmethod
    def run_matter_map(cls, problem, command):  # List[matter] -> List[matter]

        new_problem = problem.copy()
        new_problem.train_x_list = []
        new_problem.test_x_list = []

        for case in problem.train_x_list:
            new_case_matter_list = eval(f'{command}(case.matter_list)')
            new_case = CaseFactory.from_matter_list(new_case_matter_list, case.shape, case.background_color)
            new_problem.train_x_list.append(new_case)

        for case in problem.test_x_list:
            new_case_matter_list = eval(f'{command}(case.matter_list)')
            new_case = CaseFactory.from_matter_list(new_case_matter_list, case.shape, case.background_color)
            new_problem.test_x_list.append(new_case)

        return new_problem

    @classmethod
    def run_matter_reduce(cls, problem, command):  # List[matter] -> matter

        new_problem = problem.copy()
        new_problem.train_x_list = []
        new_problem.test_x_list = []

        for case in problem.train_x_list:
            new_case = case.copy()
            new_case.matter_list = [eval(f'{command}(case.matter_list)')]
            new_problem.train_x_list.append(new_case)

        for case in problem.test_x_list:
            new_case = case.copy()
            new_case.matter_list = [eval(f'{command}(case.matter_list)')]
            new_problem.test_x_list.append(new_case)

        return new_problem

    @classmethod
    def run_case_operators(cls, problem, command):  # case -> case

        new_problem = problem.copy()
        new_problem.train_x_list = [eval(f'{command}(case)') for case in problem.train_x_list]
        new_problem.test_x_list = [eval(f'{command}(case)') for case in problem.test_x_list]

        return new_problem
