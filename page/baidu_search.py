from time import sleep

from selenium import webdriver

class Baidu_Search():

    def __init__(self):
        self.dev = webdriver.Chrome()
        self.dev.get("https://www.baidu.com")
        self.dev.implicitly_wait(10)

    def search(self):
        self.dev.find_element_by_xpath("//input[@id='kw']").send_keys("python")
        self.dev.find_element_by_xpath("//input[@value='百度一下']").click()
        sleep(2)

    def out(self):
        self.dev.quit()

if __name__ == '__main__':
    obj = Baidu_Search()
    obj.search()
    obj.out()