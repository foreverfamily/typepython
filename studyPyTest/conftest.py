#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-13 下午10:24
# @Author  : gonghuihui
# @File    : conftest.py
import pytest

# content of conftest.py

@pytest.fixture(scope='session')
def image_file(tmpdir_factory):
    img = compute_expensive_image()
    fn = tmpdir_factory.mktemp('data').join('img.png')
    img.save(str(fn))
    return fn

# contents of test_image.py
def test_histogram(image_file):
    img = load_image(image_file)
    # compute and test histogram