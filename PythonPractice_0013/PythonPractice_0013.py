#! /usr/bin/env python
#! -*- coding:utf-8 -*-

__author__ = 'Sophie2805'

import urllib2
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    url ="http://tieba.baidu.com/p/2166231880"
    save_path = "/Users/Sophie/Downloads/shanben_pic/"

    headers = {
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
            'Referer':"http://tieba.baidu.com"
    }
    req = urllib2.Request(url = url ,headers = headers)
    html = urllib2.urlopen(req).read()

    # non-greedy mode to find all the pic, BS would not work here because the html is not normal
    p = re.compile('<img.+?class="BDE_Image".+?>')
    list_of_pic = p.findall(html)

    counter = 1
    for x in list_of_pic:
        soup = BeautifulSoup(x)
        url = soup.img['src']
        req = urllib2.Request(url=url, headers=headers)
        pic = urllib2.urlopen(url).read()
        postfix = url[url.rfind('.'):]
        #print postfix
        file = open(save_path+str(counter)+postfix,'w')
        try:
            file.write(pic)
        finally:
            file.close()
        counter += 1