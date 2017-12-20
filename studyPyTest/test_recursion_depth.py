#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 20:31
# @Author  : yulu
# @File    : test_recursion_depth
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1/0
        # 为什么没有输入打印的内容
        print(excinfo.type)
        # == 什么都能通过。。。
        assert excinfo.type == '1', excinfo.type

def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)

    # 没有输出啊,郁闷了

def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r'.*123*.'):
        myfunc()