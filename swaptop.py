#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'asda'

import os

UNITS = ['B', 'K', 'M', 'G', 'T', 'P', 'E']

def get_data():
    for pid in os.listdir('/proc'):

