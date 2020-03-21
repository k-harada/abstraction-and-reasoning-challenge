import numpy as np
from src.data.case import Case


class Problem:

    def __init__(self):

        self.train_x_list = []
        self.train_y_list = []
        self.test_x_list = []
        self.len_train = 0
        self.len_test = 0

        # initialize_attributes
        self.background_color = np.int8(0)
        self.shape = None
        self.color_map = None
        self.color_count = None
        self.n_row, self.n_col = None, None
        self.m_row, self.m_col = 2, 2
        self.a = None
        self.b = None
        self.color_a = None
        self.color_b = None

    def initialize(self, data):

        Problem.len_train = len(data["train"])
        Problem.len_test = len(data["test"])
        for x in data["train"]:
            c = Case()
            c.initialize(np.array(x["input"]), self.background_color)
            self.train_x_list.append(c)
            c = Case()
            c.initialize(np.array(x["output"]), self.background_color)
            self.train_y_list.append(c)
        for x in data["test"]:
            c = Case()
            c.initialize(np.array(x["input"]), self.background_color)
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
        new_problem.train_x_list = self.train_x_list[:]  # shallow copy
        new_problem.train_y_list = self.train_y_list[:]  # shallow copy
        new_problem.test_x_list = self.test_x_list[:]  # shallow copy

        new_problem.len_train = self.len_train
        new_problem.len_test = self.len_test

        new_problem.background_color = self.background_color
        new_problem.shape = self.shape
        new_problem.color_map = self.color_map
        new_problem.color_count = self.color_count
        new_problem.n_row, new_problem.n_col = self.n_row, self.n_col
        new_problem.m_row, new_problem.m_col = self.m_row, self.m_col
        new_problem.a = self.a
        new_problem.b = self.b
        new_problem.color_a = self.color_a
        new_problem.color_b = self.color_b

        return new_problem

    def judge(self):
        ac = 0
        wa = 0
        for cx, cy in zip(self.train_x_list, self.train_y_list):
            if cx.__repr__() == cy.__repr__():
                ac += 1
            else:
                wa += 1
        return ac, ac + wa
