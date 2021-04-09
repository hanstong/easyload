# @Project  :easyload
# @File     :ttt
# @Date     :2021/4/6 16:37
# @Author   :tonghanshuang
# @Email    :tonghanshuang.thu@gmail.com
# @Software :PyCharm
import easyload

json_path = "../test_input.json"
csv_path = "../test_input.json"
print(easyload.load(json_path))

path = ""
print(easyload.load_json(path))
