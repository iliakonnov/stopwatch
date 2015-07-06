#!/usr/bin/python
#coding:utf8
from imp import load_source
from os import remove
#from os import rmdir
stopwatchName=raw_input('Enter name of stopwatch file>>>')
stopwatch = load_source('stopwatch',stopwatchName)
path='./'+stopwatchName+'Images'+'/'
coord = stopwatch.load(False,path)
comments=["secondsBackgroundCoord", "minuteBackgroundCoord", "minuteArrowCoord", "secondsArrowCoord", "resetButtonCoord", "startButtonCoord", "fontCoord", "fontSize"]
with open(path+'settings.txt','w') as f:
	for i in range(len(coord)):
		if type(coord[i]) == list:
			f.write('{x},{y},{comment}\n'.format(x=coord[i][0], y=coord[i][1], comment=comments[i]))
		elif type(coord[i]) == int:
			f.write('{x},{x},{comment}\n'.format(x=coord[i], comment=comments[i]))

remove('{a}c'.format(a=stopwatchName))
'''
if raw_input('Delete files (y/n)>>>') == 'y':
	stopwatch.delete(path)
	rmdir(path)
	remove('{a}c'.format(a=stopwatchName))
'''