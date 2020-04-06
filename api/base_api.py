import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time
from config.config import SCREENSHOT_DIR

class basePage(object):
    def __init__(self, driver: webdriver.Remote):
        self.browser = driver

    #寻找元素
    def find_element(self,*loc):
        try:
            #加一个显式等待，元素加载成功
            WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located(loc))
            return self.browser.find_element(*loc)
        except AttributeError:
            print("%s页面中未能找到%s元素"%(self,loc))

    #填写文本框
    def send_keys(self,loc,keyword,click_f=True,clear_f=True):
        try:
            #getattr相当于实现self.loc(将元组变成可调用的变量)
            #loc = getattr(self,"_%s"% loc)
            if click_f:
                self.find_element(*loc).click()
            if clear_f:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(keyword)
        except AttributeError:
            print("%s页面中未能找到%s元素" % (self, loc))

    #切换frame页
    def switch_frame(self,loc):
        return self.browser.switch_to.frame(loc)

    #执行js脚本
    def js_script(self,src):
        self.browser.execute_script(src)

    # 截取图片,并保存在screenshot文件夹
    @property
    def get_screenshot(self):
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join(SCREENSHOT_DIR, f"{timestrmap}.png")
        self.browser.save_screenshot(imgPath)
        return imgPath