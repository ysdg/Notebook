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

from rx import catch
from sqlalchemy import true

picPath = r'F:\Notebook\code\python\testPic'

def ClickPicTest():
	try:
		button7location = pyautogui.locateOnScreen(os.path.join(picPath, 'calc7key.png'), grayscale=False, confidence=0.9)
		print(button7location)
		button7point = pyautogui.center(button7location)
		# pyautogui.doubleClick(os.path.join(picPath, 'Snipaste_2022-04-23_16-08-29.png'))
		pyautogui.click(button7point)
	except pyautogui.ImageNotFoundException:
		print("not find!")

def CmdsInputTest():
	pyautogui.hotkey(['alt', 'tab']) 
	pyautogui.write('Hello world!', interval=0.25)
	pyautogui.press('enter')
	pass

if __name__ == "__main__":
	CmdsInputTest();