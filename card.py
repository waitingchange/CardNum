#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding:gb2312 -*-
import os, sys
import random

# 先初始化手中的牌，转化为1 - 13 或者 14 15 是大小王 的数字
def _initArr(_inputArr):
	_inputArr = _inputArr.split(',')
	lenth = len(_inputArr)
	for i in range(lenth):
		if  _inputArr[i] == 'w':
			_inputArr[i] = 14 # 小王
		elif _inputArr[i] == 'W':
			_inputArr[i] = 15 # 大王
		else:
			_inputArr[i] = int(_inputArr[i])
		_inputArr.sort()  
	return _inputArr


def _exchange(arr , _inputArr):
	lenth = len(_inputArr)
	for i in range(lenth):
		origionNum = int(_inputArr[i])
		if origionNum < 14:
			cellLen = len(arr[origionNum]) - 1
			rand = random.randint(0,cellLen)
			num = arr[origionNum][rand]
			_inputArr[i] = num
			if len(arr[origionNum]) > 0:
				arr[origionNum].remove(num)
			else:
				print "输入的个数有问题",origionNum
		else:
			num = arr[origionNum][0];
			_inputArr[i] = num
			if len(arr[origionNum]) > 0:
				arr[origionNum].remove(num)
			else:
				print "输入的个数有问题",origionNum

	return _inputArr



	


arr = {}
for i in xrange(1,14):
	num = int(i)
	arr[i] = [0,0,0,0]
	for j in xrange(4):
		arr[i][int(j) - 1] = num - 1  + int(j) * 13
arr[14] = [52]
arr[15] = [53]



# print arr

print '请输入地主的手牌 ,小王 w,大王 W'
inputDzArr = raw_input("地主牌: ")
inputDzArr = _initArr(inputDzArr)
inputDzArr = _exchange(arr , inputDzArr)

print '地主输出结果',inputDzArr


inputLeftArr = raw_input("左边牌: ")
inputLeftArr = _initArr(inputLeftArr)
inputLeftArr = _exchange(arr , inputLeftArr)

print '左边输出结果',inputLeftArr


inputRightArr = raw_input("右边牌: ")
inputRightArr = _initArr(inputRightArr)
inputRightArr = _exchange(arr , inputRightArr)

print '右边输出结果',inputRightArr






