#! /usr/bin/env python3
from pyquery import PyQuery
import sys, random, re, time

AUTHOR_REX = re.compile(r'\d+\.(\w+)$')

def grabber(base_url, i=1):
    url = base_url + "?page=" + str(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }
    page = PyQuery(url, headers=headers)
    quotes = page(".quoteText")
    auth_match = re.search(AUTHOR_REX, base_url)
    
    if auth_match:
        author = re.sub('_', ' ', auth_match.group(1))
    else:
        author = False
        
    # sys.stderr.write(url + "\n")
    for quote in quotes.items():
        # In Python 3, we need to decode the bytes to string after encoding
        quote_text = quote.remove('script').text()
        # Handle non-ASCII characters properly
        quote_clean = quote_text.encode('ascii', 'ignore').decode('ascii')
        
        if author:
            quote_clean = quote_clean.replace(author, " -- " + author)
            
        print(quote_clean)
        print('%')
    
    if not page('.next_page').hasClass('disabled'):
        time.sleep(10)
        grabber(base_url, i + 1)

if __name__ == "__main__":
    grabber(''.join(sys.argv[1:]))
