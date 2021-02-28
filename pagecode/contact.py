#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 0:55
# @Author  : 陈庆云
# @File    : contact.py
# @Software: PyCharm
from appium.webdriver.common.mobileby import MobileBy

from pagecode.add_member_page import AddMemberPage
from pagecode.basepage import BasePage


class Contact(BasePage):
    def goto_add_member_page(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        return AddMemberPage(self.driver)
