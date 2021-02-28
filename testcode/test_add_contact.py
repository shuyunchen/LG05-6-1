#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 0:52
# @Author  : 陈庆云
# @File    : test_add_contact.py
# @Software: PyCharm
import random
from time import sleep

import pytest

from pagecode.app_start import AppStart


def get_test_date(k: int):
    test_list = []
    name = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(k):
        for m in range(6):
            name += base_str[random.randint(0, length)]
        telephone = '182' + str(random.randint(10000000, 99999999))
        print(telephone)
        test = [name, telephone]
        test_list.append(test)
    return test_list


class TestAddContact:
    def setup(self):
        self.app = AppStart().start()

    def teardown(self):
        sleep(5)
        self.app.driver.quit()

    @pytest.mark.parametrize("name, telephone", get_test_date(1))
    def test_add_contact(self, name, telephone):
        assert "添加成功" == self.app.goto_main().goto_contact(). \
            goto_add_member_page().goto_add_member().add_member(name, telephone).get_toast()
