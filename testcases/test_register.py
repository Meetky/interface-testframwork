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
from jsonpath import jsonpath
from common.operation_data import OperationExcel
from common.operation_path import DATA_PATH
from common.operation_conf import conf
from common.utils import Utils
from common.operation_log import logger


@ddt
class TestRegister(unittest.TestCase):
    excel = OperationExcel(os.path.join(DATA_PATH, "test.xlsx"), "addUser")
    login_excel = OperationExcel(os.path.join(DATA_PATH, "test.xlsx"), "admin")
    cases = excel.read_execl()
    url = conf.get("env", "test_url")
    login_info = login_excel.read_execl()
    utils = Utils()

    # 登录获取token
    @classmethod
    def setUpClass(cls) -> None:
        img_url = cls.url + cls.login_info[0]["path"]
        img_method = cls.login_info[0]["method"].lower()
        login_url = cls.url + cls.login_info[1]["path"]
        login_method = cls.login_info[1]["method"].lower()
        login_data = eval(cls.login_info[1]["params"])
        # 获取参数
        img_data = requests.request(img_method, img_url)
        code = cls.utils.code_ocr(img_data.content)
        headers = {
            "content-type": "application/json;charset=UTF-8",
            "access-code": img_data.headers["Access-code"]
        }
        login_data.update({"code": code})
        # 登录
        res = requests.request(login_method, login_url, json=login_data, headers=headers)
        cls.token = "bearer " + jsonpath(res.json(), "$.data")[0]

    @data(*cases)
    def test_register(self, case):
        # 准备参数
        url = self.url + case["path"]
        method = case["method"].lower()
        data = eval(case["params"])

        expected = eval(case["expected"])  # 预期结果
        headers = {
            "content-type": "application/json;charset=UTF-8",
            "authorization": self.token,
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
