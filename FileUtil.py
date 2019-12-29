# -*- coding: UTF-8 -*-
import conf_dev
import conf_test
import platform

# configure Multi-confronment
# 判断当前系统，并引入相对的配置文件
platform_os = platform.system()
config = conf_dev
if(platform_os == 'Linux'):
    config = conf_test
# path
data_root_path = config.data_root_path


# load old data
def read(resource_file_path, encode='utf-8'):
    file_path = data_root_path + resource_file_path
    outputs = []
    for line in open(file_path, encoding=encode):
        if not line.startswith("//"):
            outputs.append(line.strip('\n').split(',')[-1])
    return outputs

# append new data to file from scratch


def append(resource_file_path, data, encode='utf-8'):
    file_path = data_root_path + resource_file_path
    with open(file_path, 'a', encoding=encode) as f:
        f.write(data)
    f.close
