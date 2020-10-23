from database import connection

# 해야 할 일 내용 가져오기
# 최근에 작성된 순서대로
def get_quality_data_list(char2):
    conn = connection.get_connection()

    sql = '''
        select product_key,product_test
        from product_quality
        where product_test = '%s'
    ''' % (char2)

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()

    data_list = []

    for obj in row :
        data_dic = {
            'product_key' : obj[0],
            'product_test' : obj[1]

        }
        data_list.append(data_dic)

    conn.close

    return data_list