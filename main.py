from os.path import exists
import file_operations
import console_interface
path = 'phonebook.csv'
data = {}
if not exists(path):
    file_operations.creating_csv(path)
else:
    data = file_operations.reading_csv(path)
people = list(tuple(x.values()) for x in data)
print(people)
#console_interface.view(data)