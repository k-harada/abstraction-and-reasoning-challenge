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

        # initialize_attributes
        self.m_row, self.m_col = 1, 1
        self.d_row, self.d_col = 1, 1
        self.a = None
        self.b = None
        self.color_add = None
        self.color_delete = None
        self.bool_show = True
        self.is_mesh = False

    def bool_represents(self):
        return (self.values != self.background_color).astype(np.bool)

    def is_square(self):
        if self.shape[0] == self.shape[1]:
            return True
        else:
            return False

    def color_count(self):
        """
        :return: np.array(10, int8), number of cells for each color
        """
        return np.array([(self.values == c).sum() for c in range(10)]).astype(np.int8)

    def n_color(self):
        """
        :return: np.int8, number of colors other than background
        """
        color_count = self.color_count()
        return np.int8(sum([color_count[c] > 0 for c in range(10) if c != self.background_color]))

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
        color_count = self.color_count()
        c_max = self.background_color
        temp = 0
        for c in range(10):
            if c == self.background_color:
                continue
            if color_count[c] > temp:
                temp = color_count[c]
                c_max = c
        return np.int8(c_max)

    def min_color(self):
        """
        :return: np.int8, minimal color that exists other than background
        """
        color_count = self.color_count()
        c_min = self.background_color
        temp = 999
        for c in range(10):
            if c == self.background_color:
                continue
            if 0 < color_count[c] < temp:
                temp = color_count[c]
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

    def copy(self):
        new_matter = Matter(self.values, self.x0, self.y0, self.background_color)
        # copy attributes
        new_matter.m_row, new_matter.m_col = self.m_row, self.m_col
        new_matter.d_row, new_matter.d_col = self.d_row, self.d_col
        new_matter.a = self.a
        new_matter.b = self.b
        new_matter.color_add = self.color_add
        new_matter.color_delete = self.color_delete
        new_matter.bool_show = self.bool_show
        new_matter.is_mesh = self.is_mesh
        return new_matter


if __name__ == "__main__":
    m0 = Matter(np.array([[1, 2, 3], [2, 3, 5], [4, 8, 2]]))
    print(m0.color_count())
