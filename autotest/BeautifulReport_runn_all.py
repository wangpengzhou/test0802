# coding:utf-8
import  selenium
from selenium import  webdriver
import  time
import  unittest
import os
# from HTMLTestRunner import  HTMLTestRunner
# from BSTestRunner import  BSTestRunner
from BeautifulReport import BeautifulReport

# 用例路径

import unittest
from BeautifulReport import BeautifulReport    #导入BeautifulReport


report_path = os.path.join(os.getcwd(), "report")

case_path = os.path.join(os.getcwd(), "scripts")

print(case_path)
if __name__ == '__main__':
    suite_tests = unittest.defaultTestLoader.discover(case_path,pattern="*.py",top_level_dir=None)     #"."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    BeautifulReport(suite_tests).report(filename='report', description='Test case result', log_path=report_path)    #log_path='.'把report放到当前目录下

