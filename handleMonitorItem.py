
# coding=utf-8
__author__ = 'T440P'

from monitorCenter import monitorCenter
from config import config
import time



a = monitorCenter.MonitorDB(host=config.eshost,index="monitor")


#根据查询进行局部删除
def deleteMonitor(docType,query):

    a.deleteByQuery(type=docType, query=query)

#根据查询进行局部更新
def updateMonitorItem():
    doc  ={
  "doc": {
      "strategy":
          {
              "threshold":20000
          }
  }
}

    query = {"query":{"match_all":{}}}

    a.updateByQuery(type="monitorItem",query=query,doc=doc)


def insertMonitorItemFromFile_intranet():
    f = open("profileTracker.txt")

    for l in f.readlines():
        url = l
        print(url)
        product = 'wd'
        name = "[%s]-[%s]"%(product,url)

        alarm_group_id = 122339
        if product.lower() == 'ad':
            alarm_group_id = 122339
        elif product.lower() == 'vd':
            alarm_group_id = 122343
        elif product.lower() == 'wd':
            alarm_group_id = 122341

        a.insertMonitorItem(id=config.randomId(),scope='intranet',product=product,monitor_type=1,name=name,description=''
                            ,objects=url,cluster_ids=[],alarm_group_id=alarm_group_id,
                            template_id=1,alarm_clusters=2,occur_times=2,max_alarm_count=1,
                            time_threshold=20000,ip="",opsignal=0,user="guyajun",password='gs@123456')


if __name__ == "__main__":
    # insertMonitorItemFromFile_intranet()


    # updateMonitorItem()

    ######## delete history###########
    begin = time.time()
    query = {}
    try:
         deleteMonitor(docType='event',query=query)
    except Exception as e:
         pass

    # try:
    deleteMonitor(docType='history',query=query)
    # except Exception as e:
    #     pass

    end  = time.time()
    print(end-begin)
    ####################################