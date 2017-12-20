#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-20 下午10:46
# @Author  : gonghuihui
# @File    : test_smtpsimple.py
import pytest

@pytest.fixture()
def smtp():
    import smtplib
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=10)

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert 0
# 总是超时，为啥子嘞