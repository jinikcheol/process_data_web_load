from database import connection

# 해야 할 일 내용 가져오기
# 최근에 작성된 순서대로
def get_machine_data_list():
    conn = connection.get_connection()

    sql = '''
        select machine_code,product_key,start_time,end_time,process_time,machine_data,machine_data_code
        from machine 
        order by process_time ASC
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()

    machine_data_list = []

    for obj in row :
        data_dic = {
            'machine_code' : obj[0],
            'product_key' : obj[1],
            'start_time': obj[2],
            'end_time': obj[3],
            'machine_data': obj[4],
            'machine_data_code': obj[5]
        }
        machine_data_list.append(data_dic)

    conn.close

    return machine_data_list