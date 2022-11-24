from os.path import exists
import file_operations
from grafic_interface import gui_view
path = file_operations.get_data_path()
data = []
if not exists(path):
    file_operations.creating_csv(path)
else:
    data = file_operations.reading_csv(path)
gui_view(data)
