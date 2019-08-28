from time import  sleep
class Page():
    def __init__(self,driver):
        self.driver = driver
        self.base_url = "https://mail.qq.com"
        self.timeout = 10
    def _open(self,url):
        url_ = self.base_url+url
        print('the test pageis %s'%url_)
        self.driver.get(url_)
        sleep(2)
    def open(self):
        self._open(self.url)
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
