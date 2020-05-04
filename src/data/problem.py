import numpy as np
from src.data.case import Case


class Problem:

    def __init__(self):

        self.train_x_list = []
        self.train_y_list = []
        self.test_x_list = []
        self.train_x_initial_list = []
        self.test_x_initial_list = []
        self.len_train = 0
        self.len_test = 0

        # initialize_attributes
        self.background_color = np.int(0)
        self.color_map = None
        self.color_count = None
        self.a = None
        self.b = None
        self.color_add = None
        self.color_b = None
        self.is_pattern = False
        self.is_same_shape = False
        self.history = []

    def initialize(self, data):

        Problem.len_train = len(data["train"])
        Problem.len_test = len(data["test"])
        for x in data["train"]:
            c = Case()
            c.initialize(np.array(x["input"], dtype=np.int), self.background_color)
            self.train_x_list.append(c)
            self.train_x_initial_list.append(c)
            c = Case()
            c.initialize(np.array(x["output"], dtype=np.int), self.background_color)
            self.train_y_list.append(c)
        for x in data["test"]:
            c = Case()
            c.initialize(np.array(x["input"], dtype=np.int), self.background_color)
            self.test_x_list.append(c)
            self.test_x_initial_list.append(c)

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
        new_problem.train_x_initial_list = self.train_x_initial_list[:]  # shallow copy
        new_problem.test_x_initial_list = self.test_x_initial_list[:]  # shallow copy

        new_problem.len_train = self.len_train
        new_problem.len_test = self.len_test

        new_problem.background_color = self.background_color
        new_problem.color_map = self.color_map
        new_problem.color_count = self.color_count
        new_problem.a = self.a
        new_problem.b = self.b
        new_problem.color_add = self.color_add
        new_problem.color_b = self.color_b
        new_problem.is_pattern = self.is_pattern
        new_problem.is_same_shape = self.is_same_shape
        new_problem.history = self.history.copy()

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
