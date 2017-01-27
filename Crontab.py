# coding=utf-8

import threading
import time
from monitorCenter import scanner, trigger,monitorCenter
from config import  config
from logs import log


#程序初始化endpoint对象
endPoint= monitorCenter.MonitorDB(host=config.eshost,index=config.monitorIndex)

#生成监控对象
endPoint.init()

def StartScanner(itemlist):
      # scanner.batchPush(itemlist)
      scanthread = threading.Thread(target=scanner.batchPush(itemlist))

      scanthread.start()

def StartMonitor(itemlist):
     scanthread = threading.Thread(target=trigger.startChecker(itemlist))
     scanthread.start()
if __name__ =="__main__":
    #
    baseIntervel = 1
    longIntervel = baseIntervel
    # TenMinIntervelList = endPoint.getmonitorItembyfrequence(10)
    # aa = time.time()
    # StartScanner(TenMinIntervelList)
    # bb = time.time()
    # StartMonitor(TenMinIntervelList)
    # cc = time.time()
    #
    # print("****************bb-aa****************")
    # print(bb-aa)
    # print("****************cc-aa****************")
    # print(cc-aa)

    while True:
        a = time.time()
        #更新监控对象
        endPoint.update()

        TenMinIntervelList = endPoint.getmonitorItembyfrequence(10)

        # log.logger.info("*****TenMinIntervelList*****")
        # log.logger.info(TenMinIntervelList)
        # log.logger.info("*****")

        # print("****************longIntervel******************")
        # print(longIntervel)

        if longIntervel%(baseIntervel*3) == 0 and longIntervel>baseIntervel:
            pass

        if longIntervel%(baseIntervel*5) == 0 and longIntervel>baseIntervel:
            aa = time.time()
            StartScanner(TenMinIntervelList)
            bb = time.time()
            StartMonitor(TenMinIntervelList)
            cc = time.time()

        if longIntervel%(baseIntervel*10) == 0 and longIntervel>baseIntervel:
            pass


        b =time.time()
        c = 60-(b-a)
        longIntervel+=1
        if c>0:
            time.sleep(c)