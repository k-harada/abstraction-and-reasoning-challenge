import os
import json
from heapq import heappush, heappop
from src.data import Problem
from src.runner import Operator, all_operators
from src.evaluator import eval_distance

CNT_MAX = 30000


def main(data):
    p = Problem()
    cnt = 0
    p.initialize(data)
    heap_queue = []
    heap_res = []
    heappush(heap_queue, (1, 0, 0, p))
    heappush(heap_res, (1, 0, 0, p))

    while len(heap_queue) > 0:
        _, v, _, p = heappop(heap_queue)
        for op in all_operators:
            cnt += 1
            try:
                q = Operator.run(p, op)
                # evaluate
                d = eval_distance(q)
                heappush(heap_queue, (d, v + 1, cnt, q))
                heappush(heap_res, (d, v + 1, cnt, q))
            except AssertionError:
                pass
        if cnt >= CNT_MAX:
            break
    # print(cnt)
    r = heappop(heap_res)
    if r[0] == 0:
        return 0
    else:
        return 1


if __name__ == "__main__":

    for i, f in enumerate(list(sorted(os.listdir("../input/training/")))):
        if f[-5:] == ".json":
            sample_data = json.load(open(f'../input/training/{f}', "r"))
            if main(sample_data) == 0:
                print(i, f)
    print(len(os.listdir("../input/training/")))

