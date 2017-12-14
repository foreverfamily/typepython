#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-10 下午10:26
# @Author  : gonghuihui
# @File    : test_class.py

class TestClass:
    def test_one(self):
        assert "h" in "this"

    def test_two(self):
        x = "hello"
        assert hasattr(x,"check")