import json
from src.data import Problem
from src.operator.operator_1 import split_color, pick_one_color, trim_background

sample_data = json.load(open("../../input/training/1cf80156.json", "r"))
p = Problem()
p.initialize(sample_data)

if __name__ == "__main__":
    print(p)
    q = p.copy()
    print(q)
    r = split_color(p)
    print(r)
    s = pick_one_color(p, 7)
    print(s)
    t = trim_background(p)
    print(t)
