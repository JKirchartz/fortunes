#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyleft (ↄ) 2020 jkirchartz <me@jkirchartz.com>
#
# Distributed under terms of the NPL (Necessary Public License) license.

"""
WARNING: AZ Quotes allows users to submit quotes, and may have inaccurate or
duplicate quotes because of this, practice extra caution before and after using
this script. Stay vigilent.

Download all quotes from GoodReads by author's quote URL, print in fortune format
usage:
        python azquotes.py https://www.azquotes.com/author/15080-Gore_Vidal > vidal
"""

from pyquery import PyQuery
import sys, random, re, time

base_url="http://www.surrealpolitik.org/Books/view/"

def grabber(i=1):
    url = base_url + str(i)
    page = PyQuery(url)
    quotes = page(".book-quote")
    # sys.stderr.write(url + "\n")
    book_title = page('h1').text()
    author = page('.author a').text().encode('ascii', 'ignore')
    for quote in quotes.items():
        output = quote.find('.title').text().encode('ascii', 'ignore')
        re.sub(r'(\(page \d+\)|Tags: \[[^\]]*\])', '', output)
        if output and author:
            print output
            print "".join(["-- ", author])
            print '%'

    if not page('.next').hasClass('inactive'):
      time.sleep(10)
      grabber(base_url, i + 1)

if __name__ == "__main__":
  grabber(''.join(sys.argv[1:]))
