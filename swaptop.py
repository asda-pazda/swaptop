# -*- coding: utf-8 -*-
__author__ = 'asda'

UNITS = ['B', 'K', 'M', 'G', 'T', 'P', 'E']

def human_size(size):
	if size > 0:
		sign = ''
	elif size < 0:
		sign = '-'
		size = -size
	else:
		return '0.00B'
	
	expo = int(math.log(size / 2, 2) / 10)
	return '%s%.2f %s' % (sign, (float(size) / (1 << (10 * expo))), UNITS[expo])

def getData():
	""" potrzebna tablica, pid --> swap """
