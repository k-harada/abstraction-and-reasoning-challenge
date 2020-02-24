from dataclasses import dataclass
import numpy as np


def sum_up(x_arr_list, background_color):

    if len(x_arr_list) == 1:
        return x_arr_list

    # need to be same
    if set([x_arr.shape for x_arr in x_arr_list]) != 1:
        return x_arr_list

    # no overlap other than background_color
    if np.array([(x_arr != background_color).astype(np.int) for x_arr in x_arr_list]).sum(axis=0).max() > 1:
        return x_arr_list

    return [np.array([x_arr - background_color for x_arr in x_arr_list]).sum(axis=0) + background_color]


class Matter:
    """Class for objects inside case"""

    def __init__(self, x_list):
        """
        :param x_list: List[List[int]] or np.array
        """
        self.values = np.array(x_list)
        self.shape = self.values.shape
        self.placement = [0, 0]
        self.color = -1
        self.background_color = 0
        self.base_value = 0

    def __repr__(self):
        return "|" + "|".join(["".join(map(str, x)) for x in self.values.tolist()]) + "|"

    def copy(self):
        m = Matter(self.values)
        m.placement = self.placement.copy()
        m.color = self.color
        m.background_color = self.background_color
        m.base_value = self.base_value
        return m

    def deep_copy(self):
        return self.copy()


@dataclass
class CaseData:
    """class for case metadata"""
    base_value: np.int = 0
    color_value: np.array = np.zeros(10, dtype=np.int)
    background_color: np.int = 0
    color: np.int = -1

    def copy(self):
        return CaseData(self.base_value, self.color_value.copy(), self.background_color)


class TrainCase:
    """Class for keeping train case info"""

    def __init__(self):

        self.metadata = None
        self.matter_list = []
        self.output_matter_list = []

    def initialize(self, input_x_list, output_x_list):
        """
        :param input_x_list: List[List[int]] or np.array, input image
        :param output_x_list: List[List[int]] or np.array, output image
        """
        self.metadata = CaseData()
        self.matter_list.append(Matter(input_x_list))
        self.output_matter_list.append(Matter(output_x_list))

    def __repr__(self):

        s_list = sum_up(self.matter_list, self.metadata.background_color)
        res_s = []
        for s in s_list:
            res_s.append("|" + "|".join(["".join(map(str, x)) for x in s.values.tolist()]) + "|")
        t_list = sum_up(self.output_matter_list, self.metadata.background_color)
        res_t = []
        for t in t_list:
            res_t.append("|" + "|".join(["".join(map(str, x)) for x in t.values.tolist()]) + "|")
        return ",".join(res_s) + "<->" + ",".join(res_t)

    def copy(self):

        new_case = TrainCase()
        new_case.metadata = self.metadata.copy()
        new_case.matter_list = self.matter_list[:]  # shallow copy
        new_case.output_matter_list = self.output_matter_list[:]  # shallow copy

        return new_case

    def deep_copy(self):

        new_case = TrainCase()
        new_case.metadata = self.metadata.copy()
        new_case.matter_list = [m.deep_copy() for m in self.matter_list]
        new_case.output_matter_list = [m.deep_copy() for m in self.output_matter_list]

        return new_case


class TestCase:
    """Class for keeping test case info"""

    def __init__(self):

        self.metadata = None
        self.matter_list = []

    def initialize(self, input_x_list):
        """
        :param input_x_list: List[List[int]] or np.array, input image
        """
        self.metadata = CaseData()
        self.matter_list.append(Matter(input_x_list))

    def __repr__(self):

        s_list = sum_up(self.matter_list, self.metadata.background_color)
        res_s = []
        for s in s_list:
            res_s.append("|" + "|".join(["".join(map(str, x)) for x in s.values.tolist()]) + "|")
        return ",".join(res_s)

    def copy(self):

        new_case = TestCase()
        new_case.metadata = self.metadata.copy()
        new_case.matter_list = self.matter_list[:]  # shallow copy

        return new_case

    def deep_copy(self):

        new_case = TestCase()
        new_case.metadata = self.metadata.copy()
        new_case.matter_list = [m.deep_copy() for m in self.matter_list]

        return new_case


@dataclass
class ProblemData:
    """class for problem metadata"""
    base_value: np.int = 0
    color_value: np.array = np.zeros(10, dtype=np.int)
    background_color: np.int = 0
    cost: np.float = 0
    color: np.int = -1

    def copy(self):
        return ProblemData(self.base_value, self.color_value.copy(), self.background_color, self.cost)


class Problem:

    len_train = 0
    len_test = 0

    def __init__(self):

        self.metadata = None
        self.train_case_list = []
        self.test_case_list = []

    def initialize(self, data):

        self.metadata = ProblemData()
        Problem.len_train = len(data["train"])
        Problem.len_test = len(data["test"])
        for x in data["train"]:
            c = TrainCase()
            c.initialize(x["input"], x["output"])
            self.train_case_list.append(c)
        for x in data["test"]:
            c = TestCase()
            c.initialize(x["input"])
            self.test_case_list.append(c)

    def __repr__(self):

        s = []
        for c in self.train_case_list:
            s.append(c.__repr__())
        for c in self.test_case_list:
            s.append(c.__repr__())

        return "\n".join(s)

    def copy(self):

        new_problem = Problem()
        new_problem.metadata = self.metadata.copy()
        new_problem.train_case_list = self.train_case_list[:]  # shallow copy
        new_problem.test_case_list = self.test_case_list[:]  # shallow copy

        return new_problem

    def deep_copy(self):

        new_problem = Problem()
        new_problem.metadata = self.metadata.copy()
        new_problem.train_case_list = [c.deep_copy() for c in self.train_case_list]
        new_problem.test_case_list = [c.deep_copy() for c in self.test_case_list]

        return new_problem
