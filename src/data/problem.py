from dataclasses import dataclass
import numpy as np
from src.data.case import Case


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
        self.train_x_list = []
        self.train_y_list = []
        self.test_x_list = []

    def initialize(self, data):

        self.metadata = ProblemData()
        Problem.len_train = len(data["train"])
        Problem.len_test = len(data["test"])
        for x in data["train"]:
            c = Case()
            c.initialize(np.array(x["input"]))
            self.train_x_list.append(c)
            c = Case()
            c.initialize(np.array(x["output"]))
            self.train_y_list.append(c)
        for x in data["test"]:
            c = Case()
            c.initialize(np.array(x["input"]))
            self.test_x_list.append(c)

    def __repr__(self):

        s = []
        for cx, cy in zip(self.train_x_list, self.train_y_list):
            s.append(cx.__repr__() + "<->" + cy.__repr__())
        for c in self.test_x_list:
            s.append(c.__repr__())

        return "\n".join(s)

    def copy(self):

        new_problem = Problem()
        new_problem.metadata = self.metadata.copy()
        new_problem.train_x_list = self.train_x_list[:]  # shallow copy
        new_problem.train_y_list = self.train_y_list[:]  # shallow copy
        new_problem.test_x_list = self.test_x_list[:]  # shallow copy

        return new_problem

    def deep_copy(self):

        new_problem = Problem()
        new_problem.metadata = self.metadata.copy()
        new_problem.train_x_list = [c.deep_copy() for c in self.train_x_list]
        new_problem.train_y_list = [c.deep_copy() for c in self.train_y_list]
        new_problem.test_x_list = [c.deep_copy() for c in self.test_x_list]

        return new_problem
