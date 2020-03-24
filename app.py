import time, threading
import subprocess

from system import memory as sysMem

'''
Starting an application. Application will run every 30 seconds
'''
def start():

  print(time.ctime())
  time.sleep(10) 
  thread = threading.Timer(30, start)
  thread.setName('thread')
  thread.start()

  memInfo = sysMem.getMemoryUsages()
  print(memInfo)

  if sysMem.checkMemoryReachedLimit(memInfo) == True: 
      cmd='zenity --error --title="NJ Memory Reached Alert" --text="Your memory crossed the limit"' 
      subprocess.call(cmd, shell=True)
      thread.cancel()

if __name__ == "__main__":
    start()
