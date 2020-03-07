import numpy as np
from src.data.matter import Matter


class Case:

    def __init__(self):
        self.matter_list = []
        self.background_color = None
        self.shape = None
        self.repr_values = None
        self.color_count = None

    def initialize(self, values, background_color=0):
        self.matter_list = [Matter(values=values, background_color=background_color)]
        self.background_color = background_color
        self.shape = values.shape
        self.repr_values = values
        self.color_count = np.array([(self.repr_values == c).sum() for c in range(10)], dtype=np.int)

    def update(self, shape, background_color):
        self.shape = shape
        self.background_color = background_color
        # shape
        # repr_values
        # color_count
        self.repr_values = np.ones(self.shape, dtype=np.int) * self.background_color
        for m in self.matter_list:
            self.repr_values[m.x0:m.x1, m.y0:m.y1] = m.values
        self.color_count = np.array([(self.repr_values == c).sum() for c in range(10)], dtype=np.int)

    def __repr__(self):
        return "|" + "|".join(["".join(map(str, x)) for x in self.repr_values.tolist()]) + "|"

    def copy(self):
        return CaseFactory.copy(self)

    def deep_copy(self):
        return CaseFactory.deep_copy(self)


class CaseFactory:

    @classmethod
    def copy(cls, c):
        new_case = Case()
        new_case.matter_list = c.matter_list[:]
        new_case.background_color = c.background_color
        new_case.shape = c.shape
        new_case.repr_values = c.repr_values
        new_case.color_count = c.color_count
        return new_case

    @classmethod
    def deep_copy(cls, c):
        new_case = Case()
        new_case.matter_list = [m.deep_copy() for m in c.matter_list[:]]
        new_case.background_color = c.background_color
        new_case.shape = c.shape
        new_case.repr_values = c.repr_values.copy()
        new_case.color_count = c.color_count.copy()
        return new_case

    @classmethod
    def from_values(cls, values, background_color=0):
        new_case = Case()
        new_case.initialize(values, background_color)
        return new_case

    @classmethod
    def from_matter_list(cls, matter_list, shape, background_color):
        new_case = Case()
        new_case.matter_list = matter_list
        new_case.update(shape, background_color)
        return new_case

    @classmethod
    def trim_background(cls, c):

        repr_values = c.repr_values

        x_sum = (repr_values != c.background_color).sum(axis=1)
        y_sum = (repr_values != c.background_color).sum(axis=0)

        assert x_sum.sum() >= 0

        min_x = min([i for i in range(repr_values.shape[0]) if x_sum[i]])
        max_x = max([i for i in range(repr_values.shape[0]) if x_sum[i]])
        min_y = min([i for i in range(repr_values.shape[1]) if y_sum[i]])
        max_y = max([i for i in range(repr_values.shape[1]) if y_sum[i]])

        new_values = repr_values[min_x:max_x + 1, min_y:max_y + 1].copy()
        new_case = Case()
        new_case.initialize(new_values, c.background_color)
        return new_case

    @classmethod
    def resize(cls, c, mr, mc):

        assert max(c.shape[0] * mr, c.shape[1] * mc) <= 30
        repr_values = c.repr_values
        new_values = np.repeat(np.repeat(repr_values, mr, axis=0), mc, axis=1)
        new_case = Case()
        new_case.initialize(new_values, c.background_color)
        return new_case

    @classmethod
    def fractal(cls, c):

        assert max(c.shape[0] ** 2, c.shape[1] ** 2) <= 30
        repr_values = c.repr_values
        new_values = np.ones((c.shape[0] ** 2, c.shape[1] ** 2), dtype=np.int) * c.background_color

        for i in range(c.shape[0]):
            for j in range(c.shape[1]):
                if repr_values[i, j] != c.background_color:
                    new_values[i * c.shape[0]:(i + 1) * c.shape[0], j * c.shape[1]:(j + 1) * c.shape[1]] = repr_values

        new_case = Case()
        new_case.initialize(new_values, c.background_color)
        return new_case

    @classmethod
    def color_transform(cls, c, transform_rule):

        repr_values = c.repr_values
        new_values = np.zeros(repr_values.shape, dtype=np.int)

        for i in range(10):
            new_values[repr_values == i] = transform_rule[i]

        new_case = Case()
        new_case.initialize(new_values, transform_rule[c.background_color])
        return new_case


if __name__ == "__main__":
    x = (np.arange(30) % 10).reshape((5, 6)).astype(np.int)
    x[0, :] = 0
    x[-1, :] = 0
    c = Case()
    c.initialize(x)
    d = CaseFactory.trim_background(c)
    print(c)
    print(d)
