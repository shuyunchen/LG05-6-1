#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 0:57
# @Author  : 陈庆云
# @File    : add_member.py
# @Software: PyCharm
from appium.webdriver.common.mobileby import MobileBy

from pagecode.basepage import BasePage


class AddMember(BasePage):
    def add_member(self, name, telephone):
        self._send_value['value'] = name
        self.steps('../pagecode/config_yaml/add_member_sendName.yaml')
        self._send_value['value'] = telephone
        self.steps('../pagecode/config_yaml/add_member_sendTelephone.yaml')
        # 设置部门
        self.steps('../pagecode/config_yaml/add_member_depart.yaml')
        self.steps('../pagecode/config_yaml/set_department.yaml')
        self.steps('../pagecode/config_yaml/add_member_click.yaml')
        return AddMember(self.driver)

    def get_toast(self):
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        return self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
