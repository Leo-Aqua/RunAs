import os
appdata = os.getenv('appdata')
windir = os.getenv('windir')
os.remove(appdata+"/RunAs/nircmd.exe")
os.rmdir(appdata+'\RunAs')
os.remove(windir+"\elevate.bat")
