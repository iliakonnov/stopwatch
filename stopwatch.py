#!/usr/bin/python
#coding:utf8

'''
Надо исправить координаты кнопки старта. Она не нажимается в правом нижнем углу.
Надо сделать анимацию кнопок.
Сделать второй вид секундомера
Сделать версию на android
Сделать exe (pygame2exe)
'''

import pygame
import string
from os import remove
from pygame.locals import *
from imp import load_source

def setup_console(sys_enc="utf-8"):
	import sys
	import codecs
	reload(sys)
	try:
		if sys.platform.startswith("win"):
			import ctypes
			enc = "cp%d" % ctypes.windll.kernel32.GetOEMCP()
		else:
			enc = (sys.stdout.encoding if sys.stdout.isatty() else
				sys.stderr.encoding if sys.stderr.isatty() else
				sys.getfilesystemencoding() or sys_enc)
		sys.setdefaultencoding(sys_enc)
		if sys.stdout.isatty() and sys.stdout.encoding != enc:
			sys.stdout = codecs.getwriter(enc)(sys.stdout, 'replace')
		if sys.stderr.isatty() and sys.stderr.encoding != enc:
			sys.stderr = codecs.getwriter(enc)(sys.stderr, 'replace')
		from warnings import filterwarnings
		filterwarnings("ignore")
	except Exception as e:
		print("ERROR")
		import traceback
		traceback.print_exc()

setup_console()

def get_key():
	while True:
		event = pygame.event.poll()
		if event.type == KEYDOWN:
			return event.key

def display_box(screen, message):
	"Print a message in a box in the middle of the screen"
	#fontobject = pygame.font.Font("ask.ttf",15)
	fontobject = pygame.font.Font(None,20)
	screen.fill((255,255,255))
	if len(message) != 0:
		screen.blit(fontobject.render(message, 1, (0,0,0)),
								(2, (screen.get_height() / 2) - 7))
	pygame.display.flip()

def ask(screen, question):
	"ask(screen, question) -> answer"
	pygame.font.init()
	current_string = []
	display_box(screen, question + ": " + string.join(current_string,""))
	while 1:
		inkey = get_key()
		if inkey == K_BACKSPACE:
			current_string = current_string[0:-1]
		elif inkey == K_RETURN:
			break
		elif inkey == K_MINUS:
			current_string.append("_")
		elif inkey <= 127:
			current_string.append(chr(inkey))
		display_box(screen, question + ": " + string.join(current_string,""))
	return string.join(current_string,"")


testing = False

pygame.init()
pygame.display.init()
pygame.mixer.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (233, 320)
askSize = (420, 25)
caption = "Stopwatch"
screen = pygame.display.set_mode(askSize)

stopwatchName=ask(pygame.display.set_mode(askSize), 'Enter name of stopwatch file')


try:
	stopwatchFile = load_source('stopwatch',stopwatchName)
except IOError:
	while True:
		stopwatchName=inputbox.ask(pygame.display.set_mode(askSize), 'Error: file not exists')
		try:
			stopwatchFile = load_source('stopwatch',stopwatchName)
		except IOError:
			pass

objectImagesList, objectCoordList = stopwatchFile.load()
font = objectImagesList[7]
fontSize = objectCoordList[7]
tickSound = objectImagesList[6]
pygame.display.set_icon(objectImagesList[8])
'''
 №  Название             Переменная          Файл
-------------------------------------------------------------
0|1. Фон секундомера     secondsBackground   stopwatch.png   
1|2. Фон минут           minuteBackground    minuteBack.png  
2|3. Минутная стрелка    minuteArrow         minuteArrow.png 
3|4. Секундная стрелка   secondsArrow        secondsArrow.png
4|5. Кнопка сброса       resetButton         resetButton.png   
5|6. Кнопка старта       startButton         startButton.png   
6|7. Звук "тик"          tickSound           clock.ogg       
7|8. Шрифт               font                font.ttf        
8|9. Иконка              icon                icon.png  			
'''
screen = pygame.display.set_mode(size)

for i in range(0):
	time.sleep(1)
	print(i+1)


testObjectNameList = ["secondsBackground", "minuteBackground", "minuteArrow", "secondsArrow", "resetButton", "startButton", "font"]
testMoveObjectNum = 0

angle=0.6
seconds=0.0
minutes=0
hours=0
rotating=False
minuteAngle=0.01
done = False
clock = pygame.time.Clock()

