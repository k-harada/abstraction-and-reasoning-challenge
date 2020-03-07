import numpy as np
from src.data import Matter

x = np.array([[0, 1, 2], [2, 3, 4], [0, 0, 0]])


if __name__ == "__main__":
    m = Matter(x)
    print(m.repr_string())
    m0 = m.slice(0, 2, 0, 2)
    print(m0.repr_string())
    m1 = m.pick_one_color(2)
    print(m1.repr_string())
    m2 = m.trim_background()
    print(m2.repr_string())
    print(m2.values)
    m3 = m.resize(2, 2)
    print(m3.repr_string())
    print(m3.values)
