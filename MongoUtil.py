# -*- coding: UTF-8 -*-

import platform
from pymongo import MongoClient
from datetime import datetime, timedelta, timezone
import conf_dev
import conf_test

# configure Multi-confronment
platform_os = platform.system()
config = conf_dev
if(platform_os == 'Linux'):
    config = conf_test
# Mongodb
uri = 'mongodb://' + config.user + ':' + config.pwd + '@' + \
    config.server + ':' + config.port + '/' + config.db_name

# 将数据写入MONGODB
#@author
#@param
#@path
#@operation
#@date
# 先在mongodb中插入一条自增数据 db.sequence.insert({"_id":"version","seq":1})


def insert(path, data, operation='append'):
    client = MongoClient(uri)
    resources = client.smartdb.resources
    sequence = client.smartdb.sequence
    seq = sequence.find_one({"_id": "version"})["seq"]  # 获取自增id
    sequence.update_one({"_id": "version"}, {"$inc": {"seq": 1}})  # 自增id+1
    post_data = {"_class": "com.gionee.smart,domain.entity.Resources", "version": seq, "path": path,
                 "concent": data, "status": "enable", "operation": operation,
                 "createtime": datetime.now(timezone(timedelta(hours=8)))}
    resources.insert(post_data)  # 插入数据
