import os
import datetime

# ---------------- 项目根目录 --------------------
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------- 隐式等待时间 --------------------
IMPLICITLY_WAIT_TIME = 5

# ---------------- webdriver --------------------
DRIVER_PATH = os.path.join(BASE_PATH, "driver")
CHROME_DRIVER = os.path.join(DRIVER_PATH, "chromedriver.exe")
FIREFOX_DRIVER = os.path.join(DRIVER_PATH, "geckodriver.exe")

# ---------------- 测试报告 --------------------
REPORT_PATH = os.path.join(BASE_PATH, "report")
REPORT_RESULT_PATH = os.path.join(REPORT_PATH, "allure_result")
REPORT_END_PATH = os.path.join(REPORT_PATH, "allure_report")
REPORT_HISTORY_PATH = os.path.join(REPORT_PATH, "allure_result", "history")

# ---------------- 日志相关 --------------------
# 日志级别
LOG_LEVEL = 'debug'
LOG_STREAM_LEVEL = 'debug'  # 屏幕输出流
LOG_FILE_LEVEL = 'info'   # 文件输出流
# 日志命名
LOG_FOLDER = os.path.join(BASE_PATH, 'logs')
LOG_FILE_NAME = os.path.join(LOG_FOLDER, datetime.datetime.now().strftime('%Y-%m-%d') + '.log')

# ---------------- 邮件相关 --------------------
# 邮件文件列表
FILE_LIST = [
    os.path.join(BASE_PATH, "report", "zip", "report.zip")
]

# ---------------- 压缩文件相关 --------------------
# 要压缩文件夹的根路径
REPORT_DIR = os.path.join(BASE_PATH, "report", "allure_report")

# ---------------- bat文件相关 --------------------
BAT_FILE = os.path.join(BASE_PATH, "bat", "generate_report.bat")
RUN_SERVER_FILE = os.path.join(BASE_PATH, "bat", "run_allure_server.bat")
ADD_REPORT_TO_GIT_FILE = os.path.join(BASE_PATH, "bat", "add_report_to_git.bat")

# ---------------- Email相关 --------------------
EMAIL_FROMADDR = '1310063345@qq.com'  # 发件人邮箱
EMAIL_PASSWORD = 'tmerzuwndqjaigci'   # 发件人授权码
EMAIL_TOADDR = [                      # 收件人地址列表
    '1310063345@qq.com'
]

# ---------------- 截图相关 --------------------
SCREENSHOT_DIR = os.path.join(BASE_PATH, "screenshot")

if __name__ == '__main__':
    print(SCREENSHOT_DIR)