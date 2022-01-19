# -*- coding: utf-8 -*-
"""
******************************
 @Author   : Con
 @Email    : meetky@sina.cn
 @Project  : interface_test
 @Date     : 2022-01-12 21:03
 @File     : handle_conf.py
 @Description: 
 @Software : PyCharm
******************************
"""
from configparser import ConfigParser


class Config(ConfigParser):
    def __init__(self, conf_file):
        super().__init__()
        self.read(conf_file, encoding="utf-8")


conf = Config(r"D:\py_virtualenvwrapper\Projects\interface_test\conf.ini")

if __name__ == '__main__':
    conf = Config(r"D:\py_virtualenvwrapper\Projects\interface_test\conf.ini")
    name = conf.get("logging", "name")
    print(name)
