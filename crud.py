def create_record(record,data):
    data.append(record)
    return data 

def read_record(data):
    print(*data)

def update_record(index,record,data):
    data[index] = record
    return data

def delete_record(record,data):
    print(data)
    print(record)
    data.remove(record)
    return data