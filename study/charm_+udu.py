#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/07/04 19:16
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : charm_+udu.py
Software: PyCharm
'''
import subprocess

def core_run_info():
  out_bytes = subprocess.check_output("pgrep 'your exe comand' | xargs", shell=True)
  out_text = out_bytes.decode('utf-8')

  processId = out_text[:-1].split(' ')
  if processId[0] == '':
    print('no running  processes!!!')
    return
  print('Total [%d] processes%s'%(len(processId), processId))
  for process in processId:
    print(' ------------- processId:', process, '------------------')
    cmd = "ls /proc/" + process + "/task/ | xargs"
    tasks = subprocess.check_output(cmd, shell=True)
    task_text = tasks.decode('utf-8')

    task = task_text[:-1].split(' ')

    for taskId in task:
      cmd = "cat /proc/" + process + "/task/" + taskId + "/status | egrep 'Name|Cpus_allowed_list'| awk '{print $2 }' | xargs"
      tasks = subprocess.check_output(cmd, shell=True)

      task_text = tasks.decode('utf-8')
      threadName = task_text.split(' ')[0]
      Cpus_allowed_list = task_text.split(' ')[1][:-1]
      print('  taskId :[ %-6s]   threadName : %-16s Cpus_allowed_list : %s'%(taskId,threadName,Cpus_allowed_list))
  return

core_run_info()