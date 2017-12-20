#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-19 下午11:22
# @Author  : gonghuihui
# @File    : test_assert2.py
import pytest

def test_set_comparison():
    set1 = set('1308')
    set2 = set('8035')
    assert set1 == set2