#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 0:48
# @Author  : 陈庆云
# @File    : app_start.py
# @Software: PyCharm
from appium import webdriver

from pagecode.basepage import BasePage
from pagecode.main import Main


class AppStart(BasePage):
    def start(self):
        _package = 'com.tencent.wework'
        _activity = 'com.tencent.wework.launch.WwMainActivity'
        _base_url = 'http://localhost:4723/wd/hub'
        if self.driver is None:
            devices_caps = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": _package,
                "appActivity": _activity,
                "noReset": True,
                "dontStopAppOnReset": False,
                "skipDeviceInitialization": True,
                "unicodeKeyboard": True,
                "resetKeyboard": True,
            }
            self.driver = webdriver.Remote(_base_url, devices_caps)
            self.driver.implicitly_wait(5)
        # else:
        #     self.driver.start_activity(_package, _activity)
        return self

    def goto_main(self):
        return Main(self.driver)
