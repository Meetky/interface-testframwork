# -*- coding: utf-8 -*-
"""
*****************************
 @Author   :Concon
 @Email    :meetky@sina.cn
 @Project  :interface-testframwork
 @Date     :2022/4/29 11:02
 @File     :operation_db.py
 @Description: 
 @Software :PyCharm
*****************************
"""
import pymysql
from common.operation_conf import conf


def db_decorator(func):
    def wrapper(*args, **kwargs):
        # 获取数据库对象
        self = args[0]
        # 创建游标
        cursor = self.db.cursor()
        try:
            # 执行sql语句
            result = cursor.execute(args[1])
            # 提交到数据库执行
            self.db.commit()
            # 处理数据结果
            if "all" in func.__name__:
                result = cursor.fetchall()
            elif "one" in func.__name__:
                result = cursor.fetchone()
            elif "count" in func.__name__:
                pass
        except Exception as e:
            # 如果发生错误则回滚
            self.db.rollback()
            print("执行失败，已回滚！", e)
            raise
        cursor.close()
        return result

    return wrapper


class OperationDB:
    def __init__(self,
                 host=conf.get("mysql", "host"),
                 port=conf.getint("mysql", "port"),
                 username=conf.get("mysql", "username"),
                 password=conf.get("mysql", "password"),
                 db=conf.get("mysql", "db")
                 ):
        self.db = pymysql.connect(
            host=host, port=port,
            user=username, password=password,
            charset="utf8", cursorclass=pymysql.cursors.DictCursor, db=db
        )

    @db_decorator
    def find_all(self, sql):
        """
        :param sql: sql语句
        :return: 查询到的所有数据
        """
        # cursor = self.db.cursor()
        # try:
        #     # 执行sql语句
        #     cursor.execute(sql)
        #     # 提交到数据库执行
        #     self.db.commit()
        #     result = cursor.fetchall()
        # except Exception as e:
        #     # 如果发生错误则回滚
        #     self.db.rollback()
        #     print("执行失败，已回滚！", e)
        #     raise
        # finally:
        #     cursor.close()
        # return result
        pass

    @db_decorator
    def find_one(self, sql):
        """
        :param sql: sql语句
        :return: 查询到的一条数据
        """
        pass

    @db_decorator
    def find_count(self, sql):
        """
        :param sql: sql语句
        :return: 查询到的数据条数
        """
        pass

    @db_decorator
    def exec_sql(self, sql):
        """
            执行其他语句
        :param sql: sql语句
        :return:
        """
        pass

    def __del__(self):
        self.db.close()


if __name__ == '__main__':
    db = OperationDB()
    # sql = "insert into employees values(207,'KK','L','www@email.com','12345678900','1900-01-01','AC_ACCOUNT',5000,NULL,205,110);"
    # sql = "select * from employees;"
    sql = "create table class_1 (id int primary key auto_increment,name varchar(32) not null,age int not null,sex enum('w','m'),score float default 0.0);"
    # print(db.find_count(sql))
    # db.insert_data(sql)
    db.exec_sql(sql)
