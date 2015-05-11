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
    proc = subprocess.Popen(['python2 mine7.py gitosis3@elec5616.com:gitcoin.git rambler', 'param'], shell=True)
    proc2 = subprocess.Popen(['python2 /home/b/81/gitcoin/mine8.py gitosis3@elec5616.com:gitcoin.git rambler', 'param'], shell=True)
    proc3 = subprocess.Popen(['python2 /home/b/61/gitcoin/mine6.py gitosis3@elec5616.com:gitcoin.git rambler', 'param'], shell=True)
    proc4 = subprocess.Popen(['python2 /home/b/51/gitcoin/mine5.py gitosis3@elec5616.com:gitcoin.git rambler', 'param'], shell=True)

    #e = 'e'
    while True:
        
            message = p.get_message()
#            mesr = message[-5:-4]
 #           print message
 #           print mesr
            time.sleep(1000)
        #print message
            if message:
                kill(proc.pid)
                kill(proc2.pid)
                kill(proc3.pid)
                kill(proc4.pid)
#                os.system('git checkout HEAD LEDGER.txt && git pull')
                os.system('git fetch origin master')
        #os.system('git checkout HEAD LEDGER.txt && git pull')
                os.system('git reset --hard origin/master')
                proc = subprocess.Popen(['python2 mine7.py gitosis3@elec5616.com:gitcoin.git rambler', 'param'], shell=True)
                proc2 = subprocess.Popen(['python2 /home/b/81/gitcoin/mine8.py gitosis3@elec5616.com:gitcoin.git rambler', 'param'], shell=True)
                proc3 = subprocess.Popen(['python2 /home/b/61/gitcoin/mine6.py gitosis3@elec5616.com:gitcoin.git rambler', 'param'], shell=True)
                proc4 = subprocess.Popen(['python2 /home/b/51/gitcoin/mine5.py gitosis3@elec5616.com:gitcoin.git rambler', 'param'], shell=True)

#    os.system('git checkout HEAD LEDGER.txt && git pull')    
printit()
  
     #   kill(proc.pid)
