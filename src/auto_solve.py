import os
import sys
import json
import time
from heapq import heappush, heappop

from src.data import Problem
from src.runner import Runner, mappers, reducers, transformers, static_solvers, dynamic_solvers
from src.evaluator import eval_distance

TIME_LIMIT = 2.0

train_file_list = list(sorted(os.listdir("../input/training/")))
eval_file_list = list(sorted(os.listdir("../input/evaluation/")))


def auto_solve(data, time_limit=TIME_LIMIT):
    p = Problem()
    cnt = 1
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
            p = Runner.pre_solve(p, op)
        except AssertionError:
            pass

    heap_queue = []
    heap_res = []
    d = eval_distance(p)
    heappush(heap_queue, (1, 0, 0, p))
    heappush(heap_res, (d, 0, 0, p))

    # mappers and reducers
    for map_op in mappers:
        for reduce_op in reducers:
            try:
                q = Runner.set_map_reduce(p, map_op, reduce_op)
                # evaluate
                d = eval_distance(q)
                heappush(heap_queue, (d, 0, cnt, q))
                heappush(heap_res, (d, 0, cnt, q))
                cnt += 1
            except AssertionError:
                pass

    # main search
    while len(heap_queue) > 0:
        _, v, cnt_old, p = heappop(heap_queue)
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
            try:
                s = r.test_x_list[sub_id].__repr__()
                if s not in res_dict[sub_id]:
                    if len(res_dict[sub_id]) < 3:
                        res_dict[sub_id].append(s)
                    elif min([len(res_dict[sub_id]) for sub_id in range(len_test)]) >= 3:
                        go_flg = False
                    else:
                        pass
            except AssertionError:
                pass

    return res_dict


def data_load_eval(i, file_list="train"):
    # load
    if file_list == "train":
        data = json.load(open(f"../input/training/{train_file_list[i]}", "r"))
    else:
        data = json.load(open(f"../input/evaluation/{eval_file_list[i]}", "r"))
    # run
    solved_dict = auto_solve(data, time_limit=TIME_LIMIT)
    # eval
    total_ac = 0
    total_wa = 0
    for j in solved_dict.keys():
        assert len(solved_dict[j]) <= 3
        if len(solved_dict[j]) != 3:
            print(i, j, len(solved_dict[j]))
        answer_arr = data["test"][j]["output"]
        answer_str = "|" + "|".join(["".join(map(str, x)) for x in answer_arr]) + "|"
        if answer_str in solved_dict[j]:
            # print(f'AC: {i, j}')
            total_ac += 1
        else:
            # print(f'WA: {i, j}')
            total_wa += 1
    print(f'{file_list}_{i}: {total_ac} / {total_wa + total_ac}')


if __name__ == "__main__":
    for i in range(100):
        data_load_eval(i, "train")
