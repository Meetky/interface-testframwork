#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project  :interface_test
# @Description: 
# @Time    : 2022-01-02 22:18
# @Author  : Con 
# @Email    :meetky@sina.cn
# @Site    : 
# @File    : test_login_case.py
# @Software: PyCharm
import unittest
from ddt import ddt, data

from common.handle_execl import HandleExecl
from testdemo.login_func import login_check

# from unittestreport import ddt, list_data


execl = HandleExecl(r"C:\Users\Concon\Documents\test1.xlsx", "test")

cases = execl.read_execl()


@ddt
class TestLogin(unittest.TestCase):
    @data(*cases)
    def test_login(self, item):
        """登录成功"""
        params = eval(item["params"])
        res = login_check(**params)
        print("res:", res)

        expected = eval(item["expected"])
        print("expected:", expected)

        assert res == expected

#
# class TestRegister(unittest.TestCase):
#     def test_register_pass(self):
#         """注册成功"""
#         assert "OK" == "OK"
#
#     def test_register_fail(self):
#         """注册失败"""
#         assert "OK" == "111"
