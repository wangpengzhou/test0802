# coding:utf-8
from selenium import  webdriver
import  unittest
import  time
driver = webdriver.Firefox()
driver.get('https://www.51zxw.net/')
driver.maximize_window()
driver.find_element_by_id('frm_login_url').click()
driver.find_element_by_id('loginStr').send_keys('553603385@qq.com')
driver.find_element_by_id('pwd').send_keys('1234567a')
lasttendays= driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/div/div[6]/label")
# 点击复选框
time.sleep(10)
lasttendays.click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/div/div[5]/button').click()

time.sleep(10)
driver.close()
print('login is finished')

