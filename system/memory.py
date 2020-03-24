import subprocess
from config import systemconfig as sysConfig


'''
  This Method is only for get the Ram Memory status 
  not to provide the swap memory details
'''
def getMemoryUsages():
  
  cmd = 'free -g | grep Mem'
  output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
  outputArr =  output.split()
  result = {"used": outputArr[2], "total": outputArr[1], "free": outputArr[3]}
  return result


'''
  Check the memory usage is reached or not
'''
def checkMemoryReachedLimit(memoryInfo):

    if float(memoryInfo["free"]) < sysConfig.MEMORY_REACH_LIMIT:
       print("Ram Free Memory is:",memoryInfo["used"]) 
       return True  
    else:
       print ("System is Healthy")
       return False  