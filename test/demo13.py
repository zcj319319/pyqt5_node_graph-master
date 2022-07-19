#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/04/28 16:29
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : demo13.py
Software: PyCharm
'''
import os
import re

test=[{'U_SON1_1': [{'direct': 'input', 'port_name': 'clk', 'net_name': 'clk', 'status': 'connected'},
{'direct': 'input', 'port_name': 'rst_n', 'net_name': 'rst_n', 'status': 'connected'},
{'direct': 'input', 'port_name': 'cfg_of_son1[3:0]', 'net_name': 'cfg_of_son1[3:0]', 'status': 'connected'},
{'direct': 'input', 'port_name': 'din_of_son1[10:0]', 'net_name': 'din_of_son1_1[10:0]', 'status': 'connected'}]},

 {'U_SON1_2': [{'direct': 'input', 'port_name': 'clk', 'net_name': 'clk', 'status': 'connected'},
 {'direct': 'input', 'port_name': 'rst_n', 'net_name': 'rst_n', 'status': 'connected'},
 {'direct': 'input', 'port_name': 'cfg_of_son1[3:0]', 'net_name': 'cfg_of_son1[3:0]', 'status': 'connected'},
 {'direct': 'input', 'port_name': 'din_of_son1[10:0]', 'net_name': 'din_of_son1_2[10:0]', 'status': 'connected'}]},

 {'U_SON2': [{'direct': 'input', 'port_name': 'clk', 'net_name': 'clk', 'status': 'connected'},
 {'direct': 'input', 'port_name': 'rst_n', 'net_name': 'rst_n', 'status': 'connected'},
 {'direct': 'input', 'port_name': 'cfg_of_son2[3:0]', 'net_name': 'cfg_of_son2[3:0]', 'status': 'connected'},
 {'direct': 'input', 'port_name': 'din_of_son2[10:0]', 'net_name': 'din_of_son2[10:0]', 'status': 'connected'}]},

 {'U_SON3': [{'direct': 'input', 'port_name': 'clk', 'net_name': 'clk', 'status': 'connected'},
 {'direct': 'input', 'port_name': 'rst_n', 'net_name': 'rst_n', 'status': 'connected'},
 {'direct': 'input', 'port_name': 'cfg_of_son3[3:0]', 'net_name': 'cfg_of_son3[3:0]', 'status': 'connected'},
 {'direct': 'input', 'port_name': 'dout_of_son1_1[15:0]', 'net_name': 'dout_of_son1_1[15:0]', 'status': 'connected'},
 {'direct': 'input', 'port_name': 'dout_of_son1_2[15:0]', 'net_name': 'dout_of_son1_2[15:0]', 'status': 'connected'},
 {'direct': 'input', 'port_name': 'dout_of_son2[15:0]', 'net_name': 'dout_of_son2[15:0]', 'status': 'connected'}]},

 {'parent': [{'direct': 'output', 'port_name': 'dout_of_son3[15:0]', 'net_name': 'dout_of_son3[15:0]', 'status': 'connected'}]}]
# for em in test:
#     for i in em.keys():
#         port_name_list = []
#         instance_name=""
#         for j in em[i]:
#             if j["port_name"] not in port_name_list:
#                 port_name_list.append(j["port_name"])
#         port_name_list.sort(reverse=True)
#         print(port_name_list)

# text=select_item_cmd = '''
#                             SELECT * FROM "table_detail" WHERE %s LIKE '%s'
#                             ''' % ("instance_name_suffix","%dsadsa%")
#
# text=re.sub(r'(\*)','%s','sdfadfa*_dsad*asdsa')
# print(text)


# right_net_name_text = '{%s}' % "right_net_name_content"
# print(right_net_name_text)
# test='cfg_rf_detector_1'
# text= '(cfg_)(rf_detector)(_\d)'
# #
# regex_parmeter_ports= re.compile(text,re.VERBOSE)
# re_parameter_obj = re.search(regex_parmeter_ports, test)
# print(re_parameter_obj.group(2),len(re_parameter_obj.groups()))
#
# string_test= "3\\rfadc_detector"
# context = string_test.split("\\")
# print(context)
# with open(r'C:\Users\Administrator\Desktop\test99','r') as f:
#      file=f.readlines()
#      content=[]
#      for context in file:
#          content.append(context)
#      print(content)
str_text ='[15:0]'
data = str_text.split(':')[0].split('[')[1]
print(data)
