# -*- coding: utf-8 -*-
"""
******************************
 @Author   : Con
 @Email    : meetky@sina.cn
 @Project  : interface_testframwork
 @Date     : 2022-01-19 22:07
 @File     : handle_path.py
 @Description: 
 @Software : PyCharm
******************************
"""
import os

"""项目目录"""
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""配置目录"""
CONF_PATH = os.path.join(BASE_PATH, "conf")
"""数据目录"""
DATA_PATH = os.path.join(BASE_PATH, "datas")
"""日志目录"""
LOG_PATH = os.path.join(BASE_PATH, "logs")
"""报告目录"""
REPORT_PATH = os.path.join(BASE_PATH, "reports")
"""用例目录"""
CASES_PATH = os.path.join(BASE_PATH, "testcases")
