#!/usr/bin/env python
# -*- coding: cp936 -*-
#print "hello"
import os
import time
from collections import deque

def getDirAndCopyFile(sourcePath,targetPath):

    if not os.path.exists(sourcePath):
        return
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
        
    #�����ļ���
    for fileName in os.listdir(sourcePath):
        #ƴ��ԭ�ļ������ļ��еľ���·��
        absourcePath = os.path.join(sourcePath, fileName)
        #ƴ��Ŀ���ļ������ļ��ӵľ���·��
        abstargetPath = os.path.join(targetPath, fileName)
        #�ж�ԭ�ļ��ľ���·����Ŀ¼�����ļ�
        if os.path.isdir(absourcePath):
            #��Ŀ¼��Ŀ¼�����ھʹ�����Ӧ��Ŀ��Ŀ¼
            if not os.path.exists(targetPath):
                os.makedirs(abstargetPath)
            else:
                #�ݹ����getDirAndCopyFile()����
                getDirAndCopyFile(absourcePath,abstargetPath)
        #���ļ��ͽ��и���
        if os.path.isfile(absourcePath):
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
    sourcePath = r"D:\��װ���"
    targetPath = r"D:\a"
    getDirAndCopyFile(sourcePath,targetPath)
    #ʱ�����������㸴���ܹ������˶���ʱ��
    endTime = time.clock()
    time_mi = endTime // 60
    time_s = endTime // 1 % 60
    time_ms = ((endTime * 100) // 1) % 100
    print("����ʱ:%02.0f:%02.0f:%2.0f" % (time_mi, time_s, time_ms))

