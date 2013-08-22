# -*- coding: utf-8 -*-
import re
from libs.logger import Logger
from libs.getbsoup import get_b_soup
from libs.queues import Queues

#Specific crawl method
CRAWL_METHOD = 'nested'

#Specific encoding sites (if have)
ENCODING = 'cp437'

#In nested crawling there are 2 function required, collect(url_queue) and crawl(soup)
base_path = 'http://www.amazon.com'


def collect(url_queue):
    #Use logger to debug the code
    Logger.debug('Hello amazon')
    #Get the html knowledge by parsing url
    soup = get_b_soup(base_path)
    #Travel with html knowledge
    for all_url in soup.findAll('a', href=re.compile('/gp/product/')):
        #REQUIRED
        #Send all url via url_queue
        url_queue.put(base_path + all_url['href'])


def crawl(soup):
    #Get the beautiful soup
    title = soup.find('meta', {'name': 'title'})['content']
    #And send it via the output pipe
    Queues.send_to_output(title)
