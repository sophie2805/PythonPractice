#! /usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

__author__ = 'Sophie'

def stamp_num(img,num):
    drawSurface = ImageDraw.Draw(img)
    print img.size
    numFont = ImageFont.truetype("ArialHB.ttc",300)
    drawSurface.text((600,0),num,fill=(255,0,0),font=numFont)
    img = img.resize((img.size[0]/5,img.size[1]/5))
    img.save("/Users/Sophie/Downloads/tencent_999.jpg")
    img.show()

if __name__ == '__main__':
    img = Image.open("/Users/Sophie/Downloads/tencent.jpg")
    stamp_num(img,"999")





