# -*- coding: utf-8 -*-
"""
*****************************
 @Author   :Concon
 @Email    :meetky@sina.cn
 @Project  :interface_testframwork
 @Date     :2022/1/19 18:17
 @File     :run.py
 @Description: 
 @Software :PyCharm
*****************************
"""
import os
import time
import unittest
from unittestreport import TestRunner
from common.operation_path import CASES_PATH, REPORT_PATH

# 创建测试套件
suite = unittest.defaultTestLoader.discover(CASES_PATH)
# # 执行器
# runner = unittest.TextTestRunner()
# # 执行
# runner.run(suite)

# 创建执行器，并生成报告
runner = TestRunner(suite, filename=os.path.join(REPORT_PATH, time.strftime("%Y%m%d%H%M%S") + ".html"))
# 执行
runner.run()
