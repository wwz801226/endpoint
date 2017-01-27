# coding=utf-8

from tracker import generic_url, dns
from monitorCenter import monitorCenter
from config import config
import requests
from tracker import generic_url
import time


es = monitorCenter.MonitorDB(host=config.eshost,index="monitor")

def inser2monitoItem():
    publicUrls =  generic_url.geturlsfrom360()

    objects =  generic_url.getobjectsfrom360()


    if len(objects) != 0:
        for i in objects:

            privateUrls = getlocalUrls(i["object"])

            #判断是否有负载均衡
            if len(privateUrls) != 0:

                ip = generic_url.getUrlDomain(i["object"])
                product = ''

                try:
                    a = i["name"].split('-')[0]
                    product = a[1:len(a)-1].lower()
                except Exception as e:
                    ex_str = traceback.format_exc()
                    print(ex_str)

                try:

                    for privateurl in privateUrls:

                        if "https" in privateurl:

                            privateurl =  privateurl.replace("https","http")

                        urls =  es.getmonitorItembyUrl(privateurl)

                        if privateurl not in urls:

                            es.insertMonitorItem(id=config.randomId(),scope='intranet',product=product,monitor_type=1,name= i["name"] ,description=''
                                    ,objects= privateurl ,cluster_ids=[],alarm_group_id=122339
                                    ,template_id=1,alarm_clusters=2,occur_times=2,max_alarm_count=1,time_threshold=10000,ip=ip,opsignal=0)

                except Exception as e:
                    print(e)

#公网url转换为私网url
def getlocalUrls(publicUrl):

    #获取域名
    domainName = generic_url.getUrlDomain(publicUrl)

    #如果做了负载均衡
    realServeripList = getrealServerUrls(domainName)
    privateUrls = []
    if len(realServeripList) != 0:

        for i in realServeripList:
            privateUrls.append(publicUrl.replace(domainName,i))

    return  privateUrls



def getrealServerUrls(domainName):
    a = monitorCenter.MonitorDB(host=config.eshost, index="monitor")

    res = es.getdomainMapping(domainName)

    if len(res) != 0:


        return res["_source"]["realServer"]
    else:
        return []


if __name__ == "__main__":
    # getlocalUrls("http://proc-appguide-mediad.gridsumdissector.com/api/healthcheck/heartbeat")

    r = requests.get(url='http://10.201.80.35',headers={'host':'rc.gridsumdissector.com'})



    # r = requests.get(url='http://10.201.40.179/track.ashx?gsadid=gad_128_RQ749CYW',headers={'host':'click.gridsumdissector.com'})


    # r = requests.get(url='http://10.200.50.217/zabbix')

    # r =  requests.get(url='http://10.200.200.166:8015/')
    # begintime = time.time()
    # r =  requests.get("http://10.201.50.120:8907/api/dsync/brandsecurity/snapshot/heartbeat/isalive")
    # endtime = time.time()


    # begintime = time.time()
    # r = requests.get("http://10.200.50.217/zabbix")
    # endtime = time.time()
    # res = requests.get("http://10.200.40.91/client/clientbin/webdissectorclient.xap" ,headers= {'host':'www.webdissector.cn'})
    # print(res)

    # r = requests.get("https://10.201.40.190/",headers = {'host':'beta-ad.gridsumdissector.com'})

    # r = requests.get("http://10.201.50.109:9091/api/dsync/jobscheduler/heartbeat/isalive", auth=('','') ,headers={})
    # rtext =  res.text


    print(r.status_code)


    # print(r.elapsed.seconds+r.elapsed.microseconds)
    # print(r.headers)
    #

    # inser2monitoItem()

