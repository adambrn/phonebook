import logging
import log_config
import file_operations
import db_sqlite
from grafic_interface import gui_view

log_config.set_logging_conf()

file_path = file_operations.get_db_path()
db_sqlite.init_db(file_path)
data = db_sqlite.db_get(file_path,'people')
logging.info('Запуск работы программы')
gui_view(data)
logging.info('Завершение работы программы')
