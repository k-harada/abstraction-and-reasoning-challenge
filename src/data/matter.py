import numpy as np


class Matter:
    """Class for objects inside case"""
    def __init__(self, values: np.array, x0: np.int8 = 0, y0: np.int8 = 0, background_color: np.int8 = 0):
        """
        :param values: np.array(np.int8) main values
        :param x0: np.int8, position to show in result, x0:x0+shape[0], y0:y0+shape[1]
        :param y0: np.int8, position to show in result, x0:x0+shape[0], y0:y0+shape[1]
        :param background_color: np.int8, color to be treated as background
        """
        # values
        self.values = values
        # shape
        self.shape = self.values.shape
        # background
        self.background_color = background_color
        # position
        self.x0 = x0
        self.y0 = y0
        # color_count
        self.color_count = np.array([(self.values == c).sum() for c in range(10)]).astype(np.int8)

        # initialize_attributes
        self.n_row, self.n_col = self.values.shape
        self.m_row, self.m_col = 2, 2
        self.is_square = (self.n_row == self.n_col)
        self.bool_represents = (self.values != self.background_color).astype(np.bool)
        self.bool_copy = (self.values != self.background_color).astype(np.bool)
        self.a = self.n_color()
        self.b = self.n_cell()
        self.color_a = self.max_color()
        self.color_b = self.min_color()
        self.bool_show = True
        self.is_mesh = False

    def color_count(self):
        """
        :return: np.array(10, int8), number of cells for each color
        """
        return self.color_count

    def n_color(self):
        """
        :return: np.int8, number of colors other than background
        """
        return np.int8(sum([self.color_count[c] > 0 for c in range(10) if c != self.background_color]))

    def repr_values(self):
        """
        :return: np.array(self.shape, int8), simply return self.values
        """
        return self.values

    def n_cell(self):
        """
        :return: np.int8, number of cells not background
        """
        return np.int8((self.values != self.background_color).sum())

    def max_color(self):
        """
        :return: np.int8, maximal color other than background
        """
        c_max = self.background_color
        temp = 0
        for c in range(10):
            if c == self.background_color:
                continue
            if self.color_count[c] > temp:
                temp = self.color_count[c]
                c_max = c
        return np.int8(c_max)

    def min_color(self):
        """
        :return: np.int8, minimal color that exists other than background
        """
        c_min = self.background_color
        temp = 999
        for c in range(10):
            if c == self.background_color:
                continue
            if 0 < self.color_count[c] < temp:
                temp = self.color_count[c]
                c_min = c
        return np.int8(c_min)

    def set_attr(self, key, value):
        """
        sugar function for setattr, also set children
        :param key:
        :param value:
        :return:
        """
        self.__setattr__(key, value)


if __name__ == "__main__":
    m0 = Matter(np.array([[1, 2, 3], [2, 3, 5], [4, 8, 2]]))
    print(m0.color_count)
    print(m0.color_a)
    m0.set_attr("color_a", 9)
    print(m0.color_a)
