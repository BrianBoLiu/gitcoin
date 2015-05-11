#!/usr/bin/env python
# coding=utf-8


import os
import subprocess
#import sys
import time
#import threading
#import signal
import redis
import psutil
#from multiprocessing import Process, Queue
r = redis.StrictRedis(host='elec5616.com', port=6379, db=0)
p = r.pubsub()
p.subscribe('gitcoin')
                
def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.get_children(recursive=True):
        proc.kill()
    process.kill()
    


def printit():
    #threading.Timer(0.1, printit).start()
    #pro = subprocess.Popen('python2 mine.py gitosis3@elec5616.com:gitcoin.git rambler', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    #while True:
    proc = subprocess.Popen(['python2 mine.py gitosis3@elec5616.com:gitcoin.git rambler', 'param'], shell=True)
    while True:
        
            message = p.get_message()
         #   time.sleep(0.000000012)
        #print message
            if message:
		kill(proc.pid)
                os.system('git checkout HEAD LEDGER.txt && git pull')
            
          #  proc2 = subprocess.Popen('python2 mine.py gitosis3@elec5616.com:gitcoin.git rambler', shell=True)
                
                proc = subprocess.Popen(['python2 mine.py gitosis3@elec5616.com:gitcoin.git rambler', 'param'], shell=True)
          #  kill(proc2.pid)
          #  proc = subprocess.Popen(['python2 mine.py gitosis3@elec5616.com:gitcoin.git rambler', 'param'], shell=True)
          #  proc2 = subprocess.Popen('python2 mine.py gitosis3@elec5616.com:gitcoin.git rambler', shell=True)
            #pro = subprocess.Popen('python2 mine.py gitosis3@elec5616.com:gitcoin.git rambler', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
            #os.killpg(pro.pid, signal.SIGTERM)
                
                
            
            #subprocess.check_output('python2 mine.py gitosis3@elec5616.com:gitcoin.git rambler', shell=True)
             
      

if __name__ == "__main__":
    os.system('git checkout HEAD LEDGER.txt && git pull')
    printit()
    #if printit():
     #   kill(proc.pid)
      #  proc = subprocess.Popen('python2 mine.py gitosis3@elec5616.com:gitcoin.git rambler', shell=True)
    #proc = subprocess.Popen('python2 mine.py gitosis3@elec5616.com:gitcoin.git rambler', shell=True)
    
