# coding:utf-8
import  selenium
from selenium import  webdriver
import  time
import  unittest
import os
# from HTMLTestRunner import  HTMLTestRunner
from BSTestRunner import  BSTestRunner
# 用例路径
case_path = os.path.join(os.getcwd(), "scripts")
print(case_path)
discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
# case_path = './autotest'
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
# report_path ="./report"
# report_name = report_path+'/'+ now + 'html'
# # with open()
print(report_path)
if __name__ == "__main__":
    report_path = os.path.join(os.getcwd(), "report")
    now = time.strftime("%Y%m%d%H%M%S")
    report_name=report_path+'/'+now+'_report.html'
    print(report_name)
    with open(report_name,'wb') as f :
        runner = BSTestRunner(stream=f,title='Test Report',description='Test case result')
    # runner = unittest.TextTestRunner()
        runner.run(discover)
    f.close()

