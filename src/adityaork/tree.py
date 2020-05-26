from collections import defaultdict
from itertools import product
import numpy as np
from itertools import combinations, permutations
from sklearn.tree import *
from sklearn import tree
from sklearn.ensemble import BaggingClassifier
import random
from math import floor
from src.data import Problem


def get_i_o_r_c(pair):
    inp = pair["input"]
    return pair["input"], pair["output"], len(inp), len(inp[0])


def get_around(i, j, inp, size=1):
    # v = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    r, c = len(inp), len(inp[0])
    v = []
    sc = [0]
    for q in range(size):
        sc.append(q + 1)
        sc.append(-(q + 1))
    for idx, (x, y) in enumerate(product(sc, sc)):
        ii = (i + x)
        jj = (j + y)
        v.append(-1)
        if (0 <= ii < r) and (0 <= jj < c):
            v[idx] = (inp[ii][jj])
    return v


def get_diagonal(i, j, r, c):
    return None


def get_x(inp, i, j, size):
    z = []
    # z.append(i)
    # z.append(j)
    z.extend(get_around(i, j, inp, size))
    return z


def get_xy(inp, oup, size):
    x = []
    y = []
    r, c = len(inp), len(inp[0])
    for i in range(r):
        for j in range(c):
            x.append(get_x(inp, i, j, size))
            y.append(oup[i][j])
    return x, y


def get_bkg_color(task_json):
    color_dict = defaultdict(int)

    for pair in task_json['train']:
        inp, oup, r, c = get_i_o_r_c(pair)
        for i in range(r):
            for j in range(c):
                color_dict[inp[i][j]] += 1
    color = -1
    max_count = 0
    for col, cnt in color_dict.items():
        if cnt > max_count:
            color = col
            max_count = cnt
    return color


def get_num_colors(inp, oup, bl_cols):
    r, c = len(inp), len(inp[0])
    return None


def replace(inp, uni, perm):
    # uni = '234' perm = ['5','7','9']
    # print(uni,perm)
    r_map = {int(c): int(s) for c, s in zip(uni, perm)}
    r, c = len(inp), len(inp[0])
    rp = np.array(inp).tolist()
    # print(rp)
    for i in range(r):
        for j in range(c):
            if rp[i][j] in r_map:
                rp[i][j] = r_map[rp[i][j]]
    return rp


def augment(inp, oup, bl_cols):
    cols = "0123456789"
    npr_map = [1, 9, 72, 3024, 15120, 60480, 181440, 362880, 362880]
    uni = "".join([str(x) for x in np.unique(inp).tolist()])
    for c in bl_cols:
        cols = cols.replace(str(c), "")
        uni = uni.replace(str(c), "")

    exp_size = len(inp) * len(inp[0]) * npr_map[len(uni)]

    mod = floor(exp_size / 120000)
    mod = 1 if mod == 0 else mod

    # print(exp_size,mod,len(uni))
    result = []
    count = 0
    for comb in combinations(cols, len(uni)):
        for perm in permutations(comb):
            count += 1
            if count % mod == 0:
                result.append((replace(inp, uni, perm), replace(oup, uni, perm)))
    return result


def get_flips(inp, oup):
    result = []
    n_inp = np.array(inp)
    n_oup = np.array(oup)
    result.append((np.fliplr(inp).tolist(), np.fliplr(oup).tolist()))
    result.append((np.rot90(np.fliplr(inp), 1).tolist(), np.rot90(np.fliplr(oup), 1).tolist()))
    result.append((np.rot90(np.fliplr(inp), 2).tolist(), np.rot90(np.fliplr(oup), 2).tolist()))
    result.append((np.rot90(np.fliplr(inp), 3).tolist(), np.rot90(np.fliplr(oup), 3).tolist()))
    result.append((np.flipud(inp).tolist(), np.flipud(oup).tolist()))
    result.append((np.rot90(np.flipud(inp), 1).tolist(), np.rot90(np.flipud(oup), 1).tolist()))
    result.append((np.rot90(np.flipud(inp), 2).tolist(), np.rot90(np.flipud(oup), 2).tolist()))
    result.append((np.rot90(np.flipud(inp), 3).tolist(), np.rot90(np.flipud(oup), 3).tolist()))
    result.append((np.fliplr(np.flipud(inp)).tolist(), np.fliplr(np.flipud(oup)).tolist()))
    result.append((np.flipud(np.fliplr(inp)).tolist(), np.flipud(np.fliplr(oup)).tolist()))
    return result


