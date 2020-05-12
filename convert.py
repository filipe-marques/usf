#!/usr/bin/python3

''' 
Program to list files webm, mp4, mkv 
automatically and convert them with ffmpeg to mp3
Copyright (C) 2016 - 2020 Filipe Marques
'''

import os
import sys
import fnmatch

def listFiles():
    a = []
    b = []
    c = []
    zx =[]    
    for fi in os.listdir('.'):
        if fnmatch.fnmatch(fi, '*.mp4'):
            a.append(fi)
    for fil in os.listdir('.'):
        if fnmatch.fnmatch(fil, '*.webm'):
            b.append(fil)
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.mkv'):
            c.append(file)
    zx = a + b +c
    #print(zx)
    return zx

def doIt():
    g = listFiles()
    for gh in g:
        if "'" in gh:
            '''rename the name of the file without the " ' " for ffmpeg '''
            v = gh.replace("'", "")
            '''rename the file without the " ' "  to the real folder'''
            os.replace(gh, v)
            os.system("ffmpeg -i '"+ v +"' -acodec libmp3lame -ab 256k -y '"+ v +".mp3'")
        else:
            os.system("ffmpeg -i '"+ gh +"' -acodec libmp3lame -ab 256k -y '"+ gh +".mp3'")

def main():
    doIt()

if __name__ == "__main__":
    # execute only if run as a script
    main()
    sys.exit()
