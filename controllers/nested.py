from multiprocessing import Process, Queue
import threading
import traceback
from libs.getbsoup import get_b_soup
from libs.logger import Logger
import config


def crawl_thread(soup, module):
    Logger.debug('Thread start')
    try:
        module.crawl(soup)
    except:
        Logger.error('Crawl error')
        Logger.error(traceback.format_exc())
        return
    Logger.debug('Thread done')


def crawl(module, url_queue):
    #Execute the crawl process
    Logger.info('Start Crawler')
    while True:
        try:
            url = url_queue.get(timeout=config.NESTED_CRAWL_TIMEOUT)
        except:
            #If all threads are done then break the loop, Otherwise continue.
            #Why 2 ? because its need to deduct by the main thread and queue thread,
            # You can comment out the enumerate() line to see what is going on
            #Logger.debug(str(threading.enumerate()))
            if threading.activeCount() <= 2:
                Logger.info('Break crawl')
                break
            else:
                Logger.debug('There are ' + str(threading.activeCount() - 2) + ' left')
                continue

        #Spawn a new threads and parse a beautiful soup
        encoding = getattr(module, 'ENCODING', None)
        soup = get_b_soup(url, encoding=encoding)
        thread = threading.Thread(target=crawl_thread, args=(soup, module), name='CrawlThread')
        thread.start()

    Logger.info('Crawl done')


def collect(module, url_queue):
    #Excute the collect process
    Logger.info('Start Collector')
    #Send the url queue to bot via args
    module.collect(url_queue)
    Logger.info('Collect done')


def execute(module, name):
    #Execute the nested crawl method
    Logger.info('Start Execute')
    if not hasattr(module, 'collect'):
        raise NotImplementedError('You must implement collect()')

    #Create the url queue and send to collect and crawl process
    url_queue = Queue()
    collect_process = Process(target=collect, args=(module, url_queue),
                              name=name + '_CollectProcess')
    collect_process.start()

    crawl_process = Process(target=crawl, args=(module, url_queue),
                            name=name + '_CrawlProcess')
    crawl_process.start()

    #Both collect and crawl are safe
    collect_process.join()
    crawl_process.join()
    Logger.info('Execute done')