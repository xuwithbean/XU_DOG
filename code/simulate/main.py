import os
import time 
import numpy as np
import threading as trd
from matplotlib import pyplot as plt
class timesim:
    def print_time(threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print ("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1

class simthread:
    threads=[]
    class timethread(trd.Thread):
        def __init__(self, threadID, name, delay):
            trd.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.delay = delay
        def run(self):
            print ("start thread" + self.name)
            trd.Lock().acquire()
            timesim.print_time(self.name, self.delay, 2)
            trd.Lock().release()
            timethread1=simthread.timethread(1,"timethread1",1)
            timethread1.start()
            simthread.threads.append(timethread1)
        def stop(self):
            self.join()
            print("quit timthread")

    class consolethread(trd.Thread):
        def __init__(self, threadID, name, delay):
            trd.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.delay = delay
        def run(self):
            print ("start thread" + self.name)
            trd.Lock().acquire()
            console.all()
            console.keyboard()
            console.cmdsfind(console.cmd)
            trd.Lock().release()
            consolethread1=simthread.consolethread(1,"consolethread1",1)
            consolethread1.start()
            simthread.threads.append(consolethread1)
        def stop(self):
            self.join()
            print("quit consolethread")
    def stop():
        for t in simthread.threads:
            t.join()
        print ("quit all threads...")
        
    
class console:
    cmd=''
    statuspast=0
    statusreal=0
    def all():
        print(" \r-----------------console-----------------\n\
                \rinput H/h to show this shell\n\
                \rinput Q/q to quit the function\n\
                \rinput P/p to play the past time's simulation\n\
                \rinput R/r to play the real time's simulation\n\
                \r----------------- status -----------------\n\
                \r0 refers to no\n\
                \r1 refers to yes\n\
                \rnow:pastsimulation:0,realsimulation:0\n\
                \r-----------------------------------------")
    def notmatch():
        print(" \rthe command you scaned in is incorrect\n\
                \rplease use 'H/h' to watch the help document\n")
    def getstatus(p,r):
        print(" \r----------------- status -----------------\n\
                \r0 refers to no\n\
                \r1 refers to yes\n\
                \rnow:pastsimulation:%d,realsimulation:%d\n\
                \r-----------------------------------------\n" %(p,r))
    def help():
        print(" \r-----------------console-----------------\n\
                \rinput H/h to show this shell\n\
                \rinput Q/q to quit the function\n\
                \rinput S/s to stop the code\n\
                \rinput P/p to play the past time's simulation\n\
                \rinput R/r to play the real time's simulation\n\
                \r-----------------------------------------\n")
    def stop(p,r):
        print(" \r----------------- status -----------------\n\
                \r0 refers to no\n\
                \r1 refers to yes\n\
                \rnow:pastsimulation:%d,realsimulation:%d\n\
                \r-----------------------------------------\n" %(p,r))
    def quit():
        print("code is stopping now...")
        os._exit(0)
    def keyboard():
        console.cmd=input("please input the cmd now\n")
    def cmdsfind(c):
        if(c=='H' or c=='h'):
            console.help()
            console.keyboard()
            console.cmdsfind(console.cmd)
        elif(c=='Q' or c=='q'):
            console.quit()
        elif(c=='P' or c=='p'):
            console.statuspast=1
            console.statusreal=0
            console.getstatus(console.statuspast,console.statusreal)
            console.keyboard()
            console.cmdsfind(console.cmd)
        elif(c=='R' or c=='r'):
            console.statuspast=0
            console.statusreal=1
            console.getstatus(console.statuspast,console.statusreal)
            console.keyboard()
            console.cmdsfind(console.cmd)
        elif(c=='S' or c=='s'):
            print("code is stopping now...")
            console.statuspast=0
            console.statusreal=0
            console.stop(console.statuspast,console.statusreal)
            console.keyboard()
            console.cmdsfind(console.cmd)
        else:
            console.notmatch()
            console.keyboard()
            console.cmdsfind(console.cmd)
    def consoletrdinit():
        simthread.consolethread(1,"consolethread1",1).run()
        print("init the consolethread")

class param:
    class body:
        width = 15*2
        length = 41*2
        shoulderlen = 9.88
        thighlen = 22.0
        shanklen = 22.2
        id = ["ftlf","frrt","bhlf","bhrt"]
        leg_pos = [(width,length),(-width,length),(width,-length),(-width,-length)]
    class valuecount:
        id = ["ftlf","frrt","bhlf","bhrt"]
        shoulder = [0,0,0,0]
        thigh = [0,0,0,0]
        shank = [0,0,0,0]
    class log:
        time=''
        value=['','','','','']
        def readlog(filex):
            with open(filex,'r') as f:
                line = f.readline()
                print("the record's date is\n")
                print(line)
                while 1:
                    line = f.readline()
                    if len(line) == 0:
                        print("log read finished")
                        break
                    ang = line.split(',')
                    if len(ang) != 5:
                        break
                    cnt=0
                    param.log.value=[0,0,0,0,'']
                    while cnt<=4:               
                        param.log.value[cnt]=float(ang[cnt])
                        cnt=cnt+1
                    if param.log.value[5] != '#':
                        break

class anim:
    def drawleg():
        fig=plt.figure()
        ax=fig.add_subplot(111,ptojection="3d")
        ax.plot()

if __name__=='__main__':
    #anim.drawleg()
    #param.log.readlog('./code/log/log.txt')
    console.consoletrdinit()