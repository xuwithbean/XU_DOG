import os
import numpy as np
from matplotlib import pyplot as plt
import realtime

class quadruped_robot:
    width = 15*2
    length = 41*2
    shoulderlen = 0
    thighlen = 0
    shanklen = 0
    id = ["ftlf","frrt","bhlf","bhrt"]
    leg_pos = [(width,length),(-width,length),(width,-length),(-width,-length)]

class valuecount:
    id = ["ftlf","frrt","bhlf","bhrt"]
    shoulder = [0,0,0,0]
    thigh = [0,0,0,0]
    shank = [0,0,0,0]

class log:
    time = ''
    value=['','','','','']

def drawleg(id,shoulder,thigh,shank):
    if id == quadruped_robot.id[0]:
        print("still coding")
    elif id == quadruped_robot.id[1]:
        print("still coding")
    elif id == quadruped_robot.id[2]:
        print("still coding")
    elif id == quadruped_robot.id[3]:
        print("still coding")


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
            log.value=[0,0,0,0,'']
            while cnt<=4:               
                log.value[cnt]=float(ang[cnt])
                cnt=cnt+1
            if log.value[5] != '#':
                break

def playanim(logfile):
    fig = plt.figure()
    coordinate = fig.add_subplot(111,projection="3d")
    coordinate.scatter([0],[0],[0],"r")
    coordinate.set_xlim(-50,50)
    coordinate.set_ylim(-50,50)
    coordinate.set_zlim(-50,50)
    readlog(logfile)
    i = 0
    while i <= 3:
        drawleg(valuecount.id[i],valuecount.shoulder[i],valuecount.thigh[i],valuecount.shank[i])
        plt.pause(1)
        i = i+1
if __name__ =='__main__':
    print(" \r-------------------------------------\n\
            \rplease input mode\n\
            \rp is play the past log's anime\n\
            \rr is play the realtime dog's anime\n\
            \rq is quit the function\n\
            \r--------------------------------------")
    cmd = input("there to input mode(p/r/q)")
    if (cmd == 'p'):
        print("past log\n")
        playanim('runcode/simluate/log/pastlog.txt')
    elif (cmd == 'r'):
        print("reatime mode\n")
        realtime.realtimerecode('runcode/simluate/log/realtime.txt')
    elif (cmd == 'q'):
        print("function is endding...\n")
        os._exit(0)
    print("ok")