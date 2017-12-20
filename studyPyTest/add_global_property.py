#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-13 下午11:01
# @Author  : gonghuihui
# @File    : add_global_property.py
import pytest

@pytest.fixture(scope="session")
def log_global_env_facts(f):

    if pytest.config.pluginmanager.has_plugin('junit.xml'):
        my_junit = getattr(pytest.config, '_xml', None)

        my_junit.add_golbal_property('ARCH', 'PPC')
        my_junit.add_golbal_property('STORAGE_TYPE', 'CEPH')

@pytest.mark.usefixtures(log_global_env_facts)
def start_and_prepare_evn():
    pass

class TestMe(object):
    def test_foo(self):
        assert True