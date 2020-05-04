import numpy as np


class Matter:
    """Class for objects inside case"""
    def __init__(self, values: np.array, x0: int = 0, y0: int = 0, background_color: int = 0):
        """
        :param values: np.array(np.int) main values
        :param x0: int, position to show in result, x0:x0+shape[0], y0:y0+shape[1]
        :param y0: int, position to show in result, x0:x0+shape[0], y0:y0+shape[1]
        :param background_color: np.int, color to be treated as background
        """
        if x0 < 0 or y0 < 0:
            raise ValueError
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
        self.a = None
        self.b = None
        self.bool_show = True
        self.is_mesh = False

    def is_square(self):
        if self.shape[0] == self.shape[1]:
            return True
        else:
            return False

    def color_count(self):
        """
        :return: np.array(10, int), number of cells for each color
        """
        return np.array([(self.values == c).sum() for c in range(10)]).astype(int)

    def n_color(self):
        """
        :return: int, number of colors other than background
        """
        color_count = self.color_count()
        return int(sum([color_count[c] > 0 for c in range(10) if c != self.background_color]))

    def repr_values(self):
        """
        :return: np.array(self.shape, int), simply return self.values
        """
        return self.values

    def n_cell(self):
        """
        :return: int, number of cells not background
        """
        return int((self.values != self.background_color).sum())

    def max_color(self):
        """
        :return: int, maximal color other than background
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
        return c_max

    def min_color(self):
        """
        :return: int, minimal color that exists other than background
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
        return int(c_min)

    def copy(self):
        new_matter = Matter(self.values.copy(), self.x0, self.y0, self.background_color)
        # copy attributes
        new_matter.a = self.a
        new_matter.b = self.b
        new_matter.bool_show = self.bool_show
        new_matter.is_mesh = self.is_mesh
        return new_matter

    def paste_color(self):
        assert self.a is not None
        new_values = self.values.copy()
        new_values[self.values != self.background_color] = self.a % 10
        new_matter = Matter(new_values, self.x0, self.y0, self.background_color)
        # copy attributes
        new_matter.a = self.a
        new_matter.b = self.b
        new_matter.bool_show = self.bool_show
        new_matter.is_mesh = self.is_mesh
        return new_matter


if __name__ == "__main__":
    m0 = Matter(np.array([[1, 2, 3], [2, 3, 5], [4, 8, 2]]))
    print(m0.color_count())
