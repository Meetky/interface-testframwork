# -*- coding: utf-8 -*-
"""
*****************************
 @Author   :Concon
 @Email    :meetky@sina.cn
 @Project  :interface-testframwork
 @Date     :2022/4/15 16:45
 @File     :test_login.py
 @Description: 
 @Software :PyCharm
*****************************
"""
import unittest
import os
from ddt import ddt, data
from common.handle_data import HandleExcel
from common.handle_path import DATA_PATH
from common.handle_conf import conf


@ddt
class TestLogin(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_PATH, "cases.xlsx"), "login")
    cases = excel.read_execl()
    url = conf.get("env", "test_url")

    @data(*cases)
    def test_login(self, case):
        pass
