#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/05/12 19:05
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : pp.py
Software: PyCharm
'''
import xlsxwriter

workbook = xlsxwriter.Workbook('product.xlsx')  # 创建一个excel文件
worksheet = workbook.add_worksheet(u'sheet1')  # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1
# 使用readline()读文件
f = open("product.txt", 'r')
i = 0
while True:
    line = f.readline()
    if line:
        prams = line.split("#")
        for j in range(6):
            worksheet.write(i, j, prams[j])
        i += 1
    else:
        break
f.close()
workbook.close()
