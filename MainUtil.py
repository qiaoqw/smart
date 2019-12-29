# -*- coding: UTF-8 -*-

import sys
from datetime import datetime
import MongoUtil
import FileUtil

# @param resources_file_path 资源文件的path
# @param base_url 爬取的连接
# @param scratch_func 爬取的方法


def main(resources_file_path, base_url, scratch_func):
    old_data = FileUtil.read(resources_file_path)  # 读取原资源
    new_data = scratch_func(base_url, old_data)  # 爬取新资源
    if new_data:  # 如果新数据不为空
        date_new_data = "//" + datetime.now().strftime('%Y-%m-%d') + "\n" + \
            "\n".join(new_data) + "\n"  # 在新数据前面加上当前日期
        FileUtil.append(resources_file_path, date_new_data)
        MongoUtil.insert(resources_file_path, date_new_data)
    else:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '----',
              getattr(scratch_func, '__name__'), ": nothing to update ")
