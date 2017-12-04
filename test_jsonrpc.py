#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-4 下午10:54
# @Author  : gonghuihui
# @File    : test_jsonrpc.py
import unittest
import os
import jsonrpc
import json

class TestJsonrpc(unittest.TestCase):

    def load(self):
        with open('jsonrpc.json') as jsonrpc:
            data = json.load(jsonrpc)
            return data

    def test_jsonrpc(self):
        jsonrpc.jsonrpc(http='1', http_port='', ws='', ws_port='', path='')
        # print(os.path.isfile("jsonrpc.json"))
        self.assertTrue(os.path.isfile("jsonrpc.json"))
        data = self.load()
        self.assertEqual("1",data["http_config"]["enable"])



