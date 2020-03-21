import numpy as np

from src.data.matter import Matter


class MatterFactory:

    @classmethod
    def new(cls, values: np.array, x0: np.int8 = 0, y0: np.int8 = 0, background_color: np.int8 = 0):
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
