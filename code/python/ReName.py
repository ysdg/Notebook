'''
Description: file content
Author: yuanquan
Email: yuanquan2011@qq.com
Date: 2022-05-21 21:41:59
LastEditors: yuanquan
LastEditTime: 2022-05-21 21:56:03
copyright: Copyright (c) yuanquan
'''
import os

class ReName():
	def __init__(self, source: list) -> None:
		self.sourceDir = source
	
	@staticmethod
	def Format(path: str, filename: str):
		newName = filename.removeprefix("【唐诗启蒙尽在这里】B站最完整《唐诗三百首微电影》朗诵版314集完整合集，带诗词解析（每个视频由6集合成） (")
		newName = newName.removesuffix(").mp4")
		newName = newName + ".mp4"
		return os.path.join(path, newName)
		
	def Exec(self):
		""""
		add title and artist info to music file.
		music file name = title + artist
		"""
		for path in self.sourceDir:
			for dir in os.scandir(path):
				if os.path.isdir(dir.path):
					self.Exec([dir.path])
				elif os.path.isfile(dir.path):
					newName = self.Format(os.path.dirname(dir.path), os.path.basename(dir.path))
					os.rename(dir.path, newName)

if __name__ == "__main__":
	renamer = ReName([r"D:\you-get\【唐诗启蒙尽在这里】B站最完整《唐诗三百首微电影》朗诵版314集完整合集，带诗词解析（每个视频由6集合成）"])
	renamer.Exec()