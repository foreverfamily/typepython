#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 20:31
# @Author  : yulu
# @File    : test_recursion_depth
import pytest

def test_recursion_depth():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1/0
        assert excinfo.type == 'RuntimeError'