import os
import json
import pandas as pd

from src.runner.runner import Runner


def main(dir_path, time_limit):

    output_id_list = []
    output_list = []

    for i, file_name in enumerate(list(sorted(os.listdir(dir_path)))):

        if file_name[-5:] == ".json":
            p = Runner()
            with open(dir_path + file_name, "r") as file:
                data = json.load(file)
            p.initialize_from_data(data)

            try:
                p.auto_run(time_limit=time_limit)
                solved_dict = p.output()
                for j in solved_dict.keys():
                    assert len(solved_dict[j]) <= 3

                    output_id_list.append(f'{file_name[:-5]}_{j}')
                    output_list.append(" ".join(solved_dict[j]))
            except:
                for j in range(len(data["test"])):
                    output_id_list.append(f'{file_name[:-5]}_{j}')
                    output_list.append("")

    res_df = pd.DataFrame({"output_id": output_id_list, "output": output_list})
    # print(res_df)
    res_df.to_csv("submission.csv", index=False)


if __name__ == "__main__":
    main(dir_path="../input/test/", time_limit=0.1)
