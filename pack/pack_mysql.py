#encoding=utf-8
# ==============================
#         MySQL封装
# ==============================
import MySQLdb

class mysqlPack:
    def __init__(self,conn=None):
        if conn == None:
            self.conn = MySQLdb.connect(
                host='47.99.220.37',
                user='hehe',
                port=3306,
                passwd='123456',
                db='yjyx',
                charset='utf8'
            )
        else:
            self.conn = conn
        self.c=self.conn.cursor()

    #发送mysql命令
    def send_mysql_command(self,str):
        self.c.execute(str)

    #读取一行
    def read_mysql_oneline(self):
        return self.c.fetchone

    #读取全部行
    def read_mysql_allline(self):
        return self.c.fetchall()

    #输出列表
    def get_mysql_list(self):
        for i in range(self.c.rowcount):
            print(self.c.fetchone())

if __name__ == '__main__':
    pass