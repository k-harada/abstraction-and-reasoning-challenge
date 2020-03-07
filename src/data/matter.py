import numpy as np


class Matter:
    """Class for objects inside case"""
    def __init__(self, values: np.array, x0: np.int = 0, y0: np.int = 0, background_color: np.int = 0):

        self.values = values
        self.x0 = x0
        self.y0 = y0
        self.x1 = self.x0 + self.values.shape[0]
        self.y1 = self.y0 + self.values.shape[1]

        # background
        self.background_color = background_color

        # color_count
        self.color_count = np.array([(self.values == c).sum() for c in range(10)]).astype(np.int).copy()

        # n_color
        self.n_color = np.int(sum([self.color_count[c] > 0 for c in range(10)]))

        # n_cell
        self.n_cell = np.int((self.values != self.background_color).sum())

        # shape
        self.shape = self.values.shape

        # square
        if self.shape[0] == self.shape[1]:
            self.is_square = True
        else:
            self.is_square = False

        # color
        if self.n_color == 1:
            self.color = np.argmax(self.n_color)
            self.max_color = self.color
        elif self.n_color == 2 and self.color_count[self.background_color] > 0:
            color_count_temp = self.color_count.copy()
            color_count_temp[self.background_color] = 0
            self.color = np.argmax(color_count_temp)
            self.max_color = self.color
        else:
            color_count_temp = self.color_count.copy()
            color_count_temp[self.background_color] = 0
            self.color = -1
            self.max_color = np.argmax(color_count_temp)

        # bool repr
        if self.color != -1:
            self.bool_repr = (self.values != self.background_color).astype(np.int)
            self.bool_repr_force = self.bool_repr
        else:
            self.bool_repr = None
            self.bool_repr_force = (self.values != self.background_color).astype(np.int)

    def __repr__(self):
        return str(self.values)

    def copy(self):
        return MatterFactory.copy(self)

    def deep_copy(self):
        return MatterFactory.deep_copy(self)


class MatterFactory:

    @classmethod
    def new(cls, values: np.array, x0: np.int = 0, y0: np.int = 0, background_color: np.int = 0):
        return Matter(values, x0, y0, background_color)

    @classmethod
    def copy(cls, m):
        """
        :param m: matter
        :return: new Matter
        """
        return Matter(m.values, m.x0, m.y0, m.background_color)

    @classmethod
    def deep_copy(cls, m):
        """
        :param m: matter
        :return: new Matter
        """
        return Matter(m.values.copy(), m.x0, m.y0, m.background_color)

    @classmethod
    def slice(cls, m, x0, x1, y0, y1):
        """
        :param m: matter
        :param x0: region to pick
        :param x1:
        :param y0:
        :param y1:
        :return: new Matter
        """
        return Matter(m.values[x0:x1, y0:y1].copy(), x0, y0, m.background_color)

    @classmethod
    def pick_one_color(cls, m, c):
        """
        :param m: matter
        :param c: int, color to pick up
        :return: new Matter
        """
        new_values = np.ones(m.values.shape, dtype=np.int) * m.background_color
        new_values[m.values == c] = c
        return Matter(new_values, m.x0, m.y0, m.background_color)

    @classmethod
    def paste_one_color(cls, m, c):
        """
        :param m: matter
        :param c: int, color to paste
        :return: new Matter
        """
        new_values = np.ones(m.values.shape, dtype=np.int) * c
        return Matter(new_values, m.x0, m.y0, m.background_color)

    @classmethod
    def paste_max_color(cls, m):
        """
        :param m: matter
        :return: new Matter
        """
        return cls.paste_one_color(m, m.max_color)
