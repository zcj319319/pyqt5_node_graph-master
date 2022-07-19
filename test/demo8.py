#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/04/13 12:44
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : demo8.py
Software: PyCharm
'''
import re


class extract_information:
    def __init__(self):
        self.module_name = None
        self.extract_list = []
        self.info_list = []

    def parse(self, filepath):
        with open(filepath, encoding='utf-8') as f:
            add_flag = 0
            vlogs = f.readlines()
            for line in vlogs:
                line = line.strip()
                if not line.startswith('//'):
                    module_start_m = re.match('module', line)
                    re_tail_obj = re.match(r'endmodule', line)
                    if module_start_m is not None:
                        add_flag = 1
                        self.module_name = module_start_m.string.split(" ")[1]
                        continue
                    elif module_start_m is None and re_tail_obj is not None:
                        add_flag = 0
                        break
                else:
                    continue
                if add_flag == 1:
                    if len(line) != 0:
                        self.extract_list.append(line.strip())
        print(self.extract_list)

    def extract_ports_info(self, regex_ports, regex_width):
        print('input function: get_ports_info\n')
        for unit in self.extract_list:
            re_ports_obj = re.search(regex_ports, unit)
            if re_ports_obj is not None:
                port_name = re_ports_obj.group(7)
                port_direction = re_ports_obj.group(1)
                port_width_str = re_ports_obj.group(5)
                if port_width_str is None:
                    port_width = 1
                else:
                    width_str = re.search(regex_width, port_width_str).group(2)
                    width_info_list = width_str.split(":")
                    high_str = width_info_list[0]
                    low_str = width_info_list[1]
                    if '-1' in high_str:
                        port_width = high_str.split("-")[0]
                    else:
                        high = int(high_str)
                        low = int(low_str)
                        port_width = high - low + 1 if high >= low else low - high + 1
                port_info = {"name": port_name, "direct": port_direction, "width": port_width}
                self.info_list.append(port_info)
        print(self.info_list)

regex_module_ports = re.compile(r'''
         (output|input|inout)         #1 direction
         (\s+)?                         #2
         (wire|reg)?                   #3
         (\s+)?                         #4 
         (\[[\w\-\:]+\])?              #5  width
         (\s+)?                        #6
         (\w+)                         #7   port name
         ''', re.VERBOSE)

regex_width = re.compile(r'''
     (\[)
     ([\w\-\:]+)
     (\])
     ''', re.VERBOSE)

ex = extract_information()
ex.parse("son3.v")
ex.extract_ports_info(regex_module_ports,regex_width)