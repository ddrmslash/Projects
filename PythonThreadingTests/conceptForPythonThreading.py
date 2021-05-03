# This was an exploration into threading for Python3.
# I know that some math modules within Python3 are allowed to bypass the GIL this was for fun.
# A weird quirk of the GIL and threading is that when you set the threading scripts below on a low count
#   sub 200000000, the second script in the list pulls ahead consistently
#   When you increase this number to 300000000+ the scripts don't have a clear pattern

import time
from threading import Thread
import subprocess

TOTALstart = time.time()

subprocess.Popen(['python', r'C:\Users\goro\Desktop\PythonThreadingTests\THREAD4.py'])
subprocess.Popen(['python', r'C:\Users\goro\Desktop\PythonThreadingTests\THREAD1.py'])
subprocess.Popen(['python', r'C:\Users\goro\Desktop\PythonThreadingTests\THREAD2.py'])
subprocess.Popen(['python', r'C:\Users\goro\Desktop\PythonThreadingTests\THREAD3.py'])

TOTALend = time.time()
print('Time taken in seconds -', TOTALend - TOTALstart)