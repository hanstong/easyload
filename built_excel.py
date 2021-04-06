# @Project  :adaptive_topic_recommendation
# @File     :built_excel
# @Date     :2021/1/7 14:37
# @Author   :Hanshuang Tong
# @Email    :tonghanshuang.thu@gmail.com
# @Software :PyCharm
import xlwt
import numpy as np

class BuildStyleTable():
    def __init__(self):
        # 创建一个workbook 设置编码
        self.workbook = xlwt.Workbook(encoding='utf-8')

    def get_title_style(self):
        # 设置背景颜色
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = xlwt.Style.colour_map['ice_blue']  # 背景颜色

        style = xlwt.XFStyle()  # 创建一个样式对象，初始化样式
        al = xlwt.Alignment()
        al.horz = 0x02  # 设置水平居中
        al.vert = 0x01  # 设置垂直居中
        style.alignment = al
        style.pattern = pattern
        font = xlwt.Font()
        font.name = 'SimSun'
        style.font = font
        return style

    def get_mid_style(self):
        style = xlwt.XFStyle()  # 创建一个样式对象，初始化样式
        al = xlwt.Alignment()
        al.horz = 0x02  # 设置水平居中
        al.vert = 0x01  # 设置垂直居中
        style.alignment = al
        return style

    def get_auto_change_line_style(self):
        style = xlwt.XFStyle()  # 初始bai化样式
        font = xlwt.Font()  # 为样式创du建字体
        style.font = font  # 设定样式
        style.alignment.wrap = 1  # 自动zhi换dao行

        return style

    # 获取字符串长度，一个中文的长度为2
    def len_byte(self,value):
        length = len(value)
        utf8_length = len(value.encode('utf-8'))
        length = (utf8_length - length) / 2 + length
        return int(length)

    def build_sheet(self, sheet_name, title_content_dict, style_dict, merge_list, column_dict=None):
        if style_dict==None:
            style_dict = {k: self.get_mid_style() for k in title_content_dict}
            style_dict["title"] = self.get_title_style()

        # 设置全局字体与边框
        font = xlwt.Font()
        font.name = 'SimSun'
        borders = xlwt.Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        borders.left_colour = 0
        borders.right_colour = 0
        borders.bottom_colour = 0
        borders.top_colour = 0
        for t in style_dict:
            style_dict[t].borders = borders
            style_dict[t].font = font

        title_list = list(title_content_dict.keys())

        # 创建一个worksheet
        worksheet = self.workbook.add_sheet(sheet_name, cell_overwrite_ok=True)

        # 写入title
        for i, t in enumerate(title_list):
            worksheet.write(0, i, label=title_list[i], style=style_dict["title"])

        for i, title in enumerate(title_list):
            # try:
            if title in merge_list:
                if len(title_content_dict[title])==0:
                    continue
                pre = title_content_dict[title][0]
                cur_loc = 1
                title_content_dict[title].append("空")
                for j, t in enumerate(title_content_dict[title]):
                    if t != pre or j == len(title_content_dict[title]) - 1:
                        worksheet.write_merge(cur_loc , j , i, i, pre, style_dict[title])
                        cur_loc = j + 1
                        pre = t
            else:
                for j, obj in enumerate(title_content_dict[title]):
                    worksheet.write(j + 1, i, label=title_content_dict[title][j], style=style_dict[title])
            # except:
            #     continue

        # 确定栏位宽度
        try:
            col_width = [np.array([self.len_byte(str(t)) for t in (title_content_dict[title]+[title])]).max() for title in title_list]

            # 设置栏位宽度，栏位宽度小于10时候采用默认宽度
            for i in range(len(col_width)):
                if column_dict and title_list[i] in column_dict:
                    worksheet.col(i).width = 256 * column_dict[title_list[i]]
                else:
                    if col_width[i] > 10 and col_width[i]<85:
                        worksheet.col(i).width = int(256 * (col_width[i] + 1))
                    elif col_width[i]>85:
                        worksheet.col(i).width = 256 * (120 + 1)
        except:
            pass
        # # 保存
        # workbook.save(path)

