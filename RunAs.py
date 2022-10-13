import os
appdata = os.getenv('appdata')
windir = os.getenv('windir')
try:
    os.mkdir(appdata+'\RunAs')
except:
    print('Folder exists!')
os.chdir(appdata+'\RunAs')
os.system('curl.exe https://leoaqua.de/lf/nircmd.exe --output nircmd.exe')
f = open(windir+"\elevate.bat",'w')
f.write('@echo off\n'+appdata+'\RunAs\\nircmd.exe elevate cmd')
f.close()
