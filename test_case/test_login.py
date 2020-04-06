from page.login_page import loginPage
import allure
import pytest

@allure.title("登录功能")  # 用例标题
@allure.feature("测试登录功能的类")  # 归为大类
class TestLogin:
    base_url = "http://njqa.zgyjyx.net/teacher/login/login.html"
    login_message = [
        {"username": "15586804871", "password": "popcap123"},
        {"username": "13382013955", "password": "popcap123"},
        {"username": "15586804871", "password": "popcap123"},
        {"username": "13382013955", "password": "popcap123"},
        {"username": "15586804871", "password": "popcap123"},
        {"username": "13382013955", "password": "popcap123"},
    ]

    @allure.story("登录用例")  # 归为子类
    @allure.severity(allure.severity_level.CRITICAL)  # 发生BUG时的严重程度
    @pytest.mark.parametrize("login_message", login_message)
    def test_login(self, common_browser, login_message):
        common_browser.get(self.base_url)
        page = loginPage(common_browser)
        page.enter_user_info(username=login_message['username'], password=login_message['password'])
        page.click_login()
        assert "亿教亿学" in common_browser.title

if __name__ == '__main__':
    pytest.main()