def rot_center(image, angle):
	"""rotate an image while keeping its center and size"""
	orig_rect = image.get_rect()
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = orig_rect.copy()
	rot_rect.center = rot_image.get_rect().center
	rot_image = rot_image.subsurface(rot_rect).copy()
	return rot_image

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			if pos[0] > objectCoordList[5][0]+21 and pos[0] < objectCoordList[5][0]+60: #X startButton 
				if pos[1] > objectCoordList[5][1]+31 and pos[1] < objectCoordList[5][1]+52: #Y startButton
					rotating=not rotating
			elif pos[0] > objectCoordList[4][0] and pos[0] < objectCoordList[4][0]+32: #X resetButton 
				if pos[1] > objectCoordList[4][1] and pos[1] < objectCoordList[4][1]+38: #Y resetButton
					angle=0
					minuteAngle=0
					seconds,minutes,hours=0.0,0,0
			elif pos[0] > 223 and pos[0] < 233:
				if pos[1] > 310 and pos[1] < 320:
					angle = -359
					minuteAngle = -359
					seconds = 59.9
					minutes = 59
					hours = 98
					rotating = False
		if testing:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					objectCoordList[testMoveObjectNum][0]-=1
					print("{name} coords changed, {x},{y}".format(
						name=testObjectNameList[testMoveObjectNum],
						x=objectCoordList[testMoveObjectNum][0],
						y=objectCoordList[testMoveObjectNum][1]))
				elif event.key == pygame.K_RIGHT:
					objectCoordList[testMoveObjectNum][0]+=1
					print("{name} coords changed, {x},{y}".format(
						name=testObjectNameList[testMoveObjectNum],
						x=objectCoordList[testMoveObjectNum][0],
						y=objectCoordList[testMoveObjectNum][1]))
				elif event.key == pygame.K_UP:
					objectCoordList[testMoveObjectNum][1]-=1
					print("{name} coords changed, {x},{y}".format(
						name=testObjectNameList[testMoveObjectNum],
						x=objectCoordList[testMoveObjectNum][0],
						y=objectCoordList[testMoveObjectNum][1]))
				elif event.key == pygame.K_DOWN:
					objectCoordList[testMoveObjectNum][1]+=1
					print("{name} coords changed, {x},{y}".format(
						name=testObjectNameList[testMoveObjectNum],
						x=objectCoordList[testMoveObjectNum][0],
						y=objectCoordList[testMoveObjectNum][1]))
				elif event.key == pygame.K_q:
					if testMoveObjectNum < 6:
						testMoveObjectNum +=1
					else:
						testMoveObjectNum = 0
					print("Now moving object number {num} ({name})".format(name=testObjectNameList[testMoveObjectNum],num=testMoveObjectNum))
				elif event.key == pygame.K_w:
					print("All coordinates:")
					for i in range(6):
						print("{i}. {name} : {coord}".format(i=i,name=testObjectNameList[i], coord=objectCoordList[i]))
				elif event.key == pygame.K_x:
					fontSize +=1
					print("Font size: {size}".format(size=fontSize))
				elif event.key == pygame.K_z:
					if testMoveObjectNum > 0:
						fontSize -=1
					else:
						fontSize = 0
					print("Font size: {size}".format(size=fontSize))


	# =====================LOGIC
	angle=angle%-360
	minuteAngle=minuteAngle%360

	if rotating:
		#time.sleep(speed)
		pass
	if testing:
		font = pygame.font.Font('font.ttf',fontSize)

	if len(str(seconds)) != 4:
		secondsStr='0'+str(seconds)
	else:
		secondsStr=str(seconds)

	if len(str(minutes)) != 2:
		minutesStr='0'+str(minutes)
	else:
		minutesStr=str(minutes)

	if len(str(hours)) != 2:
		hoursStr='0'+str(hours)
	else:
		hoursStr=str(hours)

	if rotating:
		tickSound.play()
		seconds+=0.1
		#1print('{h}:{m}:{s}'.format(h=hoursStr,m=minutesStr,s=secondsStr))
		if seconds > 59:
			seconds=0
			minutes+=1
			if minutes > 59:
				minutes=0
				hours+=1
				if hours > 99:
					hours = 99
					rotating=False
		angle-=0.6
		minuteAngle-=0.01

	screen.fill(WHITE)
	#======================DRAWING
	for i in range(6):
		if i != 3 and i != 2:
			screen.blit(objectImagesList[i], objectCoordList[i])
	screen.blit(rot_center(objectImagesList[3],angle),objectCoordList[3])#second
	screen.blit(rot_center(objectImagesList[2],minuteAngle),objectCoordList[2])#minute
	screen.blit(font.render('{h}:{m}:{s}'.format(h=hoursStr,m=minutesStr,s=secondsStr), True, BLACK),objectCoordList[6])
	pygame.display.set_caption('{h}:{m}:{s}'.format(h=hoursStr,m=minutesStr,s=secondsStr, caption=caption))

	pygame.display.flip()
	clock.tick(10)

stopwatchFile.delete()
remove('{a}c'.format(a=stopwatchName))
pygame.quit() 