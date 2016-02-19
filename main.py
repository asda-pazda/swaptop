#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

__author__ = 'asda'


def get_data():
    pid_swap = {}
    #lpid_count = len([pid for pid in os.listdir('/proc') if pid.isdigit()])
    for pid in os.listdir('/proc'):
        if pid.isdigit():
            print pid
            with open('/proc/' + pid + '/status') as status:
                for line in status:
                    if line.startswith('VmSwap'): # <- possible optimalization, why check if we get rid of it?
                        pid_swap[int(pid)] = line.split('VmSwap:')[1].strip('\t\n').replace(" ", "")
    return pid_swap
    '''for k in pid_swap.keys():
        print k, pid_swap[k]
        #print pid_swap[k]
    #print pid_swap[int('2177')]'''

if __name__ == '__main__':
    get_data()
