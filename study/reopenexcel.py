#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/07/04 17:33
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : reopenexcel.py
Software: PyCharm
'''
import os
import psutil
import xlrd
from xlutils.copy import copy
import xlwt
def reopen_excel():
    file_name = r"C:\Users\Administrator\Desktop\initial_seq.xls"
    if os.path.exists(file_name):
        print("he")
    workbook=xlrd.open_workbook(file_name,formatting_info=True)
    wbook=copy(workbook)
    wsheet=wbook.get_sheet(0)
    #初始化样式
    style=xlwt.XFStyle()
    #为样式创建字体
    font=xlwt.Font()
    font.name='new'
    font.height=20*10 #字体大小，16为字号，20为衡量单位
    style.font=font
    #写列宽
    wsheet.col(7).width = 3333
    wsheet.write(100,7,'哈哈哈',style)
    if os.path.exists(file_name):
        print("hfdsfe")
    wbook.save(file_name)

# reopen_excel()


# def printPids():
#     pids = psutil.pids()
#     for pid in pids:
#         try:
#             p = psutil.Process(pid)
#             print('pid=%s,pname=%s' % (pid, p.name()))
#             # 关闭excel进程
#             if p.name() == 'EXCEL.EXE':
#                 print(p.children)
#                 # cmd = 'taskkill /F /IM EXCEL.EXE'
#                 # os.system(cmd)
#         except Exception as e:
#             print(e)

if __name__ == '__main__':
    reopen_excel()