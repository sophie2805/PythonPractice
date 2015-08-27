#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Sophie'

def blank_row(s):
    s = s.strip("\n\r\t   ")
    if len(s) == 0:
        return True
    else:
        return False

def note_row(s):
    s = s.strip("\n\r\t   ")
    if len(s) == 1:
        return "Code"
    elif len(s)>=2 and s[0]=='/' and s[1]=='/':
        return "Note"
    elif len(s)>=2 and s[0]=='/' and s[1]=='*':
        if s.rfind("*/") == -1 :
            return "NoteNotEnd"
        elif s.rfind("*/") == len(s) -2:
            return "Note"
        elif s.rfind("*/") < len(s) -2:
            return note_row(s[s.rfind("*/")+2:len(s)])
    elif s.rfind(";") == len(s) -1:#code
        return "Code"
    elif s.rfind(";")!=-1 and s.rfind(";") < len(s) -1:
        if note_row(s[s.rfind(";")+1:len(s)]) == "Note":
            return "Code"
        elif note_row(s[s.rfind(";")+1:len(s)]) == "NoteNotEnd":
            return "Code_NoteNotEnd"
        elif note_row(s[s.rfind(";")+1:len(s)]) == "Code":
            return "Code"
    elif s.rfind(";") == -1:
        if s.rfind("/*") == -1:
            return "Code"
        else:
            return "NoteNotEnd"

def note_blank_row_count(list_of_codes):
    l = len(list_of_codes)
    i = 1
    list_of_status=[]

    # analyze the very 1st line
    if blank_row(list_of_codes[0]):
        list_of_status.append("Blank")
    else:
        list_of_status.append(note_row(list_of_codes[0]))

    while i < l:
        if list_of_status[i-1]=="Code" or list_of_status[i-1]=="Note"or list_of_status[i-1]=="Blank"or list_of_status[i-1]=="NoteEnd":
            if blank_row(list_of_codes[i]):
                list_of_status.append("Blank")
            else:
                list_of_status.append(note_row(list_of_codes[i]))
            i += 1
            continue

        elif list_of_status[i-1]=="Code_NoteNotEnd"or list_of_status[i-1]=="NoteNotEnd":
            pos = list_of_codes[i].rfind("*/")
            if pos == -1:
                i += 1
                list_of_status.append("NoteNotEnd")
                continue
            else:
                if blank_row(list_of_codes[i][pos+2:len(list_of_codes[i])-1]):
                    list_of_status.append("NoteEnd")
                else:
                    list_of_status.append(note_row(list_of_codes[i][pos+2:len(list_of_codes[i])-1]))
                i += 1

    return list_of_status



if __name__ == '__main__':
    file = open("/Users/Sophie/IdeaProjects/BBSAutoLoginReplyScreenShot/src/test.java",'r')
    try:
        list_of_rows = file.readlines()
    finally:
        file.close()

    total_row = len(list_of_rows)
    blank = 0
    code = 0
    #print total_row
    analyze_result = note_blank_row_count(list_of_rows)

    for i in range(len(analyze_result)):
        print "row " , i+1, "~~~~",analyze_result[i]

    for x in analyze_result:
        if x == "Blank":
            blank += 1
        elif "Code" in x:
            code += 1

    note = total_row - blank - code
    print "Total row: ", total_row, "\nBlank row: ",blank,"\nCode row: ",code,"\nNote row: ",note