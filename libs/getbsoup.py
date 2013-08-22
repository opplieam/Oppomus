# -*- coding: utf-8 -*-
import requests
#from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup


def get_b_soup(url, encoding=None, timeout=15):
    """
    Get page url and return as a beautiful soup.
    Ex. soup = get_b_soup('http://www.google.com')
    Raise exception if Page not found, Internal server error,
     Connection time out, Connection error and Request error.

    Keyword Arguments:
    url -> (String) Ex. 'http://www.google.com'
    encoding -> (String) page encoding Ex. 'utf-8'. Default is None
    timeout -> (Integer) waiting time in seconds before timeout
     Ex. 15 Default is 15
    """
    try:
        request = requests.get(url, timeout=timeout)
        if request.status_code == 404:
            raise Exception("Page not found Error")
        if request.status_code == 500:
            raise Exception("Internal Server Error")
    except requests.exceptions.Timeout:
        raise Exception("Connection Timeout")
    except requests.exceptions.ConnectionError:
        raise Exception("Connection Error")
    except requests.exceptions.RequestException:
        raise Exception("Request Error")
    except:
        raise

    if encoding is None:
        soup = BeautifulSoup(request.text)
        return soup
    else:
        soup = BeautifulSoup(request.text, fromEncoding=encoding)
        return soup