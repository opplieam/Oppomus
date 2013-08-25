from multiprocessing import Process, Queue
from threading import Thread, activeCount, enumerate
import traceback
from libs.getbsoup import get_b_soup
from libs.logger import Logger
import config


def crawl_thread(url, module):
    Logger.debug('Thread start')
    encoding = getattr(module, 'ENCODING', None)
    try:
        soup = get_b_soup(url, encoding=encoding)
        module.crawl(soup)
    except:
        Logger.error('Crawl error url: ' + url)
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
            #Logger.debug(str(enumerate()))
            if activeCount() <= 2:
                Logger.info('Break crawl')
                break
            else:
                Logger.debug('There are ' + str(activeCount() - 2) + ' threads left')
                continue

        #Spawn a new threads immediate after get the url
        thread = Thread(target=crawl_thread, args=(url, module), name='CrawlThread')
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