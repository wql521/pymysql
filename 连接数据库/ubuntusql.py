if __name__ == '__main__':

    import pymysql
    from sshtunnel import SSHTunnelForwarder

    ssh_host = "1.117.23.211"  # 堡垒机ip地址或主机名
    ssh_port = 22  # 堡垒机连接mysql服务器的端口号，一般都是22，必须是数字
    ssh_user = "ubuntu"  # 这是你在堡垒机上的用户名
    ssh_password = "Wql131421"  # 这是你在堡垒机上的用户密码
    mysql_host = "127.0.0.1"  # 这是你mysql服务器的主机名或ip地址
    mysql_port = 3306  # 这是你mysql服务器上的端口，3306，mysql就是3306，必须是数字
    mysql_user = "root"  # 这是你mysql数据库上的用户名
    mysql_password = "wangqianlong0"  # 这是你mysql数据库的密码
    mysql_db = "Users"  # mysql服务器上的数据库名

    # 严格缩进要求，否则连接失败
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),  # 堡垒机的ip地址和端口号
            ssh_username=ssh_user,  # 堡垒机的用户名
            ssh_password=ssh_password,  # 堡垒机的密码
            remote_bind_address=(mysql_host, mysql_port)) as server:  # mysql服务器的ip地址和端口号

        conn = pymysql.connect(host=mysql_host,  # mysql服务器的ip地址
                               port=server.local_bind_port,  # 这是你mysql服务器的端口，3306，mysql就是3306，必须是数字
                               user=mysql_user,  # mysql服务器的用户名
                               passwd=mysql_password,  # mysql服务器的用户名和密码
                               db=mysql_db)  # 连接mysql服务器

        cursor = conn.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor

        # -------------------------------------------------操作数据库（以查询为例子）-----------------------------------------------------------------

        cursor.execute("select * from users")  # 查询数据库中的表users中的所有数据
        data = cursor.fetchall()  # 获取查询的所有记录

        for row in data:
            bianhao = row[0]
            name = row[1]
            password = row[2]
            print("ID=%s Name = %s, birth = %s" % (bianhao,name, password))

        conn.commit()   # 提交事务
        server.close()  # 关闭ssh连接
        cursor.close()  # 关闭游标
