# -*- coding: utf-8 -*-
"""
*****************************
 @Author   :Concon
 @Email    :meetky@sina.cn
 @Project  :interface-testframwork
 @Date     :2022/4/27 14:58
 @File     :utils.py
 @Description: 
 @Software :PyCharm
*****************************
"""
import os
import ddddocr
from common.operation_path import DATA_PATH


class Utils:
    def __init__(self):
        pass

    def code_ocr(self, img_bytes):
        ocr = ddddocr.DdddOcr()
        # with open(os.path.join(DATA_PATH, img), "rb") as f:
        #     img_bytes = f.read()
        return ocr.classification(img_bytes)


if __name__ == '__main__':
    import pymysql

    conn = pymysql.connect(
        host="127.0.0.1", port=3306, user="root", password="123456", charset="utf8"
    )
    cur = conn.cursor()
    sql = "use atguigudb;select * from employees;"
    cur.execute(sql)
    print(cur.fetchall())
