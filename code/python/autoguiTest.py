'''
Description: file content
Author: yuanquan
Email: yuanquan2011@qq.com
Date: 2022-04-23 15:59:39
LastEditors: yuanquan
LastEditTime: 2022-04-23 16:59:19
copyright: Copyright (c) yuanquan
'''
import pyautogui
import os
import time

from rx import catch
from sqlalchemy import true

picPath = r'F:\Notebook\code\python\testPic'

def clickPicTest():
	try:
		button7location = pyautogui.locateOnScreen(os.path.join(picPath, 'calc7key.png'), grayscale=False, confidence=0.9)
		print(button7location)
		button7point = pyautogui.center(button7location)
		# pyautogui.doubleClick(os.path.join(picPath, 'Snipaste_2022-04-23_16-08-29.png'))
		pyautogui.click(button7point)
	except pyautogui.ImageNotFoundException:
		print("not find!")

def generateNodeCmds(values: dict):
	cmds = list()
	cmds.append("kubectl exec -it {podName} -c tsdb-service -- bash".format(**values))
	# add cmds
	
	cmds.append('exit')
	return cmds

def generateNodesCmds():
	nodes = [
		{'ip': '192.168.12.57', 'podName': 'tsdb-service-0'},
		{'ip': '192.168.12.58', 'podName': 'tsdb-service-1'},
		{'ip': '192.168.12.59', 'podName': 'tsdb-service-2'},
	]
	cmds = list()
	for mValues in nodes:
		cmds.append("ssh root@{ip}".format(**mValues))
		cmds.append('Supos1304')
		cmds = cmds + generateNodeCmds(mValues)
		cmds.append('exit')
	return cmds

def cmdsInputTest(x: int, y: int):
	pyautogui.moveTo(x, y)
	pyautogui.click(x, y)
	cmdStrs = generateNodesCmds()
	# cmdStrs = [
	# 	'ssh root@192.168.12.57', 
	# 	'Supos1304',
	# 	'kubectl exec -it tsdb-service-0 -c tsdb-service -- bash',
	# 	'cd icore/config',
	# 	'cat /data/rtdb_setting.json',
	# 	'exit',
	# 	'exit',
	# ]
	for cmd in cmdStrs:		
		time.sleep(0.05 * len(cmd))
		pyautogui.write(cmd, interval=0.01)
		time.sleep(0.05 * len(cmd))
		pyautogui.press('enter')


if __name__ == "__main__":
	x, y = pyautogui.size()
	cmdsInputTest(x/2, y/2);
	
