#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-21 下午10:48
# @Author  : gonghuihui
# @File    : test_yield2.py
import pytest
import smtplib

@pytest.fixture(scope="module")
def smtp():
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp:
        yield smtp  #provide the fixture value
