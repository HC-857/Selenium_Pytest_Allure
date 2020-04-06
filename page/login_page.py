import time
from api.base_api import basePage
from selenium.webdriver.common.by import By
from page.home_page import homePage

class loginPage(basePage):
    _username_box_type = (By.NAME, "username")  # 用户名
    _password_box_type = (By.NAME, "password")  # 密码
    _submit_button_type = (By.ID, "submit")  # 登录按钮

    def enter_user_info(self, username, password):  # 登录框输入内容
        # 加*是为了解出值，否则find_element不支持
        # 用户名
        self.send_keys(loc=self._username_box_type, keyword=username)
        # 密码
        self.send_keys(loc=self._password_box_type, keyword=password)
        return self

    def click_login(self):
        self.find_element(*self._submit_button_type).click()
        time.sleep(3)
        return homePage