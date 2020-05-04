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
        # self.color_map = None
        # self.color_count = None
        # initialize_attributes
        self.n_row, self.n_col = None, None
        self.m_row, self.m_col = None, None
        self.d_row, self.d_col = None, None
        self.a = None
        self.b = None
        self.color_add = None
        self.color_b = None
        self.reducer = None
        self.pick_ind = None

    def initialize(self, values: np.array, background_color: int = 0):
        self.matter_list.append(Matter(values, background_color=background_color))
        self.background_color = background_color
        self.shape = values.shape
        # self.color_map = {np.int(i): np.int(i) for i in range(10)}
        # self.color_count = np.array([(values == c).sum() for c in range(10)]).astype(np.int)
        # initialize_attributes
        self.reducer = "simple"
        self.n_row, self.n_col = self.shape
        self.m_row, self.m_col = 1, 1
        self.d_row, self.d_col = 1, 1
        self.color_add = self.max_color()
        self.color_b = self.min_color()
        self.pick_ind = 0

    def color_count(self):
        """
        :return: np.array(10, int), number of cells for each color
        """
        # self.color_count = np.array([(self.values == c).sum() for c in range(10)]).astype(np.int)
        repr_values = self.repr_values()
        return np.array([(repr_values == c).sum() for c in range(10)]).astype(np.int)

    def n_color(self):
        """
        :return: int, number of colors other than background
        """
        return int(sum([self.color_count()[c] > 0 for c in range(10) if c != self.background_color]))

    def max_color(self):
        """
        :return: int, maximal color other than background
        """
        c_max = self.background_color
        temp = 0
        for c in range(10):
            if c == self.background_color:
                continue
            if self.color_count()[c] > temp:
                temp = self.color_count()[c]
                c_max = c
        return int(c_max)

    def min_color(self):
        """
        :return: int, minimal color that exists other than background
        """
        c_min = self.background_color
        temp = 999
        for c in range(10):
            if c == self.background_color:
                continue
            if 0 < self.color_count()[c] < temp:
                temp = self.color_count()[c]
                c_min = c
        return int(c_min)

    def copy(self):
        new_case = Case()
        new_case.background_color = self.background_color
        new_case.shape = self.shape
        # new_case.color_map = self.color_map
        # new_case.color_count = self.color_count
        # initialize_attributes
        new_case.n_row, new_case.n_col = self.n_row, self.n_col
        new_case.m_row, new_case.m_col = self.m_row, self.m_col
        new_case.d_row, new_case.d_col = self.d_row, self.d_col
        new_case.a = self.a
        new_case.b = self.b
        new_case.color_add = self.color_add
        new_case.color_b = self.color_b
        new_case.reducer = self.reducer
        new_case.pick_ind = self.pick_ind
        return new_case

    def __repr__(self):
        return "|" + "|".join(["".join(map(str, x)) for x in self.repr_values()]) + "|"

    def repr_values(self) -> np.array:
        # paste background
        repr_values = self.reduce_values()
        # try:
        #    # color map
        #    for i in range(self.shape[0]):
        #        for j in range(self.shape[1]):
        #            repr_values[i, j] = self.color_map[repr_values[i, j]]
        #except KeyError:  # sometimes -1
        #    pass

        return repr_values

    def reduce_values(self) -> np.array:

        if self.reducer == "simple":
            # pile up from 0
            # paste background
            repr_values = np.ones(self.shape, dtype=np.int) * self.background_color
            # collect values
            for m in self.matter_list:
                if not m.bool_show:
                    continue
                for i in range(m.shape[0]):
                    for j in range(m.shape[1]):
                        if m.values[i, j] != m.background_color:
                            repr_values[m.x0 + i, m.y0 + j] = m.values[i, j]
            return repr_values

        elif self.reducer == "pick":
            # trim and pick one
            pick_ind = self.pick_ind % len(self.matter_list)
            repr_values = self.matter_list[pick_ind].values
            self.shape = repr_values.shape
            return repr_values

        elif self.reducer == "bitwise":
            assert len(self.matter_list) >= 2
            m0 = self.matter_list[0]
            m1 = self.matter_list[1 % len(self.matter_list)]

            assert m0.shape == m1.shape
            # reshape
            self.shape = m0.shape

            # fit color later
            repr_values = np.zeros(self.shape, dtype=np.int)

            for i in range(m0.shape[0]):
                for j in range(m0.shape[1]):
                    if m0.values[i, j] != m0.background_color:
                        repr_values[i, j] += 1

            for i in range(m1.shape[0]):
                for j in range(m1.shape[1]):
                    if m1.values[i, j] != m1.background_color:
                        repr_values[i, j] += 2
            return repr_values

        elif self.reducer == "fractal":

            m1 = self.matter_list[0]
            m2 = self.matter_list[1 % len(self.matter_list)]

            r1, c1 = m1.shape
            r2, c2 = m2.shape
            if max(r1 * r2, c1 * c2) <= 30:
                self.shape = (r1 * r2, c1 * c2)
                repr_values = np.ones(self.shape, dtype=np.int) * self.background_color
                for i in range(r2):
                    for j in range(c2):
                        if m2.values[i, j] != m2.background_color:
                            repr_values[(i * r1):((i + 1) * r1), (j * c1):((j + 1) * c1)] = m1.values
                return repr_values
            else:
                self.shape = (30, 30)
                return np.zeros((30, 30), dtype=np.int)


if __name__ == "__main__":
    xv = (np.arange(30) % 10).reshape((5, 6)).astype(np.int)
    xv[0, :] = 0
    xv[-1, :] = 0
    case = Case()
    case.initialize(xv)
    print(case)
