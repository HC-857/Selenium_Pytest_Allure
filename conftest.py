import os
import pytest
from selenium.webdriver import DesiredCapabilities

from pack.pack_log import logger
from time import sleep
from selenium import webdriver
from config import config

log = logger()
# pytest配置对象
# 注意此对象只能在顶层目录的conftest.py文件中完成
# action：store 存储参数
# default 参数默认值，此处为“device”
# help 参数帮助信息，此处为无
def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="device", help="None")

# 解析命令行
@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

@pytest.fixture
def common_browser(cmdopt):
    os.system('chcp 65001')
    print(cmdopt)
    if cmdopt == "chrome":
        # 注意这里5001是selenium grid设置的端口号
        browser = webdriver.Remote(
            command_executor='http://www.laobaaoligei.cn:5001/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    else:
        raise Exception
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
    sleep(2)
