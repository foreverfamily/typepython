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


    def load(self):
        with open('jsonrpc_result.json') as jsonrpc:
            data = json.load(jsonrpc)
            return data

    def test_jsonrpc(self):
        jsonrpc.jsonrpc(http='1', http_port='', ws='', ws_port='', path='')
        print(os.path.isfile("jsonrpc_result.json"))
        self.assertTrue(os.path.isfile("jsonrpc_result.json"))
        data = self.load()
        self.assertEqual("1",data["http_config"]["enable"])

if __name__ == '__main__':

    unittest.main()
