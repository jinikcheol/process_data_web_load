

class testing_operate:

    def testing_start(input_data):
        data_list = {}
        for testing in input_data:
            test_list = {
            'machine_data': testing[0],
            'machine_data_code': testing[1]
            }
            data_list.append(test_list)
            print(data_list.values('machine_data'))
        return data_list.values('machine_data')