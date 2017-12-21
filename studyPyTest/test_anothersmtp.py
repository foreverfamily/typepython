#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-21 下午11:29
# @Author  : gonghuihui
# @File    : test_anothersmtp.py

smtpserver = "mail.python.org"
def test_showhelo(smtp):
    assert 0,smtp.helo()