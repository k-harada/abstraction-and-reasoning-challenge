import os
import sys
import json
import time
from heapq import heappush, heappop

from src.data import Problem
from src.runner import Runner, mappers, transformers, static_solvers, dynamic_solvers, final_solvers
from src.evaluator import eval_distance


TIME_LIMIT = 2.0


def auto_solve(data, time_limit=TIME_LIMIT):
    # flag_show = 0
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
        Runner.pre_solve(p, op)

    heap_queue = []
    heap_res = []
    d = eval_distance(p)
    heappush(heap_queue, (0, 0, 0, p))
    heappush(heap_res, (d, 0, 0, p))

    # mappers and reducers
    for map_op in mappers:
        try:
            q = Runner.run_map(p, map_op)
            # evaluate
            d = eval_distance(q)
            heappush(heap_queue, (1, 0, cnt, q))
            heappush(heap_res, (d, 0, cnt, q))
            cnt += 1
            # print(map_op, reduce_op, d)
        except AssertionError:
            pass

    # main search
    while len(heap_queue) > 0:
        prev_d, v, cnt_old, p = heappop(heap_queue)
        # print("prev_d", prev_d, cnt_old, p)
        # print(p.history)
        p: Problem
        for op in transformers:
            # print(op)
            cnt += 1
            try:
                # print(op, cnt)
                # print(p.__repr__())
                q = Runner.run_transform(p, op)
                # evaluate
                d = eval_distance(q)
                if d > 0:
                    heappush(heap_queue, (v + 1 + d // 10000, v + 1, cnt, q))
                heappush(heap_res, (d, v + 1, cnt, q))
            except AssertionError:
                pass

        for op in dynamic_solvers:
            # print(op)
            cnt += 1
            try:
                q = Runner.run_solve(p, op)
                # evaluate
                d = eval_distance(q)
                if d > 0:
                    heappush(heap_queue, (v + 1 + d // 10000, v + 1, cnt, q))
                heappush(heap_res, (d, v + 1, cnt, q))
            except AssertionError:
                pass

        for op in final_solvers:
            # print(op)
            cnt += 1
            try:
                q = Runner.run_solve(p, op)
                # evaluate
                d = eval_distance(q)
                heappush(heap_res, (d, v + 1, cnt, q))
            except AssertionError:
                pass

        # break by time
        if time.time() >= t0 + time_limit:
            break
    # print(cnt, v)

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
                        # print(r.history)
                        res_dict[sub_id].append(s)
                    elif min([len(res_dict[sub_id]) for sub_id in range(len_test)]) >= 3:
                        go_flg = False
                    else:
                        pass
            except IndexError:
                print(r.history)
            except AssertionError:
                pass

    return res_dict


def data_load_eval(i, file_list="train"):

    train_file_list = list(sorted(os.listdir("../input/training/")))
    eval_file_list = list(sorted(os.listdir("../input/evaluation/")))

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
        print(solved_dict)
        if answer_str in solved_dict[j]:
            # print(f'AC: {i, j}')
            total_ac += 1
        else:
            # print(f'WA: {i, j}')
            total_wa += 1
    print(f'{file_list}_{i}: {total_ac} / {total_wa + total_ac}')


if __name__ == "__main__":
    for i in range(50):
        data_load_eval(i, "train")
