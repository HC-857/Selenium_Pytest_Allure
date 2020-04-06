import os
import pytest
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
        os.system('taskkill /IM chromedriver.exe /F')  # 杀掉chromeodriver进程
        driver_path = config.CHROME_DRIVER
        browser = webdriver.Chrome(executable_path=driver_path)
    elif cmdopt == "firefox":
        os.system('taskkill /IM geckodriver.exe /F')  # 杀掉geckodriver进程
        driver_path = config.FIREFOX_DRIVER
        browser = webdriver.Firefox(executable_path=driver_path)
    else:
        raise Exception
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
    sleep(2)
