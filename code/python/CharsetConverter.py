'''
Description: Convert all files with target extension in sourceDirs to target charset.
	It doesn't completely reliable when file isn't long enough.
Author: yuanquan
Email: yuanquan2011@qq.com
Date: 2021-07-09 21:50:40
LastEditors: yuanquan
LastEditTime: 2021-07-10 19:47:54
copyright: Copyright (c) yuanquan
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-

SourceDirs = [r"D:\Notebook\code\python\test"]
TargetExt = ["*.cpp", "*.h"]
TargetCharset = "UTF-8"

import os, sys
from chardet import detect as encodingDetect
import codecs
import fnmatch

def GetChardet(file):
	with open(file, 'rb') as fb:
		return encodingDetect(fb.read())['encoding']

def IsTargetFile(fileName, targetExt = TargetExt):
	for filter in targetExt:
		if fnmatch.fnmatch(fileName, filter):
			return True
	return False

def GetAllFiles(path):
	filePathes = list()
	for dir in os.scandir(path):
		if os.path.isdir(dir.path):
			filePathes = filePathes + GetAllFiles(dir.path)
		elif os.path.isfile(dir.path):
			if IsTargetFile(dir.path):
				filePathes.append(dir.path)
	return filePathes

def ConvertOne(file, sourceCharset, targetCharset=TargetCharset):
	targetFile = file + "tmp"
	with open(targetFile, "w", encoding=targetCharset) as targetFp:
		with open(file, 'r', encoding=sourceCharset) as sourceFp:
			for row in sourceFp.readlines():
				targetFp.write(row)

	os.remove(file)
	os.rename(targetFile, file)

def Convert():
	for dir in SourceDirs:
		for file in GetAllFiles(dir):
			sourceCharset = GetChardet(file)
			ConvertOne(file, sourceCharset)

if __name__ == "__main__":
	Convert()
