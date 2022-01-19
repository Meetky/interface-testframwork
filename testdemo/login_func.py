#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project  :interface_test
# @Description: 
# @Time    : 2022-01-02 22:13
# @Author  : Con 
# @Email    :meetky@sina.cn
# @Site    : 
# @File    : login_func.py
# @Software: PyCharm


def login_check(username=None, password=None):
    """
        登录校验
    :param username: 账号
    :param password: 密码
    :return:
    """
    if username != None and password != None:
        if username == "admin" and password == "admin":
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "参数不能为空"}
