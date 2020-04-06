# coding:utf-8
# ==============================
#         生成报告的封装
# ==============================
import os
import shutil
import subprocess
from config import config
from pack.pack_log import logger

class TestManager:
    def __init__(self):
        self.log = logger()

    def run_bat(self, file):
        p = subprocess.Popen("cmd.exe /c" + file, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        curline = p.stdout.readline()
        while (curline != b''):
            print(curline)
            curline = p.stdout.readline()
        p.wait()
        print(p.returncode)

    def del_old_result(self):
        self.log.info("删除旧的结果集……")
        if os.path.exists(config.REPORT_RESULT_PATH):
            shutil.rmtree(config.REPORT_RESULT_PATH)

    def del_old_screenshot(self):
        self.log.info("删除旧的截图……")
        if os.path.exists(config.SCREENSHOT_DIR):
            shutil.rmtree(config.SCREENSHOT_DIR)

    def generate_report(self):
        self.log.info("生成报告……")
        result_path = config.REPORT_RESULT_PATH
        report_path = config.REPORT_END_PATH
        os.system(f"allure generate {result_path} -o {report_path} --clean")
        # 复制history文件夹，在本地生成趋势图
        files = os.listdir(config.REPORT_HISTORY_PATH)
        result_history_dir = os.path.join(config.REPORT_RESULT_PATH, "history")
        # 如果不存在则先创建文件夹
        if not os.path.exists(result_history_dir):
            os.mkdir(result_history_dir)
        for file in files:
            shutil.copy(os.path.join(config.REPORT_HISTORY_PATH, file), result_history_dir)

    def run_allure_server(self):
        self.log.info("启动allure服务！")
        os.system(f"allure open {config.REPORT_RESULT_PATH}")
