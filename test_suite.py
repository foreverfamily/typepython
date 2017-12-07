#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 13:02
# @Author  : yulu
# @File    : test_suite
import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)
    with open('UnittestTextReport', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)