from src.runner.runner import Runner
from src.adityaork.tree import predict_from_json

if __name__ == "__main__":
    p = Runner(14, file_list="train", verbose=True)
    s = predict_from_json(p.task_json)
    print(s)
    p = Runner(15, file_list="train", verbose=True)
    s = predict_from_json(p.task_json)
    print(s)
