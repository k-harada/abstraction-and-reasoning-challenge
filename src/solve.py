import json
from heapq import heappush, heappop
from src.data import Problem
from src.operator.runner import Operator, all_operators


CNT_MAX = 10000


def main(data):
    p = Problem()
    cnt = 0
    p.initialize(data)
    heap_queue = []
    heap_res = []
    heappush(heap_queue, (0, 0, p))
    heappush(heap_res, (0, 0, p))

    while len(heap_queue) > 0:
        v, _, p = heappop(heap_queue)
        for op in all_operators:
            cnt += 1
            try:
                q = Operator.run(p, op)
                # evaluate
                heappush(heap_queue, (v + 1, cnt, q))
                heappush(heap_res, (v + 1, cnt, q))
            except ValueError:
                pass
            except IndexError:
                pass
            except TypeError:
                pass
        if cnt >= CNT_MAX:
            break
    print(cnt)
    print(heap_res.pop())


if __name__ == "__main__":
    sample_data = json.load(open("../input/training/007bbfb7.json", "r"))
    main(sample_data)

