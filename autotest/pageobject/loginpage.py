from basepage import *
from selenium.webdriver.common.by import By

class loginpage():
    url='/'
    username_loc = (By.NAME,'username')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.NAME,'Submit')
    def type_username(self,username):

