from multiprocessing import Process
import traceback
from core.botlist import get_bot_list
from core.mypool import MyPool
from libs.logger import Logger
from libs.queues import Queues
import config
import output


def worker(name):
    try:
        module = __import__('bots.' + name, fromlist=[name])
    except ImportError as e:
        Logger.logging.error(e)
        Logger.logging.error(traceback.format_exc())
        exit(0)

    #Get crawl method in the bots file and execute
    crawl_method = getattr(module, 'CRAWL_METHOD',
                           config.DEFAULT_CRAWL_METHOD).lower()
    crawl_type = __import__('controllers.' + crawl_method,
                            fromlist=[crawl_method])
    crawl_type.execute(module, name)


def main():
    #Create Logger file and output queue
    Logger(parent=True)
    Queues()

    #target is in the output.py file
    output_process = Process(target=output.execute_output, name='OutputProcess')
    output_process.start()

    pool = MyPool(processes=config.NUMBER_OF_WORKERS)
    pool.map(worker, get_bot_list())

    output_process.join()


