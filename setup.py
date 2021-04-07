# @Project  :easyload
# @File     :setup
# @Date     :2021/4/6 14:28
# @Author   :tonghanshuang
# @Email    :tonghanshuang.thu@gmail.com
# @Software :PyCharm

from setuptools import setup

LONGDOC = """
easyload
=====

A Python library for loading multiple types of data

完整文档见 ``README.md``

GitHub: https://github.com/shoe-maker/easyload

特点
====

-  支持不同类型数据的加载与保存：
   -  Support Data Type: json, excel, csv, txt, npy, pkl, sql.

安装说明
========

代码对 Python 3 兼容

-  全自动安装： ``easy_install easyload`` 或者 ``pip install easyload`` / ``pip3 install easyload``
-  半自动安装：先下载 https://pypi.python.org/pypi/easyload/ ，解压后运行
   python setup.py install
-  手动安装：将 easyload 目录放置于当前目录或者 site-packages 目录
-  通过 ``import easyload`` 来引用

"""

setup(
    # 以下为必需参数
    name='easyload',  # 模块名
    version='1.0.4',  # 当前版本
    description='A Python library for loading multiple types of data',  # 简短描述
    py_modules=["my_module"],  # 单文件模块写法
    # ckages=find_packages(exclude=['contrib', 'docs', 'tests']),  # 多文件模块写法

    # 以下均为可选参数
    long_description=LONGDOC,  # 长描述

    url='https://github.com/shoe-maker/easyload',  # 主页链接
    author='ths_lmj',  # 作者名
    author_email='tonghanshuang.thu@gmail.com',  # 作者邮箱
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',  # 当前开发进度等级（测试版，正式版等）
        'Intended Audience :: Developers',  # 模块适用人群
        'Topic :: Software Development :: Build Tools',  # 给模块加话题标签
        'License :: OSI Approved :: MIT License',  # 模块的license
        'Programming Language :: Python :: 3.6',
    ],
    keywords='easy load data',  # 模块的关键词，使用空格分割
    install_requires=['xlwt','numpy','pandas'],  # 依赖模块
    packages=['easyload'],
    package_dir={'easyload': 'easyload'},
    project_urls={  # 项目相关的额外链接
        'Bug Reports': 'https://github.com/shoe-maker/easyload/issues',
        'Source': 'https://github.com/shoe-maker/easyload/',
    },
)