def gettaskxy(task_json, aug, around_size, bl_cols, flip=True):
    X = []
    Y = []
    for i, pair in enumerate(task_json['train']):
        if i == 0:
            continue
        inp, oup = pair["input"], pair["output"]
        tx, ty = get_xy(inp, oup, around_size)
        X.extend(tx)
        Y.extend(ty)
        if flip:
            for ainp, aoup in get_flips(inp, oup):
                tx, ty = get_xy(ainp, aoup, around_size)
                X.extend(tx)
                Y.extend(ty)
                if aug:
                    augs = augment(ainp, aoup, bl_cols)
                    for ainp, aoup in augs:
                        tx, ty = get_xy(ainp, aoup, around_size)
                        X.extend(tx)
                        Y.extend(ty)
        if (aug):
            augs = augment(inp, oup, bl_cols)
            for ainp, aoup in augs:
                tx, ty = get_xy(ainp, aoup, around_size)
                X.extend(tx)
                Y.extend(ty)
    return X, Y


def test_predict(task_json, model, size):
    inp = task_json['test'][0]['input']
    eoup = task_json['test'][0]['output']
    r, c = len(inp), len(inp[0])
    oup = predict(inp, model, size)
    return inp, eoup, oup


def predict(inp, model, size):
    r, c = len(inp), len(inp[0])
    oup = np.zeros([r, c], dtype=int)
    for i in range(r):
        for j in range(c):
            x = get_x(inp, i, j, size)
            o = int(model.predict([x]))
            o = 0 if o < 0 else o
            oup[i][j] = o
    return oup


def submit_predict(task_json, model, size):
    pred_map = {}
    idx = 0
    for pair in task_json['test']:
        inp = pair["input"]
        oup = predict(inp, model, size)
        pred_map[idx] = oup.tolist()
        idx += 1
    return pred_map


def train_predict(task_json, model, size):
    pred_map = {}
    idx = 0
    for pair in task_json['train']:
        inp = pair["input"]
        oup = predict(inp, model, size)
        pred_map[idx] = oup.tolist()
        idx += 1
    return pred_map


def dumb_predict(task_json):
    pred_map = {}
    idx = 0
    for pair in task_json['test']:
        inp = pair["input"]
        pred_map[idx] = [[0, 0], [0, 0]]
        idx += 1
    return pred_map


def get_loss(model, task_json, size):
    total = 0
    for pair in task_json['train']:
        inp, oup = pair["input"], pair["output"]
        eoup = predict(inp, model, size)
        total += np.sum((np.array(oup) != np.array(eoup)))
    return total


def get_test_loss(model, task_json, size):
    total = 0
    for pair in task_json['test']:
        inp, oup = pair["input"], pair["output"]
        eoup = predict(inp, model, size)
        total += np.sum((np.array(oup) != np.array(eoup)))
    return total


def get_a_size(task_json):
    return 4


def get_bl_cols(task_json):
    result = []
    bkg_col = get_bkg_color(task_json);
    result.append(bkg_col)
    # num_input,input_cnt,num_output,output_cnt
    met_map = {}
    for i in range(10):
        met_map[i] = [0, 0, 0, 0]

    total_ex = 0
    for pair in task_json['train']:
        inp, oup = pair["input"], pair["output"]
        u, uc = np.unique(inp, return_counts=True)
        inp_cnt_map = dict(zip(u, uc))
        u, uc = np.unique(oup, return_counts=True)
        oup_cnt_map = dict(zip(u, uc))

        for col, cnt in inp_cnt_map.items():
            met_map[col][0] = met_map[col][0] + 1
            met_map[col][1] = met_map[col][1] + cnt
        for col, cnt in oup_cnt_map.items():
            met_map[col][2] = met_map[col][2] + 1
            met_map[col][3] = met_map[col][3] + cnt
        total_ex += 1

    for col, met in met_map.items():
        num_input, input_cnt, num_output, output_cnt = met
        if num_input == total_ex or num_output == total_ex:
            result.append(col)
        elif num_input == 0 and num_output > 0:
            result.append(col)

    result = np.unique(result).tolist()
    if len(result) == 10:
        result.append(bkg_col)
    return np.unique(result).tolist()


def inp_oup_dim_same(task_json):
    return all([len(pair["input"]) == len(pair["output"]) and len(pair["input"][0]) == len(pair["output"][0]) for
                pair in task_json['train']])


def flattener(pred):
    str_pred = str([row for row in pred])
    str_pred = str_pred.replace(', ', '')
    str_pred = str_pred.replace('[[', '|')
    str_pred = str_pred.replace('][', '|')
    str_pred = str_pred.replace(']]', '|')
    return str_pred


