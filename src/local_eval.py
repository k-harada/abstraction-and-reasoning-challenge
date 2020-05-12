import numpy as np

from src.runner.runner import Runner


def run_local(kbn="training", time_limit=0.2, verbose=True):

    total_ac = 0
    total_wa = 0
    res_list = []
    p_list = []
    ind_list = []

    assert kbn == "training" or kbn == "evaluation"

    for ind in range(400):
        if kbn == "training":
            p = Runner(ind, "train", verbose=verbose)
        elif kbn == "evaluation":
            p = Runner(ind, "eval", verbose=verbose)
        else:
            raise ValueError
        p.auto_run(time_limit=time_limit)
        solved_dict = p.output()

        for j in solved_dict.keys():
            p_list.append(ind)
            ind_list.append(j)
            assert len(solved_dict[j]) <= 3
            answer_str = p.answer_list[j]
            if answer_str in solved_dict[j]:
                # print(f'AC: {i, j}')
                total_ac += 1
                res_list.append(1)
            else:
                # print(f'WA: {i, j}')
                total_wa += 1
                res_list.append(0)

    pct = 1 - total_ac / (total_ac + total_wa)
    print(f'{kbn} done, AC: {total_ac}, total: {total_ac + total_wa}, {pct}')
    res_arr = np.concatenate(
        [np.array(res_list).reshape((-1, 1)), np.array(p_list).reshape((-1, 1)), np.array(ind_list).reshape((-1, 1))],
        axis=1)
    np.save(f'../local_eval_log/{kbn}-{time_limit}-{pct}', res_arr)
    return None


if __name__ == "__main__":
    tle = 0.2
    run_local(kbn="training", time_limit=tle, verbose=True)
    run_local(kbn="evaluation", time_limit=tle, verbose=True)
