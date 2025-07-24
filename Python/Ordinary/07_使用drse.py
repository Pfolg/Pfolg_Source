# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   07_使用drse |User    Pfolg
# 2024/7/11   13:41
from selenium import webdriver  # 从selenium导入webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://www.baidu.com')  # 获取百度页面
inputElement = driver.find_element(by=By.ID, value='kw')  #获取输入框
searchButton = driver.find_element(by=By.ID, value='su')  #获取搜索按钮

inputElement.send_keys("Python")  #输入框输入"Python"
searchButton.click()  #搜索
input()
