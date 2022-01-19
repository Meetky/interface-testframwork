# -*- coding: utf-8 -*-
"""
******************************
 @Author   : Con
 @Email    : meetky@sina.cn
 @Project  : interface_test
 @Date     : 2022-01-09 14:10
 @File     : handle_log.py
 @Description: 
 @Software : PyCharm
******************************
"""
import logging
import time


def create_log(
        name="mylogger",
        level="DEBUG",
        fh_level="DEBUG",
        sh_level="DEBUG",
        logpath=f'{time.strftime("%Y%m%d%H%M%S")}.log',
):
    # 1.创建日志收集器
    log = logging.getLogger(name)

    # 2.设置收集器收集日志的等级
    log.setLevel(level)

    # 3.设置日志输出渠道
    # 3.1 输出到文件(年月日时分秒.log)
    fh = logging.FileHandler(logpath, encoding="utf-8")
    fh.setLevel(fh_level)
    log.addHandler(fh)
    # 3.2 输出到控制台
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)

    log.addHandler(sh)

    # 4.设置日志输出的格式
    formats = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
    # 创建格式对象
    log_format = logging.Formatter(formats)
    # 为输出渠道设置输出格式
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)
    # 5.返回日志收集器
    return log


logger = create_log()
#
# if __name__ == '__main__':
#     log = create_log()
#     log.info("111111111 -- info")
#     log.debug("111111111 -- info")
#     log.warning("111111111 -- info")
#     log.error("111111111 -- info")
