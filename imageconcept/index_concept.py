#! /usr/bin/env
# -*- coding: latin2 -*-
#import classificated txt files in folders of image data in train folder
#train_res is for usage of searching and test_res not used in the end

import os

#FILE_TEST_RES = 'test_res.txt'
FILE_TRAIN_RES = 'train_res.txt'

def build_train(path= r"D:\CS2108\ImageData\ImageData",limit = 10):
    train_path = path + r"\train\data"
    print train_path
    train_res = open(FILE_TRAIN_RES,'w')
    for root, dirs, list in os.walk(train_path):
        for i in list:
            if (r'.txt' in i):
                dir = os.path.join(root, i)
                fp = open(dir,'r')
                str = fp.read()
                v = str.split()
                v = map(float,v)
                tmpv = sorted(v)
                tmp = []
                for m in range(limit):
                    x = tmpv.pop()
                for m in v:
                    if (m>0):
                        if(m not in tmpv):
                            tmp.append(m)
                        else:
                            tmp.append(0)
                    else:
                        tmp.append(0)
                v = tmp
                str = ''
                for k in v:
                    str += ' ' + repr(k)
                folder = dir.replace(train_path,'').replace(i,'').replace("\\","")
                train_res.write(i+' '+folder+str+'\n')
    train_res.close()

if __name__ == '__main__':
    if (input('default folder?y\n').upper() == 'Y'):
        build_train()
    else:
        build_train(raw_input('please train input folder path\n'))