import logging

def set_logging_conf():
    logfile = 'phonebook.log'
    logging.basicConfig(filename=logfile,
                    encoding='utf-8',
                    level=logging.DEBUG,
                    format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")