from os.path import exists
import file_operations
import db_sqlite
from grafic_interface import gui_view
# path = file_operations.get_data_path()

# data = []
# if not exists(path):
#     file_operations.creating_csv(path)
# else:
#     data = file_operations.reading_csv(path)
file_path = file_operations.get_db_path()
db_sqlite.init_db(file_path)
data = db_sqlite.db_get(file_path,'people')
gui_view(data)
