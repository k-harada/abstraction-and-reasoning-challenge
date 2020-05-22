import os
import json
import numpy as np
from src.data.case import Case


train_file_list = list(sorted(os.listdir(os.path.join(os.path.dirname(__file__), "../../input/training/"))))
eval_file_list = list(sorted(os.listdir(os.path.join(os.path.dirname(__file__), "../../input/evaluation/"))))

SHAPE_DIFF_FLAG = 10000
VAL_ILLEGAL = 100
VAL_DIFF = 1


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
        self.color_delete = None
        self.is_pattern = False
        self.is_same_shape = False
        self.is_line_symmetry_row = False
        self.is_line_symmetry_col = False
        self.is_periodic_row = False
        self.is_periodic_col = False
        self.is_rot_symmetry = False
        self.history = []
        self.mapper = "identity"

    def initialize(self, data):

        self.len_train = len(data["train"])
        self.len_test = len(data["test"])
        for x in data["train"]:
            c = Case(new=True)
            c.initialize(np.array(x["input"], dtype=np.int), self.background_color)
            self.train_x_list.append(c)
            self.train_x_initial_list.append(c)
            c = Case(new=True)
            c.initialize(np.array(x["output"], dtype=np.int), self.background_color)
            self.train_y_list.append(c)
        for x in data["test"]:
            c = Case(new=True)
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
        new_problem.color_delete = self.color_delete
        new_problem.is_pattern = self.is_pattern
        new_problem.is_same_shape = self.is_same_shape
        new_problem.is_line_symmetry_row = self.is_line_symmetry_row
        new_problem.is_line_symmetry_col = self.is_line_symmetry_col
        new_problem.is_periodic_row = self.is_periodic_row
        new_problem.is_periodic_col = self.is_periodic_col
        new_problem.is_rot_symmetry = self.is_rot_symmetry
        new_problem.history = self.history.copy()
        new_problem.mapper = self.mapper
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

    @staticmethod
    def load(i, kbn="train"):
        if kbn == "train":
            with open(os.path.join(os.path.dirname(__file__), f"../../input/training/{train_file_list[i]}"), "r") as f:
                data = json.load(f)
                p = Problem()
                p.initialize(data)
        else:
            with open(os.path.join(os.path.dirname(__file__), f"../../input/evaluation/{eval_file_list[i]}"), "r") as f:
                data = json.load(f)
                p = Problem()
                p.initialize(data)
        return p

    def eval_distance(self) -> np.int:

        res_base = 0
        res_fractal = 1
        case_x: Case
        case_y: Case

        # normal
        for case_x, case_y in zip(self.train_x_list, self.train_y_list):

            x_values = case_x.repr_values()
            y_values = case_y.repr_values()

            # normal reducer
            # shape
            if x_values.shape != y_values.shape:
                shape_0 = min(x_values.shape[0], y_values.shape[0])
                shape_1 = min(x_values.shape[1], y_values.shape[1])
                res_base += SHAPE_DIFF_FLAG * abs(
                    x_values.shape[0] * x_values.shape[1] + y_values.shape[0] * y_values.shape[1] - 2 * shape_0 * shape_1
                )
            else:
                # values
                res_base += VAL_DIFF * (x_values != y_values).sum()
                res_base += VAL_ILLEGAL * (x_values < 0).sum()
                res_base += VAL_ILLEGAL * (x_values >= 10).sum()

        # fractal reducer
        for case_x, case_y in zip(self.train_x_list, self.train_y_list):

            r1, c1 = case_x.shape
            if case_x.shadow is None:
                r2, c2 = case_x.shape
            else:
                r2, c2 = case_x.shadow.shape

            y_values = case_y.repr_values()

            if (r1 * r2, c1 * c2) == case_y.shape:
                x_values = case_x.repr_fractal_values()

                # normal reducer
                # shape
                if x_values.shape != y_values.shape:
                    shape_0 = min(x_values.shape[0], y_values.shape[0])
                    shape_1 = min(x_values.shape[1], y_values.shape[1])
                    res_fractal += SHAPE_DIFF_FLAG * abs(
                        x_values.shape[0] * x_values.shape[1] + y_values.shape[0] * y_values.shape[1] - 2 * shape_0 * shape_1
                    )
                else:
                    # values
                    res_fractal += VAL_DIFF * (x_values != y_values).sum()
                    res_fractal += VAL_ILLEGAL * (x_values < 0).sum()
                    res_fractal += VAL_ILLEGAL * (x_values >= 10).sum()
            else:
                res_fractal += SHAPE_DIFF_FLAG * abs(
                    r1 * r2 * c1 * c2 - y_values.shape[0] * y_values.shape[1]
                )

        res = min(res_base, res_fractal)
        return res
