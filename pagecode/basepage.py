#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 0:35
# @Author  : 陈庆云
# @File    : basepage.py
# @Software: PyCharm
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _black_list = []
    _send_value = {}

    def __init__(self, mydriver: WebDriver = None):
        self.driver = mydriver

    def find(self, by, locator):
        try:
            if isinstance(by, tuple):
                return self.driver.find_element(*by)
            else:
                return self.driver.find_element(by, locator)
        except Exception as e:
            for black in self._black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
            raise e

    def send(self, value, by, locator):
        try:
            self.find(by, locator).send_keys(value)
        except Exception as e:
            for black in self._black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value, by, locator)
            raise e

    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                if 'by' in step.keys():
                    ele = self.find(step['by'], step['locator'])
                if 'action' in step.keys():
                    if 'click' == step['action']:
                        ele.click()
                    if 'send' == step['action']:
                        content: str = step['value']
                        for key in self._send_value:
                            content = content.replace('{%s}' % key, self._send_value[key])
                            self.send(content, step['by'], step['locator'])
