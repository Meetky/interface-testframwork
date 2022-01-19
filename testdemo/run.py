#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project  :interface_test
# @Description: 
# @Time    : 2022-01-03 11:19
# @Author  : Con 
# @Email    :meetky@sina.cn
# @Site    : 
# @File    : run.py
# @Software: PyCharm

import unittest
from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover(
    r"D:\py_virtualenvwrapper\Projects\interface_test\testdemo")
#
# runner = unittest.TextTestRunner()
#
# runner.run(suite)
runner = TestRunner(suite, filename="report11.html")
runner.run()
