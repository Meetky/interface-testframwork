# -*- coding: utf-8 -*-
"""
*****************************
 @Author   :Concon
 @Email    :meetky@sina.cn
 @Project  :interface-testframwork
 @Date     :2022/1/20 11:18
 @File     :test_demo1.py
 @Description: 
 @Software :PyCharm
*****************************
"""

import unittest
from ddt import ddt, data


@ddt
class TestDemo(unittest.TestCase):
    cases01 = [111, 222, 333, 444, 555]
    cases02 = ["aaa", "bbb", "ccc", "ddd", "eee"]

    def setUp(self) -> None:
        print("我是setUp~")

    @data(*cases01)
    def test_case01(self, case):
        print("test_case01：", case)

    @data(*cases02)
    def test_case02(self, case):
        print("test_case02：", case)
