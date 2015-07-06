#!/usr/bin/python
#coding:utf8
from os.path import exists

stopwatchName=raw_input('Enter name of stopwatch file>>>')
path='./'+stopwatchName+'Images'+'/'
filenames = ["stopwatch.png", "minuteBack.png", "minuteArrow.png", "secondsArrow.png", "resetButton.png", "startButton.png", "clock.ogg", "font.ttf", "icon.png"]
base64 = []
coords = []

print('\nChecking files...')
if exists(path):
	print('OK: {path} exists'.format(path=path))
else:
	print("ERROR: {path} doesn't exists")
	raise IOError
for i in filenames:
	if exists(path+i):
		print('OK: {i} exists'.format(i=i))
	else:
		print("ERROR: {i} doesn't exists".format(i=i))
		raise(IOError)
if exists(path+'settings.txt'):
	print('OK: settings.txt exists')
else:
	print("ERROR: settings.txt doesn't exists")
	raise IOError


print('\nEncoding files...')

for i in filenames:
	with open(path+i,'r') as f:
		try:
			base64.append("".join(f.read().encode('base64').splitlines()))
		except Exception as e:
			print('ERROR: {i} not encoded'.format(i=i))
			raise e
		else:
			print('OK: {i} encoded'.format(i=i))


print('\nParsing settings.txt')

with open(path+'settings.txt','r') as f:
	for i in f:
		coords.append([int(i.split(',')[0]),int(i.split(',')[1])])

print('\nGenerating "{name}"'.format(name=stopwatchName))

filE =[ 
"import os",
"def load(pyg=True,path='./'):",
"	secondsBackgroundCoord = {}".format(coords[0]),
"	minuteBackgroundCoord = {}".format(coords[1]),
"	minuteArrowCoord = {}".format(coords[2]),
"	secondsArrowCoord = {}".format(coords[3]),
"	resetButtonCoord = {}".format(coords[4]),
"	startButtonCoord = {}".format(coords[5]),
"",
"	fontCoord = {}".format(coords[6]),
"	fontSize = {}".format(coords[7][0]),
"",
"",
"	secondsBackgroundBase64 = '{}'".format(base64[0]),
"	minuteBackgroundBase64 = '{}'".format(base64[1]),
"	minuteArrowBase64 = '{}'".format(base64[2]),
"	secondsArrowBase64 = '{}'".format(base64[3]),
"	resetButtonBase64 = '{}'".format(base64[4]),
"	startButtonBase64 = '{}'".format(base64[5]),
"	tickSoundBase64 = '{}'".format(base64[6]),
"	fontBase64 = '{}'".format(base64[7]),
"	iconBase64 = '{}'".format(base64[8]),
"	objectBase64List = [secondsBackgroundBase64, minuteBackgroundBase64, minuteArrowBase64, secondsArrowBase64, resetButtonBase64, startButtonBase64, tickSoundBase64, fontBase64, iconBase64 ]",
"	objectFilenameList = ['stopwatch.png',       'minuteBack.png',       'minuteArrow.png', 'secondsArrow.png', 'resetButton.png', 'startButton.png', 'clock.ogg',     'font.ttf', 'icon.png']",
"",
"	if not os.path.exists(path):",
"		os.mkdir(path)",
"	for i in range(len(objectFilenameList)):",
"		with open(path+objectFilenameList[i],'w') as f:",
"			f.write(objectBase64List[i].decode('base64'))",
"	objectCoordList = [secondsBackgroundCoord, minuteBackgroundCoord, minuteArrowCoord, secondsArrowCoord, resetButtonCoord, startButtonCoord, fontCoord, fontSize]",
"	if pyg:",
"		import pygame",
"		secondsBackgroundImage = pygame.image.load('stopwatch.png').convert_alpha()",
"		minuteBackgroundImage = pygame.image.load('minuteBack.png').convert_alpha()",
"		minuteArrowImage = pygame.image.load('minuteArrow.png').convert_alpha()",
"		secondsArrowImage = pygame.image.load('secondsArrow.png').convert_alpha()",
"		resetButtonImage = pygame.image.load('resetButton.png').convert_alpha()",
"		startButtonImage = pygame.image.load('startButton.png').convert_alpha()",
"		tickSound = pygame.mixer.Sound('clock.ogg')",
"		font = pygame.font.Font('font.ttf',fontSize)",
"		icon = pygame.image.load('icon.png').convert_alpha()",
"",
"		tickSound=pygame.mixer.Sound('clock.ogg')",
"",
"		objectImagesList = [secondsBackgroundImage, minuteBackgroundImage, minuteArrowImage, secondsArrowImage, resetButtonImage, startButtonImage,tickSound, font, icon]",
"		objectCoordList = [secondsBackgroundCoord, minuteBackgroundCoord, minuteArrowCoord, secondsArrowCoord, resetButtonCoord, startButtonCoord, fontCoord, fontSize]",
"		return objectImagesList, objectCoordList",
"	else:",
"		return objectCoordList",
"",
"def delete(path='./'):",
"	objectFilenameList = ['stopwatch.png', 'minuteBack.png', 'minuteArrow.png', 'secondsArrow.png', 'resetButton.png', 'startButton.png','clock.ogg', 'font.ttf', 'icon.png']",
"	for i in objectFilenameList:",
"		os.remove(path+i)",
"	return",
]

print('\nSaving "{name}"'.format(name=stopwatchName))

with open(stopwatchName,'w') as f:
	for i in filE:
		f.write(i+'\n')