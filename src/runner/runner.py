import os
import json
import time
from heapq import heappush, heappop

from src.data import Problem
from src.runner.runner_map import run_map
from src.runner.runner_transform import run_transform
from src.runner.evaluator import eval_distance
from src.runner.runner_solve import pre_solve, run_solve
from src.runner.one_bennchmark import BenchMark
from src.adityaork.tree import predict_from_json


static_solvers = [
    "set_problem_color", "set_is_pattern", "set_is_periodic_row", "set_is_periodic_col",
    "set_is_line_symmetry_row", "set_is_line_symmetry_col",  "set_is_rot_symmetry"
]
mappers = [
    "color", "connect", "connect4", "mesh_split", "mesh_2", "mesh_align", "divide_row_col",
    "multiple_row_col", "color_connect", "color_connect4", "fusion",
    "map_interior", "map_interior_in", "map_interior_pierce"
]
reducers = [
    "auto_fill_row_col_periodicity", "diff_color", "collect_max", "fractal",
    "auto_fill_line_symmetry_del", "auto_fill_line_symmetry_add", "auto_fill_line_symmetry_full",
    "auto_fill_rot", "auto_fill_rot_full"
]
usual_transformers = [
    "interior_dir4_zero", "trim_background", "paste_color", "paste_color_full", "switch_color",
    "n_cell", "n_cell_keep_none", "n_color", "min_max", "mod_2", "arg_sort", "sort_ascending", "sort_descending",
    "freq", "hash_freq",
    "max_color", "keep_max_color", "change_background",
    "fill_rectangle", "connect_row", "connect_col", "connect_row_col", "connect_diagonal", "align",
    "shadow_bool", "shadow_same", "shadow_max", "shadow_min", "shadow_mesh", "shadow_ones", "keep_mesh",
    "find_rectangle", "find_symmetry", "count_hole", "transform_zoom", "transform_duplicate", "drop_duplicates",
    "rectangle_hole_simple", "rectangle_hole_mesh", "rectangle_hole_mesh_x", "keep_rectangle", "keep_max"
]
transformers = reducers + usual_transformers

dynamic_solvers = [
    "duplicate", "divide", "extend_shape", "point_cross", "solve_zoom"
]
final_solvers = [
    "reduce_bitwise", "color_pile",
    "rotations", "fill_pattern", "auto_paste", "auto_paste_full", "auto_add_color", "color_change",
    "auto_paste_a", "fit_replace_rule_33_all", "auto_pick"
]
special_solvers = ["fit_replace_rule_33"]
solvers = dynamic_solvers + final_solvers + special_solvers

train_file_list = list(sorted(os.listdir(os.path.join(os.path.dirname(__file__), "../../input/training/"))))
eval_file_list = list(sorted(os.listdir(os.path.join(os.path.dirname(__file__), "../../input/evaluation/"))))


class Runner:

    def __init__(self, i=None, file_list="train", verbose=False):
        self.original_problem = None
        self.problem_hand = None
        self.verbose = verbose
        self.name = ""
        self.task_json = None
        self.json_name = ""
        # answer
        self.answer_list = []
        # elapsed time
        self.time_record = dict()
        if self.verbose:
            for op in mappers:
                self.time_record[op] = 0.0
            for op in transformers:
                self.time_record[op] = 0.0
            for op in static_solvers:
                self.time_record[op] = 0.0
            for op in dynamic_solvers:
                self.time_record[op] = 0.0
            for op in final_solvers:
                self.time_record[op] = 0.0
        # keep record
        self.heap_queue = []
        self.heap_res = []
        self.cnt = 1
        if i is not None:
            self.name = f'{file_list}_{i}'
            self.load_file(i, file_list)

    def initialize_from_data(self, data):
        p = Problem()
        p.initialize(data)
        self.original_problem = p
        self.problem_hand = p
        return None

    def load_file(self, i, file_list):
        """load and initialize(pre solve) problem"""
        p = Problem()
        if file_list == "train":
            with open(os.path.join(os.path.dirname(__file__), f"../../input/training/{train_file_list[i]}"), "r") as f:
                data = json.load(f)
                self.task_json = data
                self.json_name = train_file_list[i][:-5]
                if self.verbose:
                    print("train", i)
                p.initialize(data)
                for j in range(len(data["test"])):
                    answer_arr = data["test"][j]["output"]
                    answer_str = "|" + "|".join(["".join(map(str, x)) for x in answer_arr]) + "|"
                    self.answer_list.append(answer_str)
        else:
            with open(os.path.join(os.path.dirname(__file__), f"../../input/evaluation/{eval_file_list[i]}"), "r") as f:
                data = json.load(f)
                self.task_json = data
                self.json_name = eval_file_list[i][:-5]
                if self.verbose:
                    print("eval", i)
                p.initialize(data)
                for j in range(len(data["test"])):
                    answer_arr = data["test"][j]["output"]
                    answer_str = "|" + "|".join(["".join(map(str, x)) for x in answer_arr]) + "|"
                    self.answer_list.append(answer_str)

        self.original_problem = p
        self.problem_hand = p

        # static solvers
        for op in static_solvers:
            self.pre_solve(op)

        return None

    def run(self, command: str) -> None:
        if command in mappers:
            self.run_map(command)
        elif command in transformers:
            self.run_transform(command)
        elif command in solvers:
            self.run_solve(command)
        else:
            raise NotImplementedError

    def auto_run(self, time_limit=0.2) -> None:

        t0 = time.time()
        t1 = 0
        v_max = 0

        # initial
        if len(self.heap_queue) == 0:

            p = self.original_problem.copy()

            # static solvers
            for op in static_solvers:
                self._pre_solve(p, op)
            d = eval_distance(p)
            heappush(self.heap_queue, (0, d, 0, p))
            heappush(self.heap_res, (d, 0, 0, p))

            # all ones benchmark
            for q in BenchMark.problem(p):
                d = eval_distance(q)
                heappush(self.heap_res, (d, 0, self.cnt, q))
                self.cnt += 1

            # mappers and reducers
            for op in mappers:
                if self.verbose:
                    t1 = time.time()
                try:
                    q = self._run_map(p, op)
                    # evaluate
                    d = eval_distance(q)
                    heappush(self.heap_queue, (1, d, self.cnt, q))
                    heappush(self.heap_res, (d, 0, self.cnt, q))
                    self.cnt += 1
                except AssertionError:
                    pass
                if self.verbose:
                    self.time_record[op] += time.time() - t1

        # main search
        while len(self.heap_queue) > 0:
            v, d_old, cnt_old, p = heappop(self.heap_queue)
            v_max = max(v_max, v + 1)
            # print(p.history)
            p: Problem
            for op in transformers:
                if self.verbose:
                    t1 = time.time()
                # print(op)
                self.cnt += 1
                try:
                    # print(op, cnt)
                    # print(p.__repr__())
                    q = self._run_transform(p, op)
                    # evaluate
                    d = eval_distance(q)
                    if d > 0:
                        heappush(self.heap_queue, (v + 1, d, self.cnt, q))
                    heappush(self.heap_res, (d, v + 1, self.cnt, q))
                except AssertionError:
                    pass
                if self.verbose:
                    self.time_record[op] += time.time() - t1

            for op in dynamic_solvers:
                if self.verbose:
                    t1 = time.time()
                # print(op)
                self.cnt += 1
                try:
                    q = self._run_solve(p, op)
                    # evaluate
                    d = eval_distance(q)
                    if d > 0:
                        heappush(self.heap_queue, (v + 1, d, self.cnt, q))
                    heappush(self.heap_res, (d, v + 1, self.cnt, q))
                except AssertionError:
                    pass
                if self.verbose:
                    self.time_record[op] += time.time() - t1

            for op in final_solvers:
                if self.verbose:
                    t1 = time.time()
                # print(op)
                self.cnt += 1
                try:
                    q = self._run_solve(p, op)
                    # evaluate
                    d = eval_distance(q)
                    heappush(self.heap_res, (d, v + 1, self.cnt, q))
                except AssertionError:
                    pass
                if self.verbose:
                    self.time_record[op] += time.time() - t1

            # break if solved
            d, v, c, r = heappop(self.heap_res)
            heappush(self.heap_res, (d, v, c, r))
            if d == 0:
                if self.verbose:
                    print(f'Solved {self.name} in {round(time.time() - t0, 3)} seconds, v={v_max}, cnt={self.cnt}')
                    print(r.history)
                    break
            # break by time
            if time.time() >= t0 + time_limit:
                if self.verbose:
                    print(f'Failed to solve {self.name} in {round(time.time() - t0, 3)} seconds, v={v_max}, cnt={self.cnt}')
                    # print(self.time_record)
                break

        return None

    def output(self):
        # output
        # for return
        len_test = len(self.original_problem.test_x_list)
        res_dict = dict()
        for sub_id in range(len_test):
            res_dict[sub_id] = []
        go_flg = True

        while len(self.heap_res) > 0 and go_flg:
            _, _, _, r = heappop(self.heap_res)
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

    def run_map(self, command: str) -> None:
        self.problem_hand = self._run_map(self.problem_hand, command)
        if self.verbose:
            self._print_distance()
        return None

    def run_transform(self, command: str) -> None:
        self.problem_hand = self._run_transform(self.problem_hand, command)
        if self.verbose:
            self._print_distance()
        return None

    def pre_solve(self, command: str) -> None:
        self._pre_solve(self.problem_hand, command)
        return None

    def run_solve(self, command: str) -> None:
        self.problem_hand = self._run_solve(self.problem_hand, command)
        if self.verbose:
            self._print_distance()
        return None

    def _print_distance(self):
        print(self.eval_distance())

    def eval_distance(self):
        return eval_distance(self.problem_hand)

    def eval_test(self, verbose=False):
        ac = 0
        wa = 0
        for c_x, ans in zip(self.problem_hand.test_x_list, self.answer_list):
            if c_x.__repr__() == ans:
                ac += 1
            else:
                wa += 1
                if verbose:
                    print(self.name, c_x.__repr__(), ans)
        return ac, wa

    @classmethod
    def _run_map(cls, problem: Problem, command: str) -> Problem:
        new_problem = run_map(problem, command)
        new_problem.history.append(command)
        return new_problem

    @classmethod
    def _run_transform(cls, problem: Problem, command: str) -> Problem:
        new_problem = run_transform(problem, command)
        new_problem.history.append(command)
        return new_problem

    @classmethod
    def _pre_solve(cls, problem: Problem, command: str) -> None:
        pre_solve(problem, command)
        return None

    @classmethod
    def _run_solve(cls, problem: Problem, command: str) -> Problem:
        new_problem = run_solve(problem, command)
        new_problem.history.append(command)
        return new_problem


if __name__ == "__main__":
    for ind in range(100):
        p_test = Runner(ind, file_list="train", verbose=True)
        p_test.auto_run(time_limit=1.0)
