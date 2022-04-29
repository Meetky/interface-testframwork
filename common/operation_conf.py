# -*- coding: utf-8 -*-
"""
******************************
 @Author   : Con
 @Email    : meetky@sina.cn
 @Project  : interface_test
 @Date     : 2022-01-12 21:03
 @File     : operation_conf.py
 @Description: 
 @Software : PyCharm
******************************
"""
from configparser import ConfigParser


class Config(ConfigParser):
    def __init__(self, conf_file):
        super().__init__()
        self.read(conf_file, encoding="utf-8")


conf = Config(r"D:\Env_Project\interface-testframwork\conf\conf.ini")

if __name__ == '__main__':
    conf = Config(r"D:\Env_Project\interface-testframwork\conf\conf.ini")
    url = conf.get("env", "test_url")
    print(url)
