#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 0:54
# @Author  : 陈庆云
# @File    : main.py
# @Software: PyCharm
from pagecode.basepage import BasePage
from pagecode.contact import Contact


class Main(BasePage):
    def goto_contact(self):
        self.steps('../pagecode/config_yaml/main.yaml')
        return Contact(self.driver)