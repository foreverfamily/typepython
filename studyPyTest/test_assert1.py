#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-19 下午10:47
# @Author  : gonghuihui
# @File    : test_assert1.py
import pytest

def f():
    return 3

def test_f():
    assert f() == 3
    assert f() % 2 == 1 , "value was odd, should be even"