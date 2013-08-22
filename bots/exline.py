# -*- coding: utf-8 -*-
"""Most 3 useful packages"""
from libs.logger import Logger
from libs.getbsoup import get_b_soup
from libs.queues import Queues

#Specific crawl method
CRAWL_METHOD = 'line'
#Specific encoding sites (if have)
#ENCODING = 'utf-8'


#Line method have only crawl()
def crawl():
    #Use logger to debug the code
    Logger.debug('Hello google')
    #Get the html knowledge by parsing url
    soup = get_b_soup('http://www.google.com')
    #Send the data to output pipe line
    Queues.send_to_output(soup.head.title.text)
    Queues.send_to_output('http://www.google.com' + soup.head.meta['content'])

