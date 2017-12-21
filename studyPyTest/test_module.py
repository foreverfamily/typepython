#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-20 下午11:59
# @Author  : gonghuihui
# @File    : test_module.py
def test_ehlo(smtp):
    respone, msg = smtp.ehlo()
    assert respone == 250
    assert b"smtp.gmail.com" in msg
    assert 0  #for demo purpose  啥意思

def test_noop(smtp):
    respone, msg = smtp.ehlo()
    assert respone == 250
    assert 0 #for demo purpose