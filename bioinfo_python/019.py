#!/usr/bin/python3

import sys

try:
	with open("noname.txt", "r") as handle:
		read = handle.readlines()
		print(3/0)
except FileFoundError:
	print("파일이 없습니다")
	sys.exit()
