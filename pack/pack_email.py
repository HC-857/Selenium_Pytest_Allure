# coding:utf-8
# ==============================
#         邮件类的封装
# ==============================
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from config import config
from pack.pack_log import logger

class emailPack:
    #初始化发件人，密码，收件人列表
    def __init__(self,server_host=None,fromaddr=None,password=None,toaddrs=None):
        if fromaddr == None:
            self.fromaddr = config.EMAIL_FROMADDR
            self.password = config.EMAIL_PASSWORD
        else:
            self.fromaddr = fromaddr
            self.password = password

        if toaddrs == None:
            self.toaddrs = config.EMAIL_TOADDR
        else:
            self.toaddrs = toaddrs

        if server_host == None: #设置邮件服务器默认值
            self.server = smtplib.SMTP('smtp.qq.com')
        else:
            self.server = smtplib.SMTP(server_host)
        self.message = MIMEMultipart() #邮件体

    #设置发件人名称，主题，内容，附件
    def set_message(self,name,title,content,filelist):
        self.message['From'] = Header(f"{name}<{self.fromaddr}>", 'utf-8') #发件人名称和地址
        self.message['Subject'] = Header(title, 'utf-8') #邮件主题
        self.message.attach(MIMEText(content)) #邮件内容
        if filelist != None: #邮件附件
            for file in filelist:
                fileApart = MIMEApplication(open(file, 'rb').read(), file.split('.')[-1])
                fileApart.add_header('Content-Disposition', 'attachment', filename=file.split("\\")[-1])
                self.message.attach(fileApart)

    #发送邮件
    def send_message(self):
        try:
            self.server.login(self.fromaddr, self.password)
            self.server.sendmail(self.fromaddr, self.toaddrs, self.message.as_string())
            print(f'邮件发送成功！收件人：{self.toaddrs}')
            self.server.quit()
        except smtplib.SMTPException as e:
            print('邮件发送失败！错误信息：', e)  # 打印错误

def send_default_email():
    log = logger()
    log.info("正在发送邮件……")
    my_email = emailPack()
    my_email.set_message(
        name = "测试小秘书",
        title="Hi！测试执行完毕提醒！",
        content='''
            您的测试报告附件已生成，请注意查收！\n
            另外也可进入http://49.234.103.36/\n
            查看最新的测试报告！
            ''',
        filelist=config.FILE_LIST
    )
    my_email.send_message()
    log.info("邮件发送完毕！")