#!/usr/bin/python3

import sys

#num1 = 3
num1 = int(sys.argv[1])	# "3" -> 3

if num1 % 2 == 0 :
	print("짝수")
else :
	print("홀수")
