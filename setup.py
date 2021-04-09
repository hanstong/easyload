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

For complete documentation, see ``README.md``

GitHub: https://github.com/shoe-maker/easyload

Main Features
====
-  A Python library for loading multiple types of data：
   -  Support Data Type: json, excel, csv, txt, npy, pkl, sql.

Installation
========
The code is Python 3 compatible

-  Fully automatic installation: ``easy_install easyload`` or ``pip install easyload`` / ``pip3 install easyload``
-  Semi-automatic installation: download https://pypi.python.org/pypi/easyload/ , unzip and run python setup.py install
-  Manual installation: Place easyload directory in the current directory or site-packages directory
-  use ``import easyload`` to import
"""
# python setup.py sdist
# twine upload dist/*

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # 以下为必需参数
    name='easyload',  # 模块名
    version='1.0.6',  # 当前版本
    description='A Python library for loading multiple types of data',  # 简短描述
    py_modules=["my_module"],  # 单文件模块写法
    # ckages=find_packages(exclude=['contrib', 'docs', 'tests']),  # 多文件模块写法

    # 以下均为可选参数
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/shoe-maker/easyload',  # 主页链接
    author='Hanshuang Tong',  # 作者名
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
