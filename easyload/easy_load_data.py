# @Project  :easyload
# @File     :load_data
# @Date     :2021/4/6 14:21
# @Author   :tonghanshuang
# @Email    :tonghanshuang.thu@gmail.com
# @Software :PyCharm
import json
import pickle

import numpy as np
import pandas as pd


def load_pkl(path):
    return pickle.load(file=open(path, "rb+"))


def load_json(path, mode='normal', key_int=False):
    json_res = []

    if mode == "normal":
        with open(path, 'r', encoding='utf-8') as result_file:
            json_res = json.load(result_file)
    elif mode == "line":
        with open(path) as f:
            for line in f:
                json_res.append(json.loads(line))

    if key_int:
        json_res = {int(k): json_res[k] for k in json_res}
    return json_res


def load_excel(path, sheetname=None):
    try:
        if not sheetname:
            return pd.read_excel(path, index_col=False, header=0)
        else:
            return pd.read_excel(path, index_col=False, header=0, sheetname=sheetname)
    except:
        if not sheetname:
            return pd.read_excel(path, index_col=False, header=0, engine='openpyxl')
        else:
            return pd.read_excel(path, index_col=False, header=0, sheetname=sheetname, engine='openpyxl')


def load_csv(path, head=True, header_list=None, delimiter=None, encoding=None):
    if head:
        try:
            if not delimiter:
                csv_res = pd.read_csv(path, header=True)
            else:
                csv_res = pd.read_csv(path, header=True, delimiter=delimiter)
        except:
            try:
                csv_res = pd.read_csv(path, header=0)
            except:
                try:
                    csv_res = pd.read_csv(path, header=0, encoding='gbk')
                except:
                    csv_res = pd.read_csv(path, header=0, delimiter="\t")
    else:
        try:
            csv_res = pd.read_csv(path, header=None)
        except:
            csv_res = pd.read_csv(path, header=None, delimiter="\t")
    if header_list:
        csv_res.columns = header_list
    return csv_res


def load_npy(path):
    np_res = np.load(path, allow_pickle=True).tolist()
    return np_res


def load_txt(path):
    with open(path, 'r', encoding="utf-8-sig") as json_file:
        data_list = json_file.read().splitlines()
    return data_list


def load_sql(path):
    sql = open(path, 'r', encoding='utf8')
    sqltxt = sql.readlines()
    sql.close()
    sql = "".join(sqltxt)
    return sql
