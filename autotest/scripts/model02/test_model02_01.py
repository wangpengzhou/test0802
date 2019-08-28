# coding:utf-8
import  selenium
from selenium import  webdriver
import  time
import  unittest


class test_model01_01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.51zxw.net/')
        self.driver.maximize_window()
        self.driver.find_element_by_id('frm_login_url').click()
        self.driver.maximize_window()
        print('it is begin')
    def test_model01_01(self):
        driver = self.driver
        driver.find_element_by_id('frm_login_url').click()
        driver.find_element_by_id('loginStr').send_keys('553603385@qq.com')
        driver.find_element_by_id('pwd').send_keys('1234567a')
        lasttendays = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/div/div[6]/label")
        # 点击复选框
        time.sleep(10)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/div/div[5]/button').click()
        print('it is running')
        driver.close()
        print('login is finished')
    def tearDown(self):
        self.driver.quit()
        print('it is over')
if __name__ == '__main__':
    unittest.main()
