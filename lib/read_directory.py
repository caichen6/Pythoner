# -*- coding: cp936 -*-

import os


#i.startswith('ģ����ص�ѹ'):
def readAllData(place='../'):
    for i in os.listdir(place):
        if os.path.isdir(i):
            readAllData(i)
        else: 
            print i

if __name__=="__main__":
    readAllData()
