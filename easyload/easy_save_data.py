# @Project  :adaptive_topic_recommendation
# @File     :load_data_util
# @Date     :2021/1/7 14:37
# @Author   :Hanshuang Tong
# @Email    :tonghanshuang.thu@gmail.com
# @Software :PyCharm
import json
import pickle

import numpy as np

from easyload.built_excel import BuildStyleTable


def save_pkl(path, data):
    pickle.dump(data, open(path, 'wb'))


def save_csv(path, data):
    data.to_csv(path, index=False, header=True, encoding='utf_8_sig')


def save_excel(path, data, format=False):
    if not format:
        data.to_excel(path, index=False, header=True, encoding='utf_8_sig')
    else:
        a_d = {k: list(data[k]) for k in data.columns}
        all_diagnosis_table = BuildStyleTable()
        title_style = all_diagnosis_table.get_title_style()
        mid_style = all_diagnosis_table.get_mid_style()
        style_dict = {"title": title_style}
        for k in a_d:
            style_dict[k] = mid_style
        all_diagnosis_table.build_sheet("Sheet1", a_d, style_dict, [])
        all_diagnosis_table.workbook.save(path)


def save_txt(path, data):
    with open(path, "w") as f:
        for i in data:
            f.writelines(i)
            f.writelines("\n")


def save_json(path, data, visual_only=False):
    if visual_only:
        data = {k: {i: str(data[k][i]) for i in data[k]} for k in data}
    json_str = json.dumps(data, indent=4, ensure_ascii=False)
    with open(path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_str)


def save_npy(path, data):
    np.save(path, data)
