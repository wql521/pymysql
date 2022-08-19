if __name__ == '__main__':
    import pymysql

    # 打开数据库连接（connect, Connect, Connection）
    # db = pymysql.connect("localhost IP地址","root账号","password密码","TEST数据库", 3306 端口)
    db = pymysql.Connect(host='localhost', port=3306, user='root', passwd='wangqianlong0', db='Users', charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQl语句
    sql = "SELECT * FROM users"  # 查询数据库中的表users中的所有数据
    cursor.execute(sql) # 执行sql语句
    data = cursor.fetchall()    # 获取查询的所有记录
    print(data) # 打印结果
    print(type(data)) # 打印结果类型
    db.close()  # 关闭数据库连接
    print("数据库连接已关闭")
