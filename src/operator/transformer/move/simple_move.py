from heapq import heappush, heappop
from src.data import Problem, Case, Matter


class SimpleMoveUntil:

    def __init__(self):
        pass

    @classmethod
    def case(cls, c: Case, direction="down") -> Case:
        h = []
        for m in c.matter_list:
            if direction == "down":
                heappush(h, (m.x0 + m.shape[0], m))
            elif direction == "up":
                heappush(h, (m.x0, m))
            elif direction == "left":
                heappush(h, (m.y0, m))
            elif direction == "right":
                heappush(h, (m.y0 + m.shape[1], m))
            else:
                raise NotImplementedError
        return c
