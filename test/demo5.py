#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/04/11 20:50
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : demo5.py
Software: PyCharm
'''
import json
import re


def read_vlog_netlist(vlog_file):
    vlog_lines = open(vlog_file, encoding='utf-8').readlines()
    # get inst tree
    module_start = 0
    modules = {}
    for line in vlog_lines:
        module_start_m = re.search('modules+(s+)', line)
        inst_m = re.search("s+(w+)s+(w+)s*\(", line)
        module_end_m = re.search('endmodule', line)

        if module_start_m:
            module_start = 1
            module = {}

            module_name = module_start_m.group(1)
            module['module_name'] = module_name

            insts = {}
            module['insts'] = insts

            modules[module_name] = module

        if module_end_m:
            module_start = 0

        if inst_m:
            module_name = inst_m.group(1)
            inst_name = inst_m.group(2)
            insts[inst_name] = module_name

    return modules

modules = read_vlog_netlist("example.v")
print(json.dumps(modules, indent=4))