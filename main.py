from os.path import exists
import file_operations
import console_interface
from grafic_interface import gui_view
path = file_operations.get_data_path()
data = {}
if not exists(path):
    file_operations.creating_csv(path)
else:
    data = file_operations.reading_csv(path)
people = list(tuple(x.values()) for x in data)
gui_view(people)
#console_interface.view(data)