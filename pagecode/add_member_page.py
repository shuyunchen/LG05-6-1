#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 0:56
# @Author  : 陈庆云
# @File    : add_member_page.py
# @Software: PyCharm
from pagecode.add_member import AddMember
from pagecode.basepage import BasePage


class AddMemberPage(BasePage):
    def goto_add_member(self):
        self.steps('../pagecode/config_yaml/add_member_page.yaml')
        return AddMember(self.driver)