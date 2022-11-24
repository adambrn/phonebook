import csv
def get_data_path():
    return 'phonebook.csv'

def creating_csv(file):
    with open (file, 'w', encoding = 'utf-8') as f:
        f.write(f'Фамилия;Имя;Отчество;Номер телефона;Примечание\n')

def reading_csv(file):
    with open (file, 'r', encoding = 'utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        return list(tuple(x.values()) for x in [line for line in reader])

def write_csv(file,data):
    with open (file, 'w', encoding = 'utf-8',newline='') as f:
        f.write(f'Фамилия;Имя;Отчество;Номер телефона;Примечание\n')
        write = csv.writer(f,delimiter=';')
        write.writerows(data)
       
def export_to_txt(file_path, data):
    with open (file_path, 'w') as f:
        for  line in data:
            f.write(' '.join(line) + '\n')

