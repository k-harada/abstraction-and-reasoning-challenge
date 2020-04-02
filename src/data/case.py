import numpy as np
from src.data.matter import Matter


class Case:
    """
    class for case data, responsible for reducers
    """
    def __init__(self):
        self.matter_list = []
        self.background_color = None
        self.shape = None
        self.color_map = None
        self.color_count = None
        # initialize_attributes
        self.n_row, self.n_col = None, None
        self.m_row, self.m_col = None, None
        self.a = None
        self.b = None
        self.color_add = None
        self.color_b = None

    def initialize(self, values: np.array, background_color: np.int8 = 0):
        self.matter_list.append(Matter(values, background_color=background_color))
        self.background_color = background_color
        self.shape = values.shape
        self.color_map = {np.int8(i): np.int8(i) for i in range(10)}
        self.color_count = np.array([(values == c).sum() for c in range(10)]).astype(np.int8)
        # initialize_attributes
        self.n_row, self.n_col = self.shape
        self.m_row, self.m_col = 2, 2
        self.color_add = self.max_color()
        self.color_b = self.min_color()

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

    def copy(self):
        new_case = Case()
        new_case.background_color = self.background_color
        new_case.shape = self.shape
        new_case.color_map = self.color_map
        new_case.color_count = self.color_count
        # initialize_attributes
        new_case.n_row, new_case.n_col = self.n_row, self.n_col
        new_case.m_row, new_case.m_col = self.m_row, self.m_col
        new_case.a = self.a
        new_case.b = self.b
        new_case.color_add = self.color_add
        new_case.color_b = self.color_b
        return new_case

    def __repr__(self):
        return "|" + "|".join(["".join(map(str, x)) for x in self.repr_values().tolist()]) + "|"

    def repr_values(self) -> np.array:
        # paste background
        repr_values = np.ones(self.shape, dtype=np.int8) * self.background_color
        # collect values
        for m in self.matter_list:
            if not m.bool_show:
                continue
            for i in range(m.shape[0]):
                for j in range(m.shape[1]):
                    if m.values[i, j] != m.background_color:
                        repr_values[m.x0 + i, m.y0 + j] = m.values[i, j]
        # color map
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                repr_values[i, j] = self.color_map[repr_values[i, j]]

        return repr_values

    def repr_binary_values(self) -> np.array:
        # paste background
        repr_binary_values = np.zeros(self.shape, dtype=np.bool)
        # collect values
        for m in self.matter_list:
            if not m.bool_show:
                continue
            binary_matter = m.bool_represents()
            for i in range(m.shape[0]):
                for j in range(m.shape[1]):
                    if binary_matter[i, j]:
                        repr_binary_values[m.x0 + i, m.y0 + j] = True

        return repr_binary_values


if __name__ == "__main__":
    xv = (np.arange(30) % 10).reshape((5, 6)).astype(np.int)
    xv[0, :] = 0
    xv[-1, :] = 0
    case = Case()
    case.initialize(xv)
    print(case)
