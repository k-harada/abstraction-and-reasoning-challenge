import json
from src.data import Problem

sample_data = json.load(open("../../input/training/1cf80156.json", "r"))
p = Problem()
p.initialize(sample_data)

if __name__ == "__main__":
    print(p)
    q = p.copy()
    print(q)
    r = q.deep_copy()
    print(r)
