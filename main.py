from os.path import exists
import csv

def creating_csv(file):
    with open (file, 'w', encoding = 'utf-8') as f:
        f.write(f'Фамилия;Имя;Отчество;Номер телефона;Примечание\n')

def reading_csv(file):
    with open (file, 'r', encoding = 'utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        return [line for line in reader]

path = 'phonebook.csv'
data = {}
if not exists(path):
    creating_csv(path)
else:
    data = reading_csv(path)

print(data)