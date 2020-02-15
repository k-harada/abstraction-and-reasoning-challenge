from dataclasses import dataclass
import numpy as np


class Matter:

    def __init__(self, x_list):
        """Class for keeping value
        :param x_list: List[List[int]]
        """
        self.value = np.array(x_list)
        self.shape = self.value.shape
        self.placement = [0, 0]
        self.color = -1
        self.background_color = 0

    def copy(self):
        x = Matter(self.value)
        x.shape = self.value.shape
        x.placement = self.placement.copy()
        x.color = self.color
        x.background_color = self.background_color
        return x


@dataclass
class CaseData:
    """Class for keeping case info"""
    base_value: np.int = 0
    color_value: np.array = np.zeros(10, dtype=np.int)
    background_color: np.int = 0

    def copy(self):
        return CaseData(self.base_value, self.color_value, self.background_color)


@dataclass
class ProblemData:
    """Class for keeping problem info"""
    base_value: np.int = 0
    color_value: np.array = np.zeros(10, dtype=np.int)
    background_color: np.int = 0

    def copy(self):
        return ProblemData(self.base_value, self.color_value, self.background_color)


class Problem:

    def __init__(self, data):
        self.len_train = len(data["train"])
        self.len_test = len(data["test"])
        self.problem_data = ProblemData()
        self.train_case_value_list = [[Matter(x["input"])] for x in data["train"]]
        self.train_case_data_list = [CaseData()] * self.len_train
        self.train_answer_value_list = [[Matter(x["output"])] for x in data["train"]]
        self.test_case_value_list = [[Matter(x["input"])] for x in data["test"]]
        self.test_case_data_list = [CaseData()] * self.len_test
        self.cost = 0
