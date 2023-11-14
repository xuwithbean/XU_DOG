import os
import numpy as np
from matplotlib import pyplot as plt
import time

class log:
    time = ''
    value=['','','','','']

def realtimerecode(filex):
    with open(filex,'r+') as f:
        ensure=input("Are you sure that you have saved the pastlog.txt and the realtime.txt?(y/n)\n")
        if ensure == 'y':
            f.truncate(0)
        else:
            os._exit(0)
        f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        f.write('\n')
        log.value=value=['0','0','0','0','!']
        while 1:
            i = 0
            while i <= 3:
                f.write(log.value[i])
                f.write(',')
                i= i+1
            f.write(log.value[i])
            f.write('\n')
            if log.value[4] != '#':
                break