def combine_preds(tid, pm1, pm3, pm5):
    result = []
    for i in range(len(pm1)):
        tk_s = tid+"_"+str(i)
        str_pred = flattener(pm1[i])+" "+flattener(pm3[i])+" "+flattener(pm5[i])
        # print(tk_s,str_pred)
        result.append([tk_s,str_pred])
    return result


def get_problem_from_model(task_json, model, size):
    p = Problem()
    data = dict()
    data["train"] = []
    data["test"] = []
    for pair in task_json['train']:
        inp = pair["input"]
        oup = predict(inp, model, size)
        data["train"].append({"input": oup, "output": pair["output"]})
    for pair in task_json['test']:
        inp = pair["input"]
        oup = predict(inp, model, size)
        data["test"].append({"input": oup})
    p.initialize(data)
    return p


def predict_from_json(task_json):
    if inp_oup_dim_same(task_json):
        a_size = get_a_size(task_json)
        bl_cols = get_bl_cols(task_json)

        isflip = False
        X1, Y1 = gettaskxy(task_json, True, 1, bl_cols, isflip)
        X3, Y3 = gettaskxy(task_json, True, 3, bl_cols, isflip)
        X5, Y5 = gettaskxy(task_json, True, 5, bl_cols, isflip)

        model_1 = BaggingClassifier(base_estimator=DecisionTreeClassifier(min_samples_leaf=2), n_estimators=10).fit(X1, Y1)
        model_3 = BaggingClassifier(base_estimator=DecisionTreeClassifier(min_samples_leaf=2), n_estimators=10).fit(X3, Y3)
        model_5 = BaggingClassifier(base_estimator=DecisionTreeClassifier(min_samples_leaf=2), n_estimators=10).fit(X5, Y5)

        p1 = get_problem_from_model(task_json, model_1, 1)
        p1.history.append("tree_1")
        p3 = get_problem_from_model(task_json, model_3, 3)
        p3.history.append("tree_3")
        p5 = get_problem_from_model(task_json, model_5, 5)
        p5.history.append("tree_5")
        return [p1, p3, p5]
    else:
        return []


def create_json_from_p(p: Problem):
    task_json = dict()
    task_json['train'] = []
    task_json['test'] = []
    for c_x, c_y in zip(p.train_x_list, p.train_y_list):
        task_json['train'].append({
            "input": c_x.repr_values().tolist(),
            "output": c_y.repr_values().tolist()
        })
    for c_x in p.test_x_list:
        task_json['test'].append({
            "input": c_x.repr_values().tolist()
        })
    return task_json


def transform_tree(p: Problem, size=1):

    task_json = create_json_from_p(p)

    assert inp_oup_dim_same(task_json)
    a_size = get_a_size(task_json)
    bl_cols = get_bl_cols(task_json)

    isflip = False

    if size == 1:
        X1, Y1 = gettaskxy(task_json, True, 1, bl_cols, isflip)
        model_1 = BaggingClassifier(base_estimator=DecisionTreeClassifier(min_samples_leaf=2), n_estimators=10).fit(X1, Y1)
        p1 = get_problem_from_model(task_json, model_1, 1)
        p1.history.append("tree_1")
        return p1
    elif size == 3:
        X3, Y3 = gettaskxy(task_json, True, 3, bl_cols, isflip)
        model_3 = BaggingClassifier(base_estimator=DecisionTreeClassifier(min_samples_leaf=2), n_estimators=10).fit(X3, Y3)
        p3 = get_problem_from_model(task_json, model_3, 3)
        p3.history.append("tree_3")
        return p3
    elif size == 5:
        X5, Y5 = gettaskxy(task_json, True, 5, bl_cols, isflip)
        model_5 = BaggingClassifier(base_estimator=DecisionTreeClassifier(min_samples_leaf=2), n_estimators=10).fit(X5, Y5)
        p5 = get_problem_from_model(task_json, model_5, 5)
        p5.history.append("tree_5")
        return p5


if __name__ == "__main__":
    import time
    t0 = time.time()
    pp = Problem.load(35, "eval")
    qq = transform_tree(pp, 3)
    print(qq)
    print(qq.eval_distance())
    rr = transform_tree(qq, 3)
    print(rr)
    print(rr.eval_distance())
    ss = transform_tree(rr, 3)
    print(ss)
    print(ss.eval_distance())
    print(time.time() - t0)
