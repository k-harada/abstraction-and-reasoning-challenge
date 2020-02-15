import json
from src.data import Problem


def main(data):
    problem = Problem(data)


if __name__ == "__main__":
    sample_data = json.load(open("../input/training/007bbfb7.json", "r"))
    main(sample_data)

