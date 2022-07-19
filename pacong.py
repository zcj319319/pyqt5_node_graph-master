#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/05/11 19:46
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : pacong.py
Software: PyCharm
'''
import re

import requests
from bs4 import BeautifulSoup
import xlsxwriter


def parse_html():
    max_list = []
    workbook = xlsxwriter.Workbook('demo1.xlsx')  # 创建一个excel文件
    worksheet = workbook.add_worksheet(u'sheet1')  # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1
    url_0 = "https://www.tansoole.com/search/search.htm?gloabSearchVo.queryString=merck&gloabSearchVo.type=1" \
            "&gloabSearchVo.listType=1&gloabSearchVo.rootId=&gloabSearchVo.segamentId=&gloabSearchVo.branchId" \
            "=&gloabSearchVo.brand=&gloabSearchVo.sortField=cn_len&gloabSearchVo.asc=true&l=&tf=&pro=&proTitle=&type" \
            "=1&type=1&type=1&type=1&type=1&type=1&specialSearch=&Pagelist=1&page.currentPageNo=1&page.pageSize=50" \
            "&page.totalCount=617 "
    url_text1 = "https://www.tansoole.com/search/search.htm?gloabSearchVo.queryString=merck&gloabSearchVo.type=1" \
                "&gloabSearchVo.listType=1&gloabSearchVo.rootId=&gloabSearchVo.segamentId=&gloabSearchVo.branchId" \
                "=&gloabSearchVo.brand" \
                "=&gloabSearchVo.sortField=cn_len&gloabSearchVo.asc=true&l=&tf=&pro=&proTitle=&type=1&type=1&type=1" \
                "&type=1&type=1&type=1&specialSearch=&next=%E4%B8%8B%E9%A1%B5&Pagelist= "
    for i in range(13):
        if i == 0:
            response = requests.get(url_0)
        else:
            response = requests.get(
                url_text1 + "%d&page.currentPageNo=%d&page.pageSize=50&page.totalCount=617" % (i, i + 1))
        soup = BeautifulSoup(response.text, 'lxml')
        for ui in soup.find_all('ul', {"class": "show-list show-list-con"}):
            inner_list = []
            for ii in ui.find_all('li'):
                text = ii.find('span', {"class": "colorRed"})
                if ii.string:
                    inner_list.append(ii.string)
                if text:
                    inner_list.append(re.findall('\d+\.?\d*', text.string)[0])
            max_list.append(inner_list)
    for row in range(len(max_list)):
        for col in range(len(max_list[row])):

    workbook.close()


if __name__ == "__main__":
    parse_html()
