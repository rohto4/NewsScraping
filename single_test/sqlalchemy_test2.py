'''
Created on 2019/05/30

@author: Rohto
'''
import MySQLdb
from abc import ABCMeta
class SqlAlchemyTest(object):
    __metaclass__ = ABCMeta
    conn = None
    
    def __init__(self):
        pass
        
    def connectDb(self):
            
        # MySQLの接続情報
        db_config = {
            'host': 'localhost',
            'db': 'yayoi_bot',  # Database Name
            'user': 'rohto4',
            'passwd': 'takehiro1290',
            'charset': 'utf8',
        }
    
        try:
            # 接続
            self.conn = MySQLdb.connect(host=db_config['host'], db=db_config['db'], user=db_config['user'],
                                   passwd=db_config['passwd'], charset=db_config['charset'])
            
            print('接続成功')
            print(self.conn)
            print('----------')
            
        except MySQLdb.Error as ex:
            print('MySQL Error: ', ex)
    
    def tableCreate(self):
        try:
            cursor = self.conn.cursor()
            
            cursor.execute('DROP TABLE IF EXISTS `students`')
            
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS `students` (
                    `id` int(11) NOT NULL,
                    `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
                    PRIMARY KEY (id)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
                '''
            )
            
            print('create table successful.')
        except MySQLdb.Error as ex:
            print('MySQL Error: ', ex)
    
    def insertData(self):
        try:
            print('insertData()')
            print(self.conn)
            cursor = self.conn.cursor()
            
            persons = [
                (1, 'yayoi'),
                (2, 'kongo'),
                (3, 'toyama')
                ]
            cursor.execute('INSERT INTO students VALUES (%s, %s)', persons)
            
        except MySQLdb.Error as ex:
            print('MySQL Error: ', ex)
    
    
    if __name__ == '__main__':
        connectDb()
        insertData()