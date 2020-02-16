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
        self.value = np.array(x_list)
        self.shape = self.value.shape
        self.placement = [0, 0]
        self.color = -1
        self.background_color = 0


@dataclass
class CaseData:
    """class for case metadata"""
    base_value: np.int = 0
    color_value: np.array = np.zeros(10, dtype=np.int)
    background_color: np.int = 0


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
            res_s.append("|" + "|".join(["".join(map(str, x)) for x in s.value.tolist()]) + "|")
        t_list = sum_up(self.output_matter_list, self.metadata.background_color)
        res_t = []
        for t in t_list:
            res_t.append("|" + "|".join(["".join(map(str, x)) for x in t.value.tolist()]) + "|")
        return ",".join(res_s) + "<->" + ",".join(res_t)

    def copy(self):

        new_case = TrainCase()
        new_case.metadata = self.metadata  # refer
        new_case.matter_list = self.matter_list[:]  # shallow copy
        new_case.output_matter_list = self.output_matter_list[:]  # shallow copy

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
            res_s.append("|" + "|".join(["".join(map(str, x)) for x in s.value.tolist()]) + "|")
        return ",".join(res_s)

    def copy(self):

        new_case = TestCase()
        new_case.metadata = self.metadata  # refer
        new_case.matter_list = self.matter_list[:]  # shallow copy

        return new_case


@dataclass
class ProblemData:
    """class for problem metadata"""
    base_value: np.int = 0
    color_value: np.array = np.zeros(10, dtype=np.int)
    background_color: np.int = 0
    cost: np.float = 0


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
        new_problem.metadata = self.metadata  # refer
        new_problem.train_case_list = self.train_case_list[:]  # shallow copy
        new_problem.test_case_list = self.test_case_list[:]  # shallow copy

        return new_problem
