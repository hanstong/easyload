# @Project  :easyload
# @File     :__init__
# @Date     :2021/4/6 18:03
# @Author   :tonghanshuang
# @Email    :tonghanshuang.thu@gmail.com
# @Software :PyCharm
from easyload import easy_load_data, easy_save_data

# all
load = easy_load_data.load

# json
load_json = easy_load_data.load_json
save_json = easy_save_data.save_json

# excel
load_excel = easy_load_data.load_excel
save_excel = easy_save_data.save_excel

# csv
load_csv = easy_load_data.load_csv
save_csv = easy_save_data.save_csv

# txt
load_txt = easy_load_data.load_txt
save_txt = easy_save_data.save_txt

# npy
load_npy = easy_load_data.load_npy
save_npy = easy_save_data.save_npy

# pkl
load_pkl = easy_load_data.load_pkl
save_pkl = easy_save_data.save_pkl

# sql
load_sql = easy_load_data.load_sql
