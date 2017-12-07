#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 12:48
# @Author  : yulu
# @File    : test_mathfunc
import unittest
from mathfunc import *

class TestMathFunc(unittest.TestCase):
    """Test mathfunc.py"""

    # def setUp(self):
    #     """do something before test.Prepare enviroment"""
    #     print("do something before test.Prepare enviroment")
    #
    # def tearDown(self):
    #     """Do something after test.Clean up"""
    #     print("Do something after test.Clean up")

    @classmethod
    def setUpClass(cls):
        print("This setUp() method only called once.")

    @classmethod
    def tearDownClass(cls):
        print("This tearDown() method only called once too.")

    def test_add(self):
        """Test method add(a, b)"""
        print("add")
        self.assertEqual(3,add(1, 2))
        self.assertEqual(5,add(2, 3))

    def test_minus(self):
        """Test method minus(a, b)"""
        print("minus")
        self.assertEqual(1,minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        print("multi")
        self.assertEqual(6,multi(2, 3))

    # @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        """Test method divide(a, b)"""
        self.skipTest('Do not this case.')
        print("divide")
        self.assertEqual(2,divide(6,3))

if __name__ == '__main__':
    unittest.main()