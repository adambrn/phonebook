from os.path import exists
import file_operations
import db_sqlite
from grafic_interface import gui_view

#Запуск бота


file_path = file_operations.get_db_path()
db_sqlite.init_db(file_path)
data = db_sqlite.db_get(file_path,'people')
gui_view(data)
