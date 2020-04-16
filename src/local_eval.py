import os
import sys
import json
import time
from heapq import heappush, heappop
import tqdm

from src.data import Problem
from src.runner import Runner, mappers, transformers, reducers, static_solvers, dynamic_solvers
from src.evaluator import eval_distance

TIME_LIMIT = 0.1


def auto_solve(data, time_limit=TIME_LIMIT):
    p = Problem()
    cnt = 0
    p.initialize(data)

    # for return
    len_test = len(p.test_x_list)
    res_dict = dict()
    for sub_id in range(len_test):
        res_dict[sub_id] = []

    # time
    t0 = time.time()
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

    # main search
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
        # break by time
        if time.time() >= t0 + time_limit:
            break
    # print(cnt)

    # output
    for sub_id in range(len_test):
        res_dict[sub_id] = []
    go_flg = True
    while len(heap_res) > 0 and go_flg:
        _, _, _, r = heappop(heap_res)
        for sub_id in range(len_test):
            s = r.test_x_list[sub_id].__repr__()
            if s not in res_dict[sub_id]:
                if len(res_dict[sub_id]) < 3:
                    res_dict[sub_id].append(s)
                elif min([len(res_dict[sub_id]) for sub_id in range(len_test)]) >= 3:
                    go_flg = False
                else:
                    pass

    return res_dict


def local_eval(dir_path, time_limit=TIME_LIMIT):

    total_ac = 0
    total_wa = 0

    for i, f in tqdm.tqdm(enumerate(list(sorted(os.listdir(dir_path))))):
        if f[-5:] == ".json":
            sample_data = json.load(open(f'{dir_path + f}', "r"))
            # print(sample_data)
            solved_dict = auto_solve(sample_data, time_limit=time_limit)
            for j in solved_dict.keys():
                assert len(solved_dict[j]) <= 3
                if len(solved_dict[j]) != 3:
                    print(i, j, len(solved_dict[j]))
                answer_arr = sample_data["test"][j]["output"]
                answer_str = "|" + "|".join(["".join(map(str, x)) for x in answer_arr]) + "|"
                if answer_str in solved_dict[j]:
                    # print(f'AC: {i, j}')
                    total_ac += 1
                else:
                    # print(f'WA: {i, j}')
                    total_wa += 1

    print(f'{dir_path} done, AC: {total_ac}, total: {total_ac + total_wa}, {1 - total_ac / (total_ac + total_wa)}')


if __name__ == "__main__":

    local_eval("../input/training/")
    local_eval("../input/evaluation/")
