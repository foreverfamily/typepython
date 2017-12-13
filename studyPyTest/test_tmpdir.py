#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-13 下午9:51
# @Author  : gonghuihui
# @File    : test_tmpdir.py

import os

# content of test_tempdir.py
def test_create_file(tmpdir):
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1
#    assert 0

def test_needsfiles(tempdir):
    print("*************")
    print(tempdir)
#     assert 0

#