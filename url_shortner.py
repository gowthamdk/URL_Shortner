from __future__ import with_statement
import contextlib
from urllib import urlencode
from urllib2 import urlopen
import sys

def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + 
    urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

def main():
    urls = ['http://splinter.readthedocs.org/en/latest/api/driver-and-element-api.html#elementapi',
            'http://pythonhosted.org/Pafy/',
            'http://pythontips.com/2013/08/03/a-url-shortener-in-python/',
            'http://cricbuzz.com/']
    for tinyurl in map(make_tiny, urls):
        print(tinyurl)
      
if __name__ == '__main__':
    main()
