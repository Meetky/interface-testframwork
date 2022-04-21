# -*- coding: utf-8 -*-
"""
*****************************
 @Author   :Concon
 @Email    :meetky@sina.cn
 @Project  :interface-testframwork
 @Date     :2022/4/15 16:45
 @File     :test_register.py
 @Description: 
 @Software :PyCharm
*****************************
"""
import unittest
import os

import requests
from ddt import ddt, data
from common.handle_data import HandleExcel
from common.handle_path import DATA_PATH
from common.handle_conf import conf
from common.handle_log import logger


@ddt
class TestRegister(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_PATH, "test.xlsx"), "addUser")
    cases = excel.read_execl()
    url = conf.get("env", "test_url")

    @data(*cases)
    def test_register(self, case):
        # 准备参数
        url = self.url + case["path"]
        method = case["method"].lower()
        data = eval(case["params"])

        expected = eval(case["expected"])  # 预期结果
        headers = {
            "content-type": "application/json;charset=UTF-8",
            "authorization": "bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7InVzZXJJZCI6MzAsInVzZXJOYW1lIjoi6Jyh56yU5bCP6ZSIIiwidXNlckxvZ2luIjoiMTg2MTM4NzI4OTgiLCJwYXNzd29yZCI6IjMyNWJmY2MxZWEyODVlOGZmNDE3MGEyMTk3M2VkMjIxIiwiaGVhZEltZ2VVcmwiOiJodHRwczovL3Rlc3QtcHJpdmF0ZS5yYXlkYXRhLnByby9yYXlkYXRhL3VwbG9hZC8yMDIyMDMyMS9pbWFnZS9kZTVkZmI4ZWVhZWI0ZjkzYjUxYmFlZjI5OGM5MzQxNy5wbmciLCJwaG9uZSI6IiIsImVtYWlsIjoiIiwic2V4IjotMSwidXNlclNvdXJjZSI6MSwicmVtYXJrIjoiIiwic3RhdHVzIjoxMDAwMSwiY3JlYXRlQnkiOjAsImNyZWF0ZVRpbWUiOjE2NDczMjg4Njg4MTksInVwZGF0ZUJ5IjowLCJ1cGRhdGVUaW1lIjoxNjUwMDEwODUyMDAwLCJncm91cHMiOm51bGwsInJhbmdlRmxhZyI6bnVsbCwicm9sZUlkcyI6bnVsbCwicm9sZUxpc3QiOm51bGwsInVzZXJJZGVudGl0eSI6bnVsbCwiaXNGb2xkZXJDcmVhdGVyIjoxLCJwZXJBcnJheSI6bnVsbCwiZ3JvdXBJZCI6bnVsbCwiYWNjb3VudFN0YXRlIjpudWxsLCJleGlzdFVzZXIiOnRydWV9LCJzdWIiOiIzMCIsImlhdCI6MTY1MDUyMTI4MCwiZXhwIjoxNjUwNTU3MjgwfQ.6wnLQZHmx7Z5Y3PlELlGwnhbuvKGQ82e7NlsD3okWH4swdEfrIgLMnCmKkXvrVansRTlhm6SCnuMgRyOCRcHxA",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }

        # 发起请求
        logger.info("==============接口测试开始==============")
        logger.info(f"请求地址：{url}")
        logger.info(f"请求方式：{method}")
        logger.info(f"请求参数：{data}")
        logger.info(f"预期结果：{expected}")
        result = requests.request(method, url, json=data, headers=headers).json()
        logger.info(f"实际结果：{result}")
        # 验证
        try:
            self.assertEqual(expected["code"], result["code"])
            self.assertEqual(expected["msg"], result["msg"])
        except AssertionError as e:
            logger.error(f"用例-【{case['title']}】--执行失败")
            raise e
        else:
            logger.info(f"用例-【{case['title']}】--执行通过")
        finally:
            logger.info("==============接口测试结束==============")
