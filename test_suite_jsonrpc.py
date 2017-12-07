#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-6 下午11:24
# @Author  : gonghuihui
# @File    : test_suite_jsonrpc.py
import unittest
from test_jsonrpc import TestJsonrpc
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromCase(TestJsonrpc))

    with open('HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='TestJsonrpc Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)