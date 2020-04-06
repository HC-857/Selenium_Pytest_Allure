# coding:utf-8
# ==============================
#        压缩文件的封装
# ==============================
import os
import zipfile  # 导入模块
from pack.pack_log import logger
from config.config import REPORT_DIR

def report_zip():
    log = logger()
    ZIP_FILE_NAME = 'report.zip'  # # 压缩包的名字
    # 将压缩包创建在什么目录
    ZIP_DIR = os.path.join(os.path.dirname(REPORT_DIR), "zip")
    if not os.path.exists(ZIP_DIR):
        os.mkdir(ZIP_DIR)
    f = zipfile.ZipFile(os.path.join(ZIP_DIR, ZIP_FILE_NAME), 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_name, file_names in os.walk(REPORT_DIR):
        # 要是不replace，就从根目录开始复制
        file_path = dir_path.replace(REPORT_DIR, '')
        # file_path = dir_path
        # 实现当前文件夹以及包含的所有文件
        file_path = file_path and file_path + os.sep or ''
        for file_name in file_names:
            f.write(os.path.join(dir_path, file_name), file_path + file_name)
    f.close()
    log.info('压缩文件成功，{}'.format(ZIP_FILE_NAME))

if __name__ == '__main__':
    report_zip()
    print(REPORT_DIR)