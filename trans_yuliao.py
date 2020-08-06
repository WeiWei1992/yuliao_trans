import os

import subprocess
import time
from ffmpy import FFmpeg
from ffmpy import *
def change_file_name(path):
    # 文件路径注意结尾要加\
    files = os.listdir(path)
    n = 0
    # print files
    for f in files:
        # 设置旧文件名（路径+文件名）
        oldname = path + files[n]
        print(oldname)
        # 设置新文件名
        # newname=path + files[n][0:2]+'.wav' # 01-99
        newname = path + files[n][0:3] + '.wav'  # 100-201
        print(newname)
        # 改文件名
        # 01设置四点十分的闹铃.wav -> 01.wav
        os.rename(oldname, newname)
        n += 1


def convertfiles(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(unicode(root)) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        for f in files:
            #print(f)
            f=os.path.join(file_dir,f)
            print(f)
            if os.path.splitext(f)[1] == '.wav':
                # fname = os.path.splitext(f)[0]
                # fname=fname+'-cvt.wav'
                # fname=os.path.join(file_dir,fname)
                # print(fname)
                # cmd_cvt = "ffmpeg -i " + f + " -ac 2 " + fname
                # print(cmd_cvt)
                # print(cmd_cvt)
                # reval = os.popen(cmd_cvt)
                # print(reval.read())

                fname = os.path.splitext(f)[0]
                # print(newname)
                cmd_cvt = "ffmpeg -i " + f + " -ac 2 " + fname + "-cvt.wav"
                print(cmd_cvt)
                #cmd_cvt="dir"
                reval = os.popen(cmd_cvt)
                print(reval.read())



if __name__ == '__main__':
    path = u'C:\\Users\\weiwei\\Desktop\语音\\App\\1'
    # change_file_name(path)
    convertfiles(path)