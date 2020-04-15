import os
import json
from heapq import heappush, heappop

from src.data import Problem
from src.runner import Runner, mappers, transformers, reducers, static_solvers, dynamic_solvers
from src.evaluator import eval_distance

CNT_MAX = 1000


def main(data):
    p = Problem()
    cnt = 0
    p.initialize(data)

    # static solvers
    for op in static_solvers:
        try:
            p = Runner.run_solve(p, op)
        except AssertionError:
            pass

    heap_queue = []
    heap_res = []
    heappush(heap_queue, (1, 0, 0, p))
    heappush(heap_res, (1, 0, 0, p))

    # mappers
    for op in mappers:
        cnt += 1
        v = 0
        try:
            q = Runner.run_map(p, op)
            # evaluate
            d = eval_distance(q)
            heappush(heap_queue, (d, v + 1, cnt, q))
            heappush(heap_res, (d, v + 1, cnt, q))
        except AssertionError:
            pass

    while len(heap_queue) > 0:
        _, v, _, p = heappop(heap_queue)
        p: Problem
        for op in transformers:
            cnt += 1
            try:
                # print(op, cnt)
                # print(p.__repr__())
                q = Runner.run_transform(p, op)
                # evaluate
                d = eval_distance(q)
                heappush(heap_queue, (d, v + 1, cnt, q))
                heappush(heap_res, (d, v + 1, cnt, q))
            except AssertionError:
                pass
        for op in reducers:
            cnt += 1
            try:
                q = Runner.run_reduce(p, op)
                # evaluate
                d = eval_distance(q)
                heappush(heap_queue, (d, v + 1, cnt, q))
                heappush(heap_res, (d, v + 1, cnt, q))
            except AssertionError:
                pass
        for op in dynamic_solvers:
            cnt += 1
            try:
                q = Runner.run_solve(p, op)
                # evaluate
                d = eval_distance(q)
                heappush(heap_queue, (d, v + 1, cnt, q))
                heappush(heap_res, (d, v + 1, cnt, q))
            except AssertionError:
                pass
        if cnt >= CNT_MAX:
            break
    # print(cnt)
    return heappop(heap_res)


if __name__ == "__main__":

    for i, f in enumerate(list(sorted(os.listdir("../input/training/")))):
        if i >= 50:
            continue
        print(i)
        if f[-5:] == ".json":
            sample_data = json.load(open(f'../input/training/{f}', "r"))
            r = main(sample_data)
            if r[0] == 0:
                print(i, f, r[1], r[2])
                # print(r)
    print(len(os.listdir("../input/training/")))
    """
    for i, f in enumerate(list(sorted(os.listdir("../input/evaluation/")))):

        if f[-5:] == ".json":
            sample_data = json.load(open(f'../input/evaluation/{f}', "r"))
            r = main(sample_data)
            if r[0] == 0:
                print(i, f, r[1], r[2])
                # print(r)
    print(len(os.listdir("../input/evaluation/")))
    """
