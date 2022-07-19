#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/04/13 23:49
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : demo9.py
Software: PyCharm
'''
import re
# import sqlite3
#
# # '''创建一个数据库，文件名'''
# # 如果给定的数据库名称 filename 不存在，则该调用将创建一个数据库
# conn = sqlite3.connect("./db/tableTrace2022.db")
# # '''创建游标'''
# cursor = conn.cursor()
#
# cursor.execute('''SELECT * FROM module_detail where port_name ='clk_1' and instance_name = 'Us'  ''')
# rest = cursor.fetchone()
#
# print(rest)
# for item in rest:
#     directory_name, module_path = item[0], item[1]
#     print(directory_name,module_path)
test = ['U_SON1_1(SON1)', 'U_SON1_2(SON1)', 'U_SON2_1(SON2)', 'U_SON3_1(SON3)']
unit={'U_SON1_1(SON1)': 'U_SON1_1', 'U_SON1_2(SON1)': 'U_SON1_2', 'U_SON2_1(SON2)': 'U_SON2_1', 'U_SON3_1(SON3)': 'U_SON3_1'}
rest=[unit[i] for i in test]
# print(rest)
gg='(%s)'% ((',').join(rest))
print(test[-1])