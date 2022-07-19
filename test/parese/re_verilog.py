#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/05/11 16:59
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : re_verilog.py
Software: PyCharm
'''
import re

"verilog/Systemverilog formating"
__author__ = 'Auguesty'

f = open('hello.v', 'r+')
f2 = open('abc2.v', 'w+')
flines = f.readlines()

kongge = " "


def none_parameter(iostr):
    n = None
    if iostr == '\n':
        iostr = ''
    elif iostr == '':
        iostr = ''
    elif iostr[-1] == '\n':
        iostr = iostr[:-1]
    else:
        iostr = iostr

    if re.fullmatch(r'\s*(\S*\s*)\s*(\,)\s*', iostr):
        n = re.fullmatch(r'\s*(\S*\s*)\s*(\,)\s*', iostr)
        return f'{kongge:<4s}{n.group(1).replace(" ", ""):<24s}{n.group(2).replace(" ", ""):<s}'
    else:
        return iostr


def iorectify(iostr):
    n = None
    if iostr == '\n':
        iostr = ''
    elif iostr == '':
        iostr = ''
    elif iostr[-1] == '\n':
        iostr = iostr[:-1]
    else:
        iostr = iostr

    if re.fullmatch(r'\s*(input|output|inout)\s*(wire|reg)\s*(\[[^\:]+\:[^\:]+\])\s*([0-9a-zA-Z\_]+)\s*(\,?)\s*(.*)',
                    iostr):
        n = re.fullmatch(
            r'\s*(input|output|inout)\s*(wire|reg)\s*(\[[^\:]+\:[^\:]+\])\s*([0-9a-zA-Z\_]+)\s*(\,?)\s*(.*)', iostr)
        return f'{kongge:<4s}{n.group(1):<8s}{n.group(2):<10s}{n.group(3).replace(" ", ""):<20s}{n.group(4):<20s}{n.group(5):<8s}{n.group(6):<s}'

    elif re.fullmatch(r'\s*(input|output|inout)\s*(wire|reg)\s*([0-9a-zA-Z\_]+)\s*(\,?)\s*(.*)', iostr):
        n = re.fullmatch(r'\s*(input|output|inout)\s*(wire|reg)\s*([0-9a-zA-Z\_]+)\s*(\,?)\s*(.*)', iostr)
        return f'{kongge:<4s}{n.group(1):<8s}{n.group(2):<10s}{kongge:<20s}{n.group(3):<20s}{n.group(4):<8s}{n.group(5):<s}'

    elif re.fullmatch(r'\s*(input|output|inout)\s*([0-9a-zA-Z\_]+)\s*(\,?)\s*(.*)', iostr):
        n = re.fullmatch(r'\s*(input|output|inout)\s*([0-9a-zA-Z\_]+)\s*(\,?)\s*(.*)', iostr)
        return f'{n.group(1):<8s}{kongge:<4s}{kongge:<12s}{n.group(2):<24s}{n.group(3):<s}{n.group(4):<s}'

    elif re.fullmatch(r'\s*(input|output|inout)\s*(\[[^\:]+\:[^\:]+\])\s*([0-9a-zA-Z\_]+)\s*(\,?)\s*(.*)', iostr):
        n = re.fullmatch(r'\s*(input|output|inout)\s*(\[[^\:]+\:[^\:]+\])\s*([0-9a-zA-Z\_]+)\s*(\,?)\s*(.*)', iostr)
        return f'{n.group(1):<8s}{kongge:<4s}{n.group(2).replace(" ", ""):<12s}{n.group(3):<24s}{n.group(4):<s}{n.group(5):<s}'

    else:
        return iostr


def sigdefrectify(sigstr):
    p = None
    if sigstr == '\n':
        sigstr = ''
    elif sigstr == '':
        sigstr = ''
    elif sigstr[-1] == '\n':
        sigstr = sigstr[:-1]
    else:
        sigstr = sigstr

    if re.fullmatch(r'\s*(wire|reg)\s*(\[[^\:]+\:[^\:]+\])\s*([0-9a-zA-Z\_]+)\s*(\;)\s*(.*)', sigstr):
        p = re.fullmatch(r'\s*(wire|reg)\s*(\[[^\:]+\:[^\:]+\])\s*([0-9a-zA-Z\_]+)\s*(\;)\s*(.*)', sigstr)
        return f'{p.group(1):<8s}{p.group(2).replace(" ", ""):<12s}{p.group(3):<24s}{p.group(4):<4s}{p.group(5):<s}'
    elif re.fullmatch(r'\s*(wire|reg)\s*([0-9a-zA-Z\_]+)\s*(\;)\s*(.*)', sigstr):
        p = re.fullmatch(r'\s*(wire|reg)\s*([0-9a-zA-Z\_]+)\s*(\;)\s*(.*)', sigstr)
        return f'{p.group(1):<8s}{kongge:<12s}{p.group(2):<24s}{p.group(3):<4s}{p.group(4):<s}'

    elif re.fullmatch(r'\s*(localparam|parameter)\s*([0-9a-zA-Z\_]+)\s*(\=.+?)(\;)\s*(.*)', sigstr):
        p = re.fullmatch(r'\s*(localparam|parameter)\s*([0-9a-zA-Z\_]+)\s*(\=.+?)(\;)\s*(.*)', sigstr)
        return f'{p.group(1):<16s}{p.group(2):<12s}{p.group(3).replace(" ", ""):<24s}{p.group(4):<4s}{p.group(5):<s}'
    else:
        return sigstr


def insectify(insstr):
    q = None
    if insstr == '\n':
        insstr = ''
    elif insstr == '':
        insstr = ''
    elif insstr[-1] == '\n':
        insstr = insstr[:-1]
    else:
        insstr = insstr

    if re.fullmatch(r'(\s*\.\s*\S*)\s*'
                    r'(\()\s*'
                    r'([^\(\)\s*]*)\s*'
                    r'(\))\s*'
                    r'(\,?)\s*'
                    r'(.*)', insstr):
        q = re.fullmatch(r'(\s*\.\s*\S*)\s*(\()\s*([^\(\)\s*]*)\s*(\))\s*(\,?)\s*(.*)', insstr)
        return f'{q.group(1).replace(" ", ""):<24s}{q.group(2).replace(" ", ""):<s}{kongge:<s}{q.group(3).replace(" ", ""):<30s}{q.group(4):<s}{q.group(5):<2s}{q.group(6):<s}'
    else:
        return insstr


if __name__ == '__main__':
    f2.seek(0, 0)
    for i in flines:
        y = none_parameter(i)
        ii = iorectify(y)
        iii = sigdefrectify(ii)
        iiii = insectify(iii)
        f2.write(iiii + '\n')
    f.close()
    f2.close()
    print('done')
