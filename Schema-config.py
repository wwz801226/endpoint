# coding=utf-8
import datetime
monitoritem ='''
PUT monitor/_mapping/monitorItem
{
  "dynamic":"strict",
  "properties": {
    "alarm_group_id":
      {
          "type": "long"
        },
      "name":
      {
          "type": "string",
		  "index" : "not_analyzed"
        },
       "description": {
                  "type": "string",
                  "index" : "not_analyzed"
               },
      "created_at":
      {
          "type":"date",
          "format":"yyy-MM-dd HH:mm:ss"
        },
      "updated_at":
      {
          "type":"date",
          "format":"yyy-MM-dd HH:mm:ss"
        },
      "id":
      {
          "type": "long"
        },
       "monitor_type":
      {
          "type": "short"
        },
      "objects":
      {
          "type": "string",
		  "index" : "not_analyzed"
        },
      "ip":
      {
          "type": "string",
		  "index" : "not_analyzed"
        },
      "product":
      {
          "type": "string",
		  "index" : "not_analyzed"
        },
      "level":
      {
          "type": "string",
		  "index" : "not_analyzed"
        },
      "cluster_ids":
      {
          "type": "short"
        },
      "template_id":
      {
          "type": "short"
        },
      "strategy":{
        "properties":{
          "alarm_clusters":
          {
            "type":"short"
          },
          "max_alarm":
          {
            "type":"short"
          },
          "occurs":
          {
            "type":"short"
          },
           "threshold":
          {
            "type":"integer"
          }
        }
      }
        ,
      "status":
      {
          "type": "short"
        },
	  "network_scope":
	  {
	     "type":"string",
		 "index" : "not_analyzed"
	  },
	  "opsignal":
	  {
	     "type":"short"
	  }
  }
}
'''


history = '''
PUT monitor/_mapping/history
{
  "dynamic":"strict",
  "properties": {
		"id":
		  {
			  "type": "long"
			},
		 "itemid":
		  {
			  "type": "long"
			},
		 "time":
		 {
		   "type":"date",
		   "format":"yyy-MM-dd HH:mm:ss.SSSSSS"
		 },
		  "duration":
		  {
			  "type": "float"
			},
		  "ok":
		  {
			  "type": "short"
			},
		  "status_code":
		  {
			  "type": "short"
			}
		}
}
'''

alarm_group ='''
    PUT monitor/_mapping/alarmGroup
{
  "dynamic":"strict",
  "properties": {
		"id":
		  {
			  "type": "long"
			},
		 "name":
		  {
			  "type": "string",
			  "index" : "not_analyzed"
			},
		 "description":
		  {
			  "type": "string",
			  "index" : "not_analyzed"
			},
		  "send_mail":
		  {
			  "type": "short"
			},
		  "send_msg":
		  {
			  "type": "short"
			},
		  "send_time_from":
		  {
			  "type": "short"
			},
		  "send_time_to":
		  {
			  "type": "short"
			},
		  "status":
		  {
			  "type": "short"
			},
		  "type":
		  {
			  "type": "short"
			},
		 "receiver_ids":
		  {
			  "type": "long"
			},
			"signal":
		  {
			  "type": "short"
			}
		}
}
'''
#告警联系人
AlarmReciver='''
   PUT monitor/_mapping/alarmReceiver
{
  "dynamic":"strict",
  "properties": {
		"id":
		  {
			  "type": "long"
			},
		  "name":
		  {
			  "type": "string",
			  "index" : "not_analyzed"
			},
		   "email":
		  {
			  "type": "string"
			},
		   "phone":
		  {
			  "type": "string"
			}
		}
}
'''

cluster='''
{
     " area": "华北",
     " id": 1,
     " isp": "联通",
     "location": "beijing",
     " name": "北京联通"
   }
 '''
#监控模板
# '''
# GET  0
# POST 1
# HEAD 2
# '''
#is_matched
#0 匹配响应内容
#1 不匹配响应内容
#2 不关心响应内容（只看状态码）

template = '''
PUT monitor/template/_mapping
{
  "dynamic":"strict",
  "properties": {
		"cookie":
		  {
			  "type": "string",
			  "index" : "not_analyzed"
			},
		"http_method":
		  {
			  "type": "short",
			  "index" : "not_analyzed"
			},
		"id":
		  {
			  "type": "long"
			},
		"is_matched":
		  {
			  "type": "short"
			},
		"monitor_frequence":
		  {
			  "type": "short"
			},
		"name":
		  {
			  "type": "string",
			  "index" : "not_analyzed"
			},
		"request_content":
		  {
			  "type": "string"
			},
		"response_body":
		  {
			  "type": "string",
			  "index" : "not_analyzed"
			},
		"status_code":
		  {
			  "type": "short"
			},
		"monitor_type":
		  {
			  "type": "short"
			}
		}
}

     '''



event = '''
PUT monitor/_mapping/event
{
  "dynamic":"strict",
 "properties":{
       "id":{"type":"long"},
	   "type_id":{"type":"short"},
	   "item_id":{"type":"long"},
	   "start":{"type":"date",
          "format":"yyy-MM-dd HH:mm:ss"},
	   "end":{"type":"date",
          "format":"yyy-MM-dd HH:mm:ss"},
	   "status":{"type":"short"},
	   "continue_time":{"type":"long"},
	    "content":{"type":"string"},
		 "time":{"type":"date",
		   "format":"yyy-MM-dd HH:mm:ss.SSSSSS"
		 }
	   }
 }
'''

domainMapping =  '''
PUT  monitor_mapping/domainMapping1
{
  "dynamic":"strict",
  "properties": {
    "domainName":
    {
      "type": "string"
    },
    "publicVip":
    {
      "type": "string"
    },
    "realServer":
    {
      "type": "string"
    }
  }

}
'''
