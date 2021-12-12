'''
Description: format info of mp3 music file
Author: yuanquan
Email: yuanquan2011@qq.com
Date: 2021-12-12 16:00:49
LastEditors: yuanquan
LastEditTime: 2021-12-12 18:52:58
copyright: Copyright (c) yuanquan
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mutagen.mp3 import MP3  
from mutagen.easyid3 import EasyID3  
import glob  
import os

class MusicFormatter():
	def __init__(self, source=[r"C:\Users\YQ\Music\music"], ext = [".mp3"]) -> None:
		self.sourceDir = source
		self.ext = ext
	
	@staticmethod
	def Format(path: str, filename: str, ext: list):
		fileInfo = os.path.splitext(filename)[0].split(" - ")
		if len(fileInfo) != 2: return False
		if os.path.splitext(filename)[1] not in ext: return False
		title, artist = fileInfo[0], fileInfo[1]
		song = glob.glob(os.path.join(path, filename))[0]
		mp3file = MP3(song, ID3=EasyID3)
		if "title" not in mp3file and "artist" not in mp3file:
			mp3file["title"] = title
			mp3file["artist"] = artist
			mp3file.save()
			print("Modify file: ", os.path.join(path, filename))
		
	def Exec(self, dirs=list):
		""""
		add title and artist info to music file.
		music file name = title + artist
		"""
		for path in dirs:
			for dir in os.scandir(path):
				if os.path.isdir(dir.path):
					self.Exec([dir.path])
				elif os.path.isfile(dir.path):
					self.Format(os.path.dirname(dir.path), os.path.basename(dir.path), self.ext)


if __name__ == "__main__":
	# MusicFormatter.Format(r"C:\Users\YQ\Music\music", "拆东墙 - 许嵩.mp3")
	formater = MusicFormatter()
	formater.Exec(formater.sourceDir)
	pass

