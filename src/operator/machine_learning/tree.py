import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from src.data import Problem, Case, Matter


def tree_x(x_arr: np.array, ext: int = -1):

    # expand_x
    x_arr_ex = ext * np.ones((x_arr.shape[0] + 4, x_arr.shape[1] + 4), dtype=int)
    x_arr_ex[2:-2, 2:-2] = x_arr

    # features
    # 13 points around
    feature_arr = np.zeros((x_arr.shape[0] * x_arr.shape[1], 13), dtype=int)
    feature_arr[:, 0] = x_arr_ex[:-4, 2:-2].reshape(-1, )
    feature_arr[:, 1] = x_arr_ex[1:-3, 1:-3].reshape(-1, )
    feature_arr[:, 2] = x_arr_ex[1:-3, 2:-2].reshape(-1, )
    feature_arr[:, 3] = x_arr_ex[1:-3, 3:-1].reshape(-1, )
    feature_arr[:, 4] = x_arr_ex[2:-2, :-4].reshape(-1, )
    feature_arr[:, 5] = x_arr_ex[2:-2, 1:-3].reshape(-1, )
    feature_arr[:, 6] = x_arr_ex[2:-2, 2:-2].reshape(-1, )
    feature_arr[:, 7] = x_arr_ex[2:-2, 3:-1].reshape(-1, )
    feature_arr[:, 8] = x_arr_ex[2:-2, 4:].reshape(-1, )
    feature_arr[:, 9] = x_arr_ex[3:-1, 1:-3].reshape(-1, )
    feature_arr[:, 10] = x_arr_ex[3:-1, 2:-2].reshape(-1, )
    feature_arr[:, 11] = x_arr_ex[3:-1, 3:-1].reshape(-1, )
    feature_arr[:, 12] = x_arr_ex[4:, 2:-2].reshape(-1, )

    return feature_arr


class DecisionTreeDirect:

    def __init__(self):
        pass

    @classmethod
    def build_tree_from_problem(cls, p: Problem) -> None:
        c_x: Case
        c_y: Case
        feature_arr_list = []
        target_list = []
        for c_x, c_y in zip(p.train_x_list, p.train_y_list):
            assert c_x.shape == c_y.shape
            feature_arr = tree_x(c_x.repr_values())
            feature_arr_list.append(feature_arr)
            target_list.append(c_y.repr_values().reshape(-1, ))
        feature_arr_all = np.concatenate(feature_arr_list, axis=0)
        target_all = np.concatenate(target_list, axis=0)
        cls.model = BaggingClassifier(DecisionTreeClassifier(), n_estimators=100)
        cls.model.fit(feature_arr_all, target_all)
        return None

    @classmethod
    def array(cls, x_arr: np.array, background: int):
        predict_class = cls.model.predict(tree_x(x_arr))
        predict_prob_1 = cls.model.predict_proba(tree_x(x_arr, ext=-1))
        predict_prob_2 = cls.model.predict_proba(tree_x(x_arr, ext=10))
        predict_prob = np.minimum(predict_prob_1, predict_prob_2)
        predict_class[predict_prob.max(axis=1) < 1] = x_arr.reshape((-1, ))[predict_prob.max(axis=1) < 1]
        return predict_class.reshape(x_arr.shape)

    @classmethod
    def case(cls, c: Case) -> Case:
        new_values = cls.array(c.repr_values(), c.background_color)
        new_case: Case = c.copy()
        new_case.matter_list = [Matter(new_values, background_color=c.background_color, new=True)]
        return new_case

    @classmethod
    def problem_one(cls, p: Problem) -> Problem:
        cls.build_tree_from_problem(p)
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        t = 1
        q = cls.problem_one(p)
        while t < 100:
            q = cls.problem_one(p)
            if p.__repr__() == q.__repr__():
                break
            t += 1
        return q


if __name__ == "__main__":
    pp = Problem.load(177, "eval")
    print(pp)
    qq = DecisionTreeDirect.problem(pp)
    print(qq)
    rr = DecisionTreeDirect.problem(qq)
    print(rr)
    pp = Problem.load(179, "eval")
    qq = DecisionTreeDirect.problem(pp)
    print(qq)
    pp = Problem.load(185, "eval")
    qq = DecisionTreeDirect.problem(pp)
    print(qq)
    pp = Problem.load(192, "eval")
    qq = DecisionTreeDirect.problem(pp)
    print(qq)
