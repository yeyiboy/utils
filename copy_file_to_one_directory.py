#!/usr/bin/env python
# -*- coding: cp936 -*-
#print "hello"
import os
import time
from collections import deque
sPh=r"D:\b"
tPh=r"D:\a"
def getDirAndCopyFile(sourcePath,targetPath):
        if not os.path.exists(sourcePath):
        	return
    	#abstargetPath=r"D:\a"
    	#遍历文件夹
    	for fileName in os.listdir(sourcePath):
        	absourcePath = os.path.join(sourcePath,fileName)
        #abstargetPath = os.path.join(targetPath, fileName)
        	if os.path.isdir(absourcePath):
            		getDirAndCopyFile(absourcePath,abstargetPath)
        	if os.path.isfile(absourcePath):
                        #print(absourcePath)
			abstargetPath = os.path.join(tPh,fileName)
			print(abstargetPath)
			rbf = open(absourcePath,"rb")
			wbf = open(abstargetPath,"wb")
    			while True:
                                content = rbf.readline(1024*1024)
                                if len(content)==0:
                                        break
                                wbf.write(content)
                                wbf.flush()
                        rbf.close()
                        wbf.close()

if __name__ == '__main__':
	startTime = time.clock()
    	sourcePath = sPh
    	targetPath = tPh
    	getDirAndCopyFile(sourcePath,targetPath)
    	endTime = time.clock()
    	time_mi = endTime // 60
    	time_s = endTime // 1 % 60
    	time_ms = ((endTime * 100) // 1) % 100
    	print("总用时:%02.0f:%02.0f:%2.0f" % (time_mi, time_s, time_ms))

