easyload
========
Loading and Saving data made easy！

Main Features
====
-  A Python library for loading multiple types of data：
   -  Support Data Type: json, excel, csv, txt, npy, pkl, sql.

Installation
========
The code is Python 3 compatible

-  Fully automatic installation: ``easy_install easyload`` or ``pip install easyload`` / ``pip3 install easyload``
-  Semi-automatic installation: download https://pypi.python.org/pypi/easyload/ , unzip and run python setup.py install
-  Manual installation: place easyload directory in the current directory or site-packages directory
-  use ``import easyload`` to import


Quick start
========
```python
# encoding=utf-8
import easyload
load_file_path, save_file_path = "", ""
json_data = easyload.load_json(load_file_path)
easyload.save_json(save_file_path,json_data)
```