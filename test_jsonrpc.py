#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-4 下午10:54
# @Author  : gonghuihui
# @File    : test_jsonrpc.py
import unittest
import os
import json
import jsonrpc

class TestJsonrpc(unittest.TestCase):
    """Test jsonrpc.py"""


    def setUp(self):
        print "do something before test.Prepare evironment"

    def tearDown(self):
        print "Do something after test.Clean up"
        os.remove("jsonrpc_result.json")

    def load(self):
        with open('jsonrpc_result.json') as jsonrpc:
            data = json.load(jsonrpc)
            return data

    def test_jsonrpc(self):
        jsonrpc.jsonrpc(http='www.baidu.com', http_port='8080', ws='shop.dianjia.io', ws_port='8888', path='')
        # print(os.path.isfile("jsonrpc.json"))
        self.assertTrue(os.path.isfile("jsonrpc_result.json"))
        data = self.load()
        self.assertEqual("www.baidu.com",data["http_config"]["enable"])
        self.assertEqual("shop.dianjia.io",data["ws_config"]["enable"])
        self.assertEqual("8080",data["http_config"]["listen_port"])
        self.assertEqual("8888",data["ws_config"]["listen_port"])
