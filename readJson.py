#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-4 下午11:35
# @Author  : gonghuihui
# @File    : readJson.py

# -*- coding: utf-8 -*-
import json
import os


def load():
    with open('jsonrpc1.json') as jsonrpc:
        data = json.load(jsonrpc)
        return data



if __name__ == "__main__":

    # data = {}
    # data["last"]=time.strftime("%Y%m%d")
    # store(data)

    data = load()
    print data["http_config"]["enable"]
    os.remove("jsonrpc.json")
    print(os.path.isfile('jsonrpc.json'))
