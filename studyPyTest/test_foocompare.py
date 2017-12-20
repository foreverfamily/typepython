#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-19 下午11:33
# @Author  : gonghuihui
# @File    : test_foocompare.py
import pytest
class Foo(object):
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2

    # 与https://docs.pytest.org/en/latest/assert.html#assert执行结果不一样