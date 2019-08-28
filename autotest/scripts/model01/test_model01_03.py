import  selenium
from selenium import  webdriver
import  time
import  unittest


class test_model01_01(unittest.TestCase):
    def setUp(self):
        print('it is begin')
    def test_model01_01(self):
        print('it is running')
    def tearDown(self):
        print('it is over')
if __name__ == '__main__':
    unittest.main()