'''
Created on 2019/05/30

@author: Rohto
'''
import MySQLdb

        
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
    conn = MySQLdb.connect(host=db_config['host'], db=db_config['db'], user=db_config['user'],
                           passwd=db_config['passwd'], charset=db_config['charset'])
    
    print('接続成功')
    print(conn)
    print('----------')
    
    # タプルで取得
    # cursor = conn.cursor()
    # 辞書型で取得
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    
except MySQLdb.Error as ex:
    print('MySQL Error: ', ex)

def tableCreate():
    try:        
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

def insertData():
    try:
        print('insertData()')
        print(conn)
        
#         cursor.execute('INSERT INTO students VALUES (%s, %s)', (1, 'toyama'))
        persons = [
            (2, 'yayoi'),
            (3, 'kongo'),
            (4, 'chino'),
            ]
        cursor.executemany('INSERT INTO students VALUES (%s, %s)', persons)
        
        conn.commit()
    except MySQLdb.Error as ex:
        print('MySQL Error: ', ex)
    
    print('----------')

def selectData():
    try:
        print('selectData()')
        print(conn)
        
        cursor.execute('SELECT * FROM students ORDER BY `id` ASC')
        
        print('件数')
        print(cursor.rowcount)
        print('全データ')
        for data in  cursor:
            print('id : ' + str(data['id']) + ', name : ' + data['name'])
    
    except MySQLdb.Error as ex:
        print('MySQL Error: ', ex)
if __name__ == '__main__':
#     insertData()
    selectData()
    conn.close()