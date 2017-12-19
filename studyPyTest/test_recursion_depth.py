#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 20:31
# @Author  : yulu
# @File    : test_recursion_depth
import pytest

#本来应该是执行失败的，可是执行成功了，为什么？？？
def test_recursion_depth():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1/0
        assert excinfo.type == 'RuntimeError'