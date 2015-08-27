#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sophie'

from collections import OrderedDict

class AppearanceCounter(object):
    def __init__(self):
        self.dict = {}

    def add_count(self,item):
        count = self.dict.setdefault(item, 0)
        self.dict[item] = count + 1

    def sort(self, desc = None):
        """~~~~~~Method 1~~~~~~~~~"""
        #result = sorted([(v,k) for (k,v) in self.dict.items()], reverse = desc)

        """~~~~~~Method 2~~~~~~~~"""
        result = OrderedDict(sorted(self.dict.items(), key = lambda x: x[1], reverse = desc))

        return result

if __name__ == '__main__':
    ac = AppearanceCounter()
    file = open('/Users/Sophie/PycharmProjects/Practice_0004/CNN_News.txt','r')
    try:
        list_of_all_lines = file.readlines()
    finally:
        file.close()

    list_of_all_words = []
    temp = []

    for x in list_of_all_lines:
        temp = [t.strip(".?\"!,()'") for t in x.lower().split()]
        list_of_all_words.extend(temp)

    for x in list_of_all_words:
        ac.add_count(x)

    r = ac.sort(True)
    print r