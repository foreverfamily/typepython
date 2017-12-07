#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 12:48
# @Author  : yulu
# @File    : test_mathfunc
import unittest
from mathfunc import *

class TestMathFunc(unittest.TestCase):
    """Test mathfunc.py"""

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3,add(1, 2))
        self.assertEqual(3,add(2, 3))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1,minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6,multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2,divide(6,3))

if __name__ == '__main__':
    unittest.main()