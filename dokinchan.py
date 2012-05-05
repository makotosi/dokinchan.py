#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'makotosiraisi3@gmail.com (Makoto Siraisi)'

import os
import sys, codecs
import json
import urllib

sys.stdout = codecs.EncodedFile(sys.stdout, 'utf_8')

APP_ID = ''
query = 'ドキンちゃん'
base_url = "http://api.search.live.net/json.aspx?Appid=%s&query=%s&sources=image&image.count=50" % (APP_ID, query)
urls = []

def get_data(base_url):
    bing = urllib.urlopen(base_url)
    data = json.load(bing)
    for i in range(50):
    	urls.append(data['SearchResponse']['Image']['Results'][i]['MediaUrl'])

def get_dokin_chan(urls):
    get_data(base_url)
    for i in range(len(urls)):
    	img = urllib.urlopen(urls[i])
    	f = open( os.path.basename(urls[i]), 'wb')
    	f.write(img.read())
    	img.close()
    	f.close()

if APP_ID == '':
    exit('Please check APP_ID')

if __name__ == '__main__':
    get_dokin_chan(urls)

