import pymysql


class MySQL_query:

    def insert_product_master(x):
        conn, cur = None, None
        data1, data2, data3, data4, data5, data6, data7 = " ", " ", " ", " ", " ", " ", " "
        sql = " "
        conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
        cur = conn.cursor()

        for i in range(len(x)):
            data = x[i]
            data1 = data['product_code']
            data2 = data['product_name']
            data3 = data['product_class']
            data4 = data['product_num']
            data5 = data['product_target_l']
            data6 = data['product_target_w']
            data7 = data['product_target_h']
            sql = "INSERT INTO product_master Values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','" + data5 + "','" + data6 + "','" + data7 + "')"
            cur.execute(sql)
            conn.commit()

        conn.close()

    def insert_machine_master(x):
        conn, cur = None, None
        data1, data2, data3, data4, data5 = " ", " ", " ", " ", " "
        sql = " "
        conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
        cur = conn.cursor()

        for i in range(len(x)):
            data = x[i]
            data1 = data['machine_code']
            data2 = data['machine_class']
            data3 = data['machine_assembly']
            data4 = data['machine_process_time']
            data5 = data['machine_data_code']

            sql = "INSERT INTO machine_master Values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','" + data5 + "')"
            cur.execute(sql)
            conn.commit()

        conn.close()

    def insert_product_quality(x):
        conn, cur = None, None
        data1, data2, data3, data4, data5, data6 = " ", " ", " ", " ", " ", " "
        sql = " "
        conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
        cur = conn.cursor()

        data = x[0]
        data1 = data['product_key']
        data2 = data['product_size_l']
        data3 = data['product_size_w']
        data4 = data['product_size_h']
        data5 = data['product_test']
        data6 = data['product_test_timestamp']


        sql = "INSERT INTO product_quality Values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','" + data5 + "','" + data6 + "')"
        cur.execute(sql)
        conn.commit()

        conn.close()

    def insert_product_history(x):
        conn, cur = None, None
        data1, data2, data3 = " ", " ", " "
        sql = " "
        conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
        cur = conn.cursor()

        data = x[0]

        data1 = data['product_key']
        data2 = data['product_code']
        data3 = data['product_timestamp']

        sql = "INSERT INTO product_history Values('" + data1 + "','" + data2 + "','" + data3 + "')"
        cur.execute(sql)
        conn.commit()

        conn.close()

    def insert_machine(x):
        conn, cur = None, None
        data1, data2, data3, data4, data5, data6, data7, data8 = " ", " ", " ", " ", " ", " ", " ", " "
        sql = " "
        conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
        cur = conn.cursor()

        data = x[0]

        data1 = data['machine_code']
        data2 = data['product_key']
        data3 = data['start_time']
        data4 = data['end_time']
        data5 = data['makespan']
        data6 = data['process_time']
        data7 = data['machine_data']
        data8 = data['machine_data_code']

        sql = "INSERT INTO machine Values('" + data1 + "','" + data2 + "','" + data3 + "','" + \
              data4 + "','" + data5 + "','" + data6 + "','" + data7 + "','" + data8 + "')"
        cur.execute(sql)
        conn.commit()

        conn.close()