#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyleft (ↄ) 2024 jkirchartz <me@jkirchartz.com>
#
# Distributed under terms of the NPL (Necessary Public License) license.

"""
NOTE: Lib Quotes actually checks sources for it's quotes, unlike AZQuote

Download all quotes from LibQuotes by author's name, print in fortune format
usage:
        python libquotes.py gore-vidal > vidal
"""

from pyquery import PyQuery
from fake_headers import Headers
import sys, random, re, time, json

base_url = "https://libquotes.com/"
header = Headers( headers=True ).generate() # get random header
def grabber(name, i=1):
    url = base_url + name + "/" + str(i)
    page = PyQuery(url=url, headers=header)
    quotes = page(".panel-body")
    for quote in list(quotes.items()):
        output = quote.find('.quote_link').text() # .encode('ascii', 'ignore')
        author = quote.find('.fda').text() # .encode('ascii', 'ignore')
        if output and author:
            print(output)
            print("".join(["-- ", author]))
            print('%')

    if not page('.pager > li:last-of-type').hasClass('p_current'):
        time.sleep(10)
        grabber(name, i + 1)

if __name__ == "__main__":
  grabber(''.join(sys.argv[1:]))
