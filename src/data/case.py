import numpy as np
from src.data.matter import Matter


class Case:
    """
    class for case data, responsible for reducers
    """
    def __init__(self, new=False, copy=False):
        self.matter_list = []
        self.background_color = None
        self.shape = None

        # initialize_attributes
        self.a = None
        self.b = None
        self.color_add = None
        self.color_delete = None
        self.repr_values_ = None
        self.shadow = None  # np.array, for fractal etc, rarely set
        if new or copy:
            pass
        else:
            raise ValueError

    def initialize(self, values: np.array, background_color: int = 0):
        self.matter_list = [Matter(values, background_color=background_color, new=True)]
        self.background_color = background_color
        self.shape = values.shape

        # initialize_attributes
        self.a = None
        self.b = None
        self.color_add = None
        self.color_delete = None
        self.repr_values_ = values
        self.shadow = None  # for fractal etc

    def color_count(self):
        """
        :return: np.array(10, int), number of cells for each color
        """
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
        new_case = Case(copy=True)
        new_case.background_color = self.background_color
        new_case.shape = self.shape
        # initialize_attributes
        new_case.a = self.a
        new_case.b = self.b
        new_case.color_add = self.color_add
        new_case.color_delete = self.color_delete
        new_case.repr_values_ = None
        new_case.shadow = self.shadow
        return new_case

    def __repr__(self):
        return "|" + "|".join(["".join(map(str, x)) for x in self.repr_values()]) + "|"

    def repr_values(self) -> np.array:

        if self.repr_values_ is not None:
            return self.repr_values_
        # pile up from 0
        # paste background
        repr_values = np.ones(self.shape, dtype=np.int) * self.background_color
        # collect values
        for m in self.matter_list:
            if not m.bool_show:
                continue
            for i in range(m.shape[0]):
                for j in range(m.shape[1]):
                    if self.color_add is None:
                        if m.values[i, j] != m.background_color:
                            repr_values[m.x0 + i, m.y0 + j] = m.values[i, j]
                    else:
                        if m.values[i, j] != m.background_color:
                            if m.values[i, j] != repr_values[m.x0 + i, m.y0 + j] != self.background_color:
                                repr_values[m.x0 + i, m.y0 + j] = self.color_add
                            else:
                                repr_values[m.x0 + i, m.y0 + j] = m.values[i, j]
        self.repr_values_ = repr_values
        return repr_values

    def repr_fractal_values(self) -> np.array:

        base_arr = self.repr_values()
        if self.shadow is None:
            shadow_arr = (base_arr != self.background_color).astype(np.bool)
        else:
            shadow_arr = self.shadow

        r1, c1 = base_arr.shape
        r2, c2 = shadow_arr.shape

        assert 0 < r1 * r2 <= 30
        assert 0 < c1 * c2 <= 30

        repr_values = np.ones((r1 * r2, c1 * c2), dtype=np.int) * self.background_color
        # basic
        if shadow_arr.dtype == 'bool':
            for i in range(r2):
                for j in range(c2):
                    if shadow_arr[i, j]:
                        repr_values[(i * r1):((i + 1) * r1), (j * c1):((j + 1) * c1)] = base_arr
        else:
            for i in range(r2):
                for j in range(c2):
                    add_arr = shadow_arr[i, j] * (base_arr != self.background_color).astype(np.int)
                    repr_values[(i * r1):((i + 1) * r1), (j * c1):((j + 1) * c1)] = add_arr

        return repr_values


if __name__ == "__main__":
    xv = (np.arange(30) % 10).reshape((5, 6)).astype(np.int)
    xv[0, :] = 0
    xv[-1, :] = 0
    case = Case()
    case.initialize(xv)
    print(case)
