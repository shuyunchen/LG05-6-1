#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 16:41
# @Author  : 陈庆云
# @File    : set_department.py
# @Software: PyCharm

from pagecode.basepage import BasePage


class SetDepartment(BasePage):
    def set_department(self):
        self.steps('../pagecode/config_yaml/set_department.yaml')