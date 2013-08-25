from multiprocessing import current_process, get_logger
from os.path import abspath
import logging
import config


class Logger():
    logging = None

    def __init__(self, parent=False):
        if parent:
            #get_logger() from multiprocessing package
            Logger.logging = get_logger()
        else:
            #getLogger() from logging package
            Logger.logging = logging.getLogger()
        Logger.logging.setLevel(config.LOG_LEVEL)
        #create file handler which logs even debug messages
        fh = logging.FileHandler(abspath('') + '/logs/'
                                 + str(current_process().name), mode='a')
        fh.setLevel(config.LOG_LEVEL)
        #create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(config.LOG_LEVEL)
        #create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s [%(process)d/%(processName)s] '
                                      '%(levelname)s - %(message)s', '%y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        #add the handlers to the logger
        Logger.logging.addHandler(fh)
        Logger.logging.addHandler(ch)

    @staticmethod
    def info(data):
        Logger.logging.info(data)

    @staticmethod
    def error(data):
        Logger.logging.error(data)

    @staticmethod
    def debug(data):
        Logger.logging.debug(data)

    @staticmethod
    def warning(data):
        Logger.logging.warning(data)