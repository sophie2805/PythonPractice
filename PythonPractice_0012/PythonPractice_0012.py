#! /usr/bin/env python
#! -*- coding: utf-8 -*-

__author__ = 'Sophie'

import re

if __name__ == '__main__':
    file = open("/Users/Sophie/PycharmProjects/PythonPractice/PythonPractice_0012/key_word.txt","r")
    list_key_word =[]
    try:
        list_key_word = file.readlines()
    finally:
        file.close()
    for i in range(len(list_key_word)):
        list_key_word[i]=list_key_word[i].strip(" \n")
    while(True):
        userinput = raw_input("Please input something.\n")
        result = ""
        for x in list_key_word:
            #result = userinput.replace(x,"*")
            result = re.sub(x,"*",userinput)
            userinput = result
        print result
        continue_or_not = raw_input("Do you want continue? Please input y/n. Any other inputs will be taken as y.\n")
        if continue_or_not.lower() == 'n':
            break

