import os
from src.runner.runner import Runner


def test_log():
    with open(os.path.join(os.path.dirname(__file__), "log.txt")) as f:
        flag = False
        for row in f:
            if row[:5] == "train":
                file_kbn = list(row.split())
            elif row[:4] == "eval":
                file_kbn = list(row.split())
            elif row[:6] == "Failed":
                flag = False
            elif row[:6] == "Solved":
                flag = True
            # print(row, file_kbn)
            if flag and row[0] == "[":
                op_list = eval(row.strip())
                p = Runner(int(file_kbn[1]), file_kbn[0], verbose=True)
                for op in op_list:
                    p.run(op)
                ac, wa = p.eval_test(verbose=True)
                if wa == 0 and file_kbn[0] == "eval":
                    # print(file_kbn[1], op_list)
                    pass
                if wa > 0:
                    print(op_list)
                    print(ac, wa)
                assert p.eval_distance() == 0


if __name__ == "__main__":
    test_log()
