#coding=utf-8
import MySQLdb

class MySQLClass:
    def __init__(self,
                 host='127.0.0.1',
                 port = 3306,
                 user='root',
                 passwd='root',
                 db ='changeorder',
                 charset='utf8',):
        try:
            self.conn= MySQLdb.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset=charset)
        except MySQLdb.Error,e:
            errormsg = 'Cannot connect to server\nERROR (%s): %s' %(e.args[0],e.args[1])
            print errormsg
            sys.exit()

        self.cursor = self.conn.cursor()

        
    def executeSQL(self,sql=''):
        self.cursor.execute(sql)
        self.conn.commit()

    def querySQL(self,sql=''):
        count = self.cursor.execute(sql),
        allresult = self.cursor.fetchall()
        return count,allresult

    def __del__(self):
        """ Terminate the connection """
        self.conn.close()
        self.cursor.close()

if __name__ == '__main__':
    mysql = MySQLClass()
    result = mysql.querySQL('select count(*) from changeorder')
    print result
